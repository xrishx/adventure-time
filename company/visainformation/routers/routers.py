from rest_framework.routers import DefaultRouter
from company.visainformation.viewsets.viewsets import VisaInformationViewSet
from django.urls import path, include

visainformation_router = DefaultRouter()
visainformation_router.register(r'visainformation', VisaInformationViewSet)

urlpatterns = [
    path('', include(visainformation_router.urls)),
]