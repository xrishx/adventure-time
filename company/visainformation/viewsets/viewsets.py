from rest_framework import viewsets
from company.visainformation.models import VisaInformation
from company.visainformation.serializers.serializers import VisaInformationSerializer

class VisaInformationViewSet(viewsets.ModelViewSet):
    queryset = VisaInformation.objects.all()
    serializer_class = VisaInformationSerializer
    