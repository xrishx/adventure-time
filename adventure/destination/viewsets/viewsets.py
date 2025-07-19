from rest_framework import viewsets
from adventure.destination.models import Destination, Departure, GalleryImage
from adventure.destination.serializers.serializers import (
    DestinationReadSerializer,
    DestinationWriteSerializer,
    DepartureSerializer,
    GalleryImageSerializer,
)
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DestinationReadSerializer
        return DestinationWriteSerializer

class DepartureViewSet(viewsets.ModelViewSet):
    queryset = Departure.objects.all()
    serializer_class = DepartureSerializer

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer