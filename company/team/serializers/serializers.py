from rest_framework import serializers
from company.team.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'position', 'description', 'image']
        read_only_fields = ['id', 'created_at', 'updated_at']
