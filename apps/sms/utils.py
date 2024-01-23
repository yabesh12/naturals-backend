import os
import requests

sms_provider = os.environ.get('SMS_PROVIDER')


def process_sms(mobile_number, otp, timeout):
    """
    Process sms based on the sms_provider and Sending OTP to the user
    :param mobile_number: To which mobile number OTP has to send
    :param otp: Otp code for a user
    :return:
    """
    content = f"Hi! Your OTP for logging into Naturals Bridal Services is {otp}. OTP is valid for {timeout} minutes. Do not share with anyone."
    if sms_provider == 'Kalerya':
        url = "https://api-alerts.kaleyra.com/v4/"
        querystring = {"method": "sms", "sender": os.environ.get('KALEYRA_SENDER_ID'), "to": "91" + str(mobile_number),
                       "message": content,
                       "api_key": os.environ.get('KALEYRA_KEY')}
        response = requests.request("GET", url, params=querystring)
        return response
    elif sms_provider == 'winnovature':
        url = "https://api.itextos.com/genericapi/QSGenericReceiver"
        querystring = {
            "version": "1.0",
            "header": os.environ.get('WINNOVATURE_SENDER_ID'),
            "type": "PM",
            "dest": "91" + str(mobile_number),
            "msg": content,
            "accesskey": os.environ.get('WINNOVATURE_ACCESS_KEY')
        }
        response = requests.request("GET", url, params=querystring)
        return response
