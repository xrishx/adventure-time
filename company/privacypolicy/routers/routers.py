from rest_framework.routers import DefaultRouter
from company.privacypolicy.viewsets.viewsets import PrivacyPolicyViewSet
from django.urls import path, include

privacypolicy_router = DefaultRouter()
privacypolicy_router.register(r'privacypolicy', PrivacyPolicyViewSet)

urlpatterns = [
    path('', include(privacypolicy_router.urls)),
]