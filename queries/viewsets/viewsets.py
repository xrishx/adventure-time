from rest_framework import viewsets, filters
from queries.models import Query
from typing import Type
from rest_framework import serializers
from queries.serializers.serializers import QueryReadSerializer, QueryCreateSerializer

class QueryViewSet(viewsets.ModelViewSet):
    
    queryset = Query.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return QueryReadSerializer
        return QueryCreateSerializer

