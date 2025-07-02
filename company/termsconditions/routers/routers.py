from rest_framework.routers import DefaultRouter
from company.termsconditions.viewsets.viewsets import TermsConditionsViewSet
from django.urls import path, include

termsconditions_router = DefaultRouter()
termsconditions_router.register(r'termsconditions', TermsConditionsViewSet)

urlpatterns = [
    path('', include(termsconditions_router.urls)),
]