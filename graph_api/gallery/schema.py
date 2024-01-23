import graphene

from apps.gallery.models import BridalGallery
from graph_api.gallery.type import BridalGalleryType


class GalleryQuery(graphene.ObjectType):
    get_bridal_gallery_images = graphene.List(BridalGalleryType)

    def resolve_get_bridal_gallery_images(self, info):
        """
        Returns Bridal Gallery Images
        """
        return BridalGallery.objects.all()
