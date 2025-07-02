from rest_framework.routers import DefaultRouter
from queries.viewsets.viewsets import QueryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'queries', QueryViewSet)

urlpatterns = router.urls