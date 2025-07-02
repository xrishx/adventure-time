from rest_framework.routers import DefaultRouter
from company.popup.viewsets.viewsets import PopupViewSet
from django.urls import path, include

popup_router = DefaultRouter()
popup_router.register(r'popup', PopupViewSet)

urlpatterns = [
    path('', include(popup_router.urls)),
]