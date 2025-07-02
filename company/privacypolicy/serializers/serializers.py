from rest_framework import serializers
from company.privacypolicy.models import PrivacyPolicy

class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['content']
        read_only_fields = ['id', 'created_at', 'updated_at']
