from rest_framework import serializers
from company.termsconditions.models import TermsConditions

class TermsConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsConditions
        fields = ['content']
        read_only_fields = ['id', 'created_at', 'updated_at']