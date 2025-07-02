from rest_framework.routers import DefaultRouter
from company.homepage.viewsets.viewsets import HomepageVideoViewSet
from django.urls import path, include

homepage_router = DefaultRouter()
homepage_router.register(r'homepage', HomepageVideoViewSet)

urlpatterns = [
    path('', include(homepage_router.urls)),
]