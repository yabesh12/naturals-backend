import graphene
from graphene_django import DjangoObjectType

from apps.testimonial.models import Testimonial


class TestimonialType(DjangoObjectType):
    testimonial_desktop_video_url = graphene.String()
    testimonial_mobile_video_url = graphene.String()

    class Meta:
        model = Testimonial
        fields = "__all__"
        interfaces = (graphene.relay.Node,)

    def resolve_testimonial_desktop_video_url(self, info):
        """
        change the relative path to absolute path for desktop video
        """
        return info.context.build_absolute_uri(self.desktop_video.url)

    def resolve_testimonial_mobile_video_url(self, info):
        """
        change the relative path to absolute path for mobile video
        """
        return info.context.build_absolute_uri(self.mobile_video.url)
