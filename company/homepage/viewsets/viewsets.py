from rest_framework import viewsets
from company.homepage.models import HomepageVideo
from company.homepage.serializers.serializers import HomepageVideoSerializer


class HomepageVideoViewSet(viewsets.ModelViewSet):
    queryset = HomepageVideo.objects.all()
    serializer_class = HomepageVideoSerializer
    