from rest_framework import viewsets, filters
from adventure.package.models import Package
from adventure.package.serializers.serializers import PackageReadSerializer, PackageWriteSerializer
from adventure.package.utilities.pagination import MyPageNumberPagination

class PackageViewSet(viewsets.ModelViewSet):
    
    queryset = Package.objects.all()
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PackageReadSerializer
        return PackageWriteSerializer