from rest_framework.routers import DefaultRouter
from adventure.activities.viewsets.viewsets import ActivityViewSet
from django.urls import path, include

activities_router = DefaultRouter()
activities_router.register(r'activities', ActivityViewSet)

url_patterns = [
    path('', include(activities_router.urls)),
]