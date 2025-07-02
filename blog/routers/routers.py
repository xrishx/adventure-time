from rest_framework.routers import DefaultRouter
from blog.viewsets.viewsets import BlogViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'blog', BlogViewSet)

urlpatterns = router.urls