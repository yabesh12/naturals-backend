import graphene

from apps.experts.models import BridalExpert
from graph_api.experts.type import BridalExpertsType


class BridalExpertsQuery(graphene.ObjectType):
    get_bridal_experts = graphene.List(BridalExpertsType)

    def resolve_get_bridal_experts(self, info):
        """
        Return list of Bridal Experts
        """
        return BridalExpert.objects.all()
