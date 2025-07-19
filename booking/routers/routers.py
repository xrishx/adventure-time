from rest_framework.routers import DefaultRouter
from booking.viewsets.viewsets import BookingViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls