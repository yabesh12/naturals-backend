import graphene
from graphene_django import DjangoObjectType

from apps.services.models import Service


class ServicesType(DjangoObjectType):
    services_desktop_image_url = graphene.String()
    services_mobile_image_url = graphene.String()

    class Meta:
        model = Service
        fields = "__all__"
        interfaces = (graphene.relay.Node,)

    def resolve_services_desktop_image_url(self, info):
        """
        change the relative path to absolute path for desktop image
        """
        return info.context.build_absolute_uri(self.desktop_image.url)

    def resolve_services_mobile_image_url(self, info):
        """
        change the relative path to absolute path for mobile image
        """
        return info.context.build_absolute_uri(self.mobile_image.url)
