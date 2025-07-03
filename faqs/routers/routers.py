from rest_framework.routers import DefaultRouter
from faqs.viewsets.viewsets import FaqViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'faqs', FaqViewSet)

urlpatterns = router.urls
