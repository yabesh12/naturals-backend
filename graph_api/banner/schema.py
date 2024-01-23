import graphene

from apps.banner.models import Banner
from graph_api.banner.type import BannerType


class BannerQuery(graphene.ObjectType):
    get_banner_video = graphene.Field(BannerType)

    def resolve_get_banner_video(self, info):
        """
        Return Single Banner Video
        """
        return Banner.objects.last()
