from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from adventure.activities.models import Activity
from adventure.package.models import Package
from adventure.destination.models import Destination

# Create your models here.
class Booking(models.Model):
    class Airline(models.TextChoices):
        YETI = 'Yeti Airlines', 'Yeti Airlines'
        EMIRATES = 'Fly Emirates', 'Fly Emirates'
        QATAR = 'Qatar Airways', 'Qatar Airways'
        DELTA = 'Delta Airlines', 'Delta Airlines'
        LUFTHANSA = 'Lufthansa', 'Lufthansa'
        AIR_FRANCE = 'Air France', 'Air France'
        BA = 'British Airways', 'British Airways'
        SOUTHWEST = 'Southwest Airlines', 'Southwest Airlines'
        ANA = 'ANA', 'ANA'
        JAL = 'Japan Airlines', 'Japan Airlines'
    
    class Service(models.TextChoices):
        BUDGET = 'budget', 'Budget'
        STANDARD = 'standard', 'Standard'
        PREMIUM = 'premium', 'Premium'

    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(help_text='Email')
    phone_number = models.CharField(max_length=10, help_text= 'Phone number')
    country = CountryField(help_text='Country')
    airlines = models.CharField(max_length=100, choices=Airline.choices, help_text='Airlines')
    no_of_travellers = models.IntegerField(help_text='Number of travellers')

    # Activity Details
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT, help_text='Activity')
    package = models.ManyToManyField(Package, help_text='Package')
    destination = models.ForeignKey(Destination, on_delete=models.PROTECT,null=True, help_text='Destination')

    arrival_date = models.DateField(help_text='Arrival Date')
    departure_date = models.DateField(help_text='Departure Date')
    service_type = models.CharField(max_length=10, choices=Service.choices, help_text='Service Type')
    customize_trip = models.TextField(help_text='Customize Trip Here', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return f'{self.full_name} + {self.destination}'

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'