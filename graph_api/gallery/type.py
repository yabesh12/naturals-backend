import graphene
from graphene_django import DjangoObjectType

from apps.gallery.models import BridalGallery


class BridalGalleryType(DjangoObjectType):
    gallery_desktop_image_url = graphene.String()
    gallery_mobile_image_url = graphene.String()

    class Meta:
        model = BridalGallery
        fields = "__all__"
        interfaces = (graphene.relay.Node,)

    def resolve_gallery_desktop_image_url(self, info):
        """
        change the relative path to absolute path for desktop image
        """
        return info.context.build_absolute_uri(self.desktop_image.url)

    def resolve_gallery_mobile_image_url(self, info):
        """
        change the relative path to absolute path for mobile image
        """
        return info.context.build_absolute_uri(self.mobile_image.url)
