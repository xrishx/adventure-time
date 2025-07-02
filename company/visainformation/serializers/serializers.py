from rest_framework import serializers
from company.visainformation.models import VisaInformation

class VisaInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaInformation
        fields = ['content']
        read_only_fields = ['id', 'created_at', 'updated_at']

