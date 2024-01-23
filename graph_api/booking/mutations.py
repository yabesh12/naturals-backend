from datetime import datetime

import graphene
from graphql import GraphQLError
from graphql_relay import from_global_id
from django.core.cache import cache

from apps.booking.models import Booking, State, City, Service
from graph_api.booking.type import BookingType
from graph_api.booking.utils import validate_phone_number, generate_otp, verify_otp, validate_email, block_spam_request, \
    mobile_requested_for_otp


class SendOtp(graphene.Mutation):
    """
    Validate Mobile number and send otp
    """

    class Arguments:
        mobile_number = graphene.String(required=True)

    status = graphene.String()
    message = graphene.String()

    def mutate(self, info, mobile_number, **kwargs):
        validate_phone_number(mobile_number)
        block_spam_request(mobile_number)
        generate_otp(mobile_number)
        return SendOtp(status='success', message='otp has been sent to your mobile number')


class VerifyOtp(graphene.Mutation):
    """
    Validate the otp with the particular mobile number
    """

    class Arguments:
        mobile_number = graphene.String(required=True)
        otp = graphene.String(required=True)

    status = graphene.String()
    message = graphene.String()

    def mutate(self, info, mobile_number, otp):
        validate_phone_number(mobile_number)
        if mobile_requested_for_otp(mobile_number):
            if verify_otp(mobile_number, otp):

                return VerifyOtp(status='success', message='otp verified successfully')
            else:
                return VerifyOtp(status='error', message='Invalid otp!')


class ResendOtp(graphene.Mutation):
    """
    Resend the otp
    """

    class Arguments:
        mobile_number = graphene.String(required=True)

    status = graphene.String()
    message = graphene.String()

    def mutate(self, info, mobile_number):
        validate_phone_number(mobile_number)
        block_spam_request(mobile_number)
        generate_otp(mobile_number)
        return ResendOtp(status='success', message='otp has been sent to your mobile number')


class CreateBooking(graphene.Mutation):
    """
    Mutation to create a record for section 'Book with us now in naturals'
    Required Fields
    -> First name, Last name, mobile no, email, service, booking date, state id, city id
    Optional
    -> message
    Returns Booking object with success status if valid or status with error
    """

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        mobile_number = graphene.String(required=True)
        email_id = graphene.String(required=True)
        service_id = graphene.String(required=True)
        booking_date = graphene.String(required=True)
        state_id = graphene.String(required=True)
        city_id = graphene.String(required=True)
        message = graphene.String()

    booking = graphene.Field(BookingType)
    status = graphene.String()
    message = graphene.String()

    def mutate(self, info, first_name, last_name, mobile_number, email_id, service_id, booking_date, state_id, city_id,
               *args,
               **kwargs):
        validate_phone_number(mobile_number)
        validate_email(email_id)
        if cache.get(f"{mobile_number}-verified") is None:
            raise GraphQLError("Please Verify your mobile number!")
        try:
            service_obj = Service.objects.get(id=from_global_id(service_id)[1])
        except Exception:
            raise GraphQLError("Invalid Service!")

        try:
            state_obj = State.objects.get(id=from_global_id(state_id)[1])
        except Exception:
            raise GraphQLError("Invalid State!")

        try:
            city_obj = City.objects.get(state=state_obj, id=from_global_id(city_id)[1])
        except Exception:
            raise GraphQLError("Invalid City!")

        try:

            booking_obj = Booking.objects.create(first_name=first_name,
                                                 last_name=last_name,
                                                 mobile_number=mobile_number,
                                                 email=email_id,
                                                 service=service_obj,
                                                 booking_date=datetime.strptime(booking_date, "%Y-%m-%d"),
                                                 state=state_obj,
                                                 city=city_obj,
                                                 message=kwargs.get('message')
                                                 )

            cache.delete(f"{mobile_number}-verified")

            return CreateBooking(booking=booking_obj, status="Success", message="Successfully Booked")


        except Exception as e:
            return e


class BookingMutation(graphene.ObjectType):
    send_otp = SendOtp.Field()
    verify_otp = VerifyOtp.Field()
    resend_otp = ResendOtp.Field()
    create_booking = CreateBooking.Field()
