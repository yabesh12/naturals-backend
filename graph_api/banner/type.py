import graphene
from graphene_django import DjangoObjectType

from apps.banner.models import Banner


class BannerType(DjangoObjectType):
    """
    Banner Video Type
    """
    banner_desktop_video_url = graphene.String()
    banner_mobile_video_url = graphene.String()

    class Meta:
        model = Banner
        fields = "__all__"
        interfaces = (graphene.relay.Node,)

    def resolve_banner_desktop_video_url(self, info):
        """
        change the relative path to absolute path for desktop video
        """
        return info.context.build_absolute_uri(self.desktop_video.url)

    def resolve_banner_mobile_video_url(self, info):
        """
        change the relative path to absolute path for mobile video
        """
        return info.context.build_absolute_uri(self.mobile_video.url)
