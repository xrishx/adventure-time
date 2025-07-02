from rest_framework import viewsets, filters
from queries.models import Query
from queries.serializers.serializers import QueryReadSerializer, QueryCreateSerializer
from queries.utilities.pagination import MyPageNumberPagination

class QueryViewSet(viewsets.ModelViewSet):
    
    queryset = Query.objects.all()
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return QueryReadSerializer
        return QueryCreateSerializer

