from rest_framework import viewsets
from company.privacypolicy.models import PrivacyPolicy
from company.privacypolicy.serializers.serializers import PrivacyPolicySerializer


class PrivacyPolicyViewSet(viewsets.ModelViewSet):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer
    