from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 20

# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     max_limit = 20

