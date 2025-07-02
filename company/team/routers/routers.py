from rest_framework.routers import DefaultRouter
from company.team.viewsets.viewsets import TeamViewSet
from django.urls import path, include

team_router = DefaultRouter()
team_router.register(r'team', TeamViewSet)

urlpatterns = [
    path('', include(team_router.urls)),
]