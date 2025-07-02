from rest_framework import viewsets, filters
from blog.models import Blog
from blog.serializers.serializers import BlogReadSerializer, BlogCreateSerializer
from blog.utilities.pagination import MyPageNumberPagination

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BlogReadSerializer
        return BlogCreateSerializer