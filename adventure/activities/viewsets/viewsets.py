from rest_framework import viewsets, filters
from adventure.activities.models import Activity
from adventure.activities.serializers.serializers import ActivityReadSerializer, ActivityWriteSerializer
from adventure.activities.utilities.pagination import MyPageNumberPagination

class ActivityViewSet(viewsets.ModelViewSet):
    
    queryset = Activity.objects.all()
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ActivityReadSerializer
        return ActivityWriteSerializer