from rest_framework.routers import DefaultRouter
from company.legaldocs.viewsets.viewsets import LegalDocsViewSet
from django.urls import path, include

legaldocs_router = DefaultRouter()
legaldocs_router.register(r'legaldocs', LegalDocsViewSet)

urlpatterns = [
    path('', include(legaldocs_router.urls)),
]