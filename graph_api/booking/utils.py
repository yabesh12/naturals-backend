import base64
from datetime import datetime
import pyotp
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.validators import validate_email as validate_email_prebuilt
from graphql import GraphQLError

from apps.sms.utils import process_sms


def validate_phone_number(mobile_number):
    """
    Validating user given mobile number has valid length or not

    :param mobile_number: (integer) mobile number to validate
    :return: Exception
    """
    if mobile_number:
        if len(str(mobile_number)) != 10:
            raise GraphQLError('Enter a valid mobile Number')
        if not str(mobile_number).isnumeric():
            raise GraphQLError('Mobile Number should be Integer')
    else:
        raise GraphQLError("Mobile Number Cannot be empty")


def gen_key(phone):
    return str(phone) + str(datetime.date(datetime.now())) + pyotp.random_base32()


def generate_otp(mobile_number):
    """
    Generates a 6 digit OTP
    otp cache time set to 5 minutes, after that otp will expire
    """
    key = base64.b32encode(gen_key(mobile_number).encode())
    otp = pyotp.TOTP(key, interval=320, digits=6)
    otp_code = otp.now()
    cache.set(f"{mobile_number}-otp", otp_code, timeout=300)
    print(otp_code)
    process_sms(mobile_number, otp=otp_code, timeout=5)
    return otp_code


def verify_otp(mobile_number, otp_code):
    """
    Verifying OTP code provided by the user

    @:param mobile_number: user mobile number
    @:param otp_code: OTP code provided by the user
    @:return: Boolean
    """
    if otp_code:
        if cache.get(f"{mobile_number}-otp") == otp_code:
            cache.delete(f"{mobile_number}-otp")
            # set 15 min to verified mobile for booking purpose
            cache.set(f"{mobile_number}-verified", otp_code, timeout=900)
            return True
        else:
            return False
    else:
        return False


def validate_email(email):
    """
    Validating email provided by the user has correct syntax or not
    @:param email: pass email to validate
    :return: Boolean
    """
    try:
        validate_email_prebuilt(email)
        return True
    except ValidationError:
        raise Exception("Enter a valid Email!")


def block_spam_request(mobile_number):
    """
    Restrictions :
    one mobile number can receives otp 3 times within a minute
    """
    data = cache.get(f"{mobile_number}-req")
    print(data)
    count = 1
    if data is None:
        cache.set(f"{mobile_number}-req", count, timeout=60)
    else:
        if int(data) >= 3:
            raise GraphQLError("Please try again after a minute!")
        data += 1
        cache.set(f"{mobile_number}-req", data, timeout=60)
    return True


def mobile_requested_for_otp(mobile_number):
    """
    Check if the mobile number is requested for send otp then verify the otp
    otherwise block the request
    """
    value = cache.get(f"{mobile_number}-otp")
    if value is None:
        raise GraphQLError("Invalid Request for Verify OTP! Try Send OTP.")
    return True

