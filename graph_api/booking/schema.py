import graphene
from graphql import GraphQLError
from graphql_relay import from_global_id

from apps.booking.models import City, State, Service
from graph_api.booking.type import StateType, CityType, ServiceType


class BookingDataQuery(graphene.ObjectType):
    get_services = graphene.List(ServiceType)
    get_states = graphene.List(StateType)
    get_cities_by_state = graphene.List(CityType, state_id=graphene.ID(required=True))

    def resolve_get_services(root, info):
        """
        Return List of Services that are available
        """
        return Service.objects.all()

    def resolve_get_states(root, info):
        """
        Return List of States
        """
        return State.objects.all()

    def resolve_get_cities_by_state(root, info, state_id):
        """
        :params: state id
        Return List of cities associated with particular state object
        """
        try:
            state_obj = State.objects.get(id=from_global_id(state_id)[1])
        except Exception:
            raise GraphQLError("Invalid State!")

        return City.objects.filter(state=state_obj)
