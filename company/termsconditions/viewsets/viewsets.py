from rest_framework import viewsets
from company.termsconditions.models import TermsConditions
from company.termsconditions.serializers.serializers import TermsConditionsSerializer

class TermsConditionsViewSet(viewsets.ModelViewSet):
    queryset = TermsConditions.objects.all()
    serializer_class = TermsConditionsSerializer
    