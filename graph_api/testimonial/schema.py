import graphene

from apps.testimonial.models import Testimonial
from graph_api.testimonial.type import TestimonialType


class TestimonialQuery(graphene.ObjectType):
    get_customer_testimonials = graphene.List(TestimonialType)

    def resolve_get_customer_testimonials(root, info):
        """
        Return list of customer testimonials
        """
        return Testimonial.objects.all()
