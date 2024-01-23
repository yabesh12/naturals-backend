import graphene
from graphene_django import DjangoObjectType

from apps.glimpse.models import GlimpseVideoCarousel


class GlimpseVideoCarouselType(DjangoObjectType):
    """
    Glimpse section video carousel Type
    """
    glimpse_desktop_video_url = graphene.String()
    glimpse_mobile_video_url = graphene.String()

    class Meta:
        model = GlimpseVideoCarousel
        fields = "__all__"
        interfaces = (graphene.relay.Node,)

    def resolve_glimpse_desktop_video_url(self, info):
        """
        change the relative path to absolute path for desktop video
        """
        return info.context.build_absolute_uri(self.desktop_video.url)

    def resolve_glimpse_mobile_video_url(self, info):
        """
        change the relative path to absolute path for mobile video
        """
        return info.context.build_absolute_uri(self.mobile_video.url)
