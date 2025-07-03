from rest_framework import viewsets
from faqs.models import Faq
from faqs.serializers.serializers import FaqSerializer
from rest_framework import filters


class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
