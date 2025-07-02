from rest_framework.routers import DefaultRouter
from reviews.viewsets.viewsets import ReviewViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls