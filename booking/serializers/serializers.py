from rest_framework import serializers
from booking.models import Booking

class BookingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['full_name', 'email','phone_number', 'country', 'airlines', 'no_of_travellers', 'activity', 'package', 'destination', 'arrival_date', 'departure_date', 'service_type', 'customize_trip']

class BookingReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'created_at',
                'full_name',
                'phone_number',
                'email',
                'country',
                'airlines',
                'activity', 'package', 'destination', 'customize_trip']
        
