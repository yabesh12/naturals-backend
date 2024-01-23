import graphene

from graph_api.banner.schema import BannerQuery
from graph_api.booking.mutations import BookingMutation
from graph_api.booking.schema import BookingDataQuery
from graph_api.experts.schema import BridalExpertsQuery
from graph_api.gallery.schema import GalleryQuery
from graph_api.glimpse.schema import GlimpseVideoCarouselQuery
from graph_api.services.schema import ServicesQuery
from graph_api.testimonial.schema import TestimonialQuery


class Query(BannerQuery,
            ServicesQuery,
            GalleryQuery,
            GlimpseVideoCarouselQuery,
            BridalExpertsQuery,
            TestimonialQuery,
            BookingDataQuery,
            graphene.ObjectType):
    pass


class Mutation(BookingMutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)
