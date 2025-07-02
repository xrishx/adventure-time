from rest_framework import viewsets
from company.team.models import Team
from company.team.serializers.serializers import TeamSerializer
from rest_framework import filters

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    