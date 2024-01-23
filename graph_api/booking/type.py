import graphene
from graphene_django import DjangoObjectType

from apps.booking.models import Booking, State, City, Service


class BookingType(DjangoObjectType):
    class Meta:
        model = Booking
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class StateType(DjangoObjectType):
    class Meta:
        model = State
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class CityType(DjangoObjectType):
    class Meta:
        model = City
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
