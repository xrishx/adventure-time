from rest_framework.routers import DefaultRouter
from adventure.destination.viewsets.viewsets import DestinationViewSet, DepartureViewSet, GalleryImageViewSet
from django.urls import path, include

destination_router = DefaultRouter()
destination_router.register(r'destination', DestinationViewSet)
destination_router.register(r'departures', DepartureViewSet)
destination_router.register(r'gallery-images', GalleryImageViewSet)

urlpatterns = [
    path('', include(destination_router.urls)),
]