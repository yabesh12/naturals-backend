import graphene

from apps.glimpse.models import GlimpseVideoCarousel
from graph_api.glimpse.type import GlimpseVideoCarouselType


class GlimpseVideoCarouselQuery(graphene.ObjectType):
    get_glimpse_video_carousels = graphene.List(GlimpseVideoCarouselType)

    def resolve_get_glimpse_video_carousels(root, info):
        """
        Return list of Videos for Glimpse section
        """
        return GlimpseVideoCarousel.objects.all()
