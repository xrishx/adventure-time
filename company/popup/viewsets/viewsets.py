from rest_framework import viewsets
from company.popup.models import Popup
from company.popup.serializers.serializers import PopupSerializer

class PopupViewSet(viewsets.ModelViewSet):
    queryset = Popup.objects.all()
    serializer_class = PopupSerializer