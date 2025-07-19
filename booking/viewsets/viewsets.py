from rest_framework import viewsets, filters
from booking.models import Booking
from booking.serializers.serializers import BookingReadSerializer, BookingWriteSerializer
from booking.utilities.pagination import MyPageNumberPagination

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BookingReadSerializer
        return BookingWriteSerializer
    
    def perform_create(self, serializer):
        booking = serializer.save()

        try:    
                # 1. Send email to the user (Booking Confirmation)
            subject = 'Your Trip Booking Confirmation'
            message = render_to_string('emails/booking_confirmation.html', {'booking': booking})
            user_email = booking.email  # Assuming you have an email field in the booking form
            user_email_message = EmailMessage(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
            )
            user_email_message.content_subtype = "html"  # Set the content type to HTML
            user_email_message.send()

                # 2. Send email to the admin (New Booking Notification)
            admin_subject = 'New Booking Submitted'
            admin_message = render_to_string('emails/new_booking_admin.html', {'booking': booking})
            admin_email = settings.ADMIN_EMAIL  # The admin email address
            admin_email_message = EmailMessage(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                [admin_email],  # Send to the admin's email
            )
            admin_email_message.content_subtype = "html"  # Set the content type to HTML
            admin_email_message.send()

        except Exception as e:
            # Handle errors (you can log the error or send an admin notification)
            print(f"Error sending email: {e}")


