from rest_framework import viewsets, filters
from reviews.models import Review
from reviews.serializers.serializers import ReviewCreateSerializer, ReviewReadSerializer
from reviews.utilities.pagination import MyPageNumberPagination

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReviewReadSerializer
        return ReviewCreateSerializer

