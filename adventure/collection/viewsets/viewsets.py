from rest_framework import viewsets, filters
from adventure.collection.models import Collection
from adventure.collection.serializers.serializers import CollectionReadSerializer, CollectionWriteSerializer
from adventure.collection.utilities.pagination import MyPageNumberPagination

class CollectionViewSet(viewsets.ModelViewSet):

    queryset = Collection.objects.all()
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CollectionReadSerializer
        return CollectionWriteSerializer
    
    