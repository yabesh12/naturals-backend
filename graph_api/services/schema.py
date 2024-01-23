import graphene

from apps.services.models import Service
from graph_api.services.type import ServicesType


class ServicesQuery(graphene.ObjectType):
    get_our_services = graphene.List(ServicesType)

    def resolve_get_our_services(root, info):
        """
        Return List of Services
        """
        return Service.objects.all()
