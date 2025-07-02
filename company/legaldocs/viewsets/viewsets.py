from rest_framework import viewsets
from company.legaldocs.models import LegalDocs
from company.legaldocs.serializers.serializers import LegalDocsSerializer

class LegalDocsViewSet(viewsets.ModelViewSet):
    queryset = LegalDocs.objects.all()
    serializer_class = LegalDocsSerializer