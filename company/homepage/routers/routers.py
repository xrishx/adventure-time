from rest_framework.routers import DefaultRouter
from company.homepage.viewsets.viewsets import HomepageVideoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'homepage', HomepageVideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]