from django.db import models
from adventure.package.models import Package
from django.core.exceptions import ValidationError 

class Destination(models.Model):
    class Currency(models.TextChoices):
        USD = 'USD'
        EUR = 'EUR'
        AUD = 'AUD'
        NPR = 'NPR'
        INR = 'INR'

    # DESTINATION MODELS
    title = models.CharField(max_length=100, help_text='Destination Title', default='')
    package = models.ManyToManyField(Package)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Price')
    currency = models.CharField(max_length=3, choices=Currency.choices, default=Currency.USD, null=True, blank=True, help_text='Currency')
    is_allowed = models.BooleanField(default=False, help_text='Is Price Allowed?')

    # UPLOAD IMAGES
    feature_image = models.ImageField(upload_to='images/destinations', null=True, blank=True, help_text='Upload an image file')
    trip_pdf = models.FileField(upload_to='pdf/trips', null=True, blank=True, help_text='Upload a pdf file')
    # GalleryImage should go here

    # DETAILED DESCRIPTION
    overview = models.TextField(max_length=1000, help_text='Overview', null=True, blank=True)
    inclusion_exclusions = models.TextField(max_length=1000, help_text='Inclusions and Exclusions', null=True, blank=True)
    itinerary = models.TextField(max_length=1000, help_text='Itinerary', null=True, blank=True)
    trip_map = models.ImageField(upload_to='images/trip_map', null=True, blank=True, help_text='Upload an image file')
    trip_map_link = models.URLField(null=True, blank=True, max_length=500, help_text='Trip Map Link')
    gear_equipment = models.TextField(max_length=1000, help_text='Gear and Equipment', null=True, blank=True)
    useful_info = models.TextField(max_length=1000, help_text='Useful Information', null=True, blank=True)

    # AT A GLANCE
    duration = models.CharField(max_length=100, help_text='Duration', null=True, blank=True)
    trip_grade = models.CharField(max_length=100, help_text='Trip Grade', null=True, blank=True)
    best_season = models.CharField(max_length=100, help_text='Best Season', null=True, blank=True)
    max_altitude = models.CharField(max_length=100, help_text='Max Altitude', null=True, blank=True)
    meals = models.CharField(max_length=100, help_text='Meals', null=True, blank=True)
    nature_of_trip = models.CharField(max_length=100, help_text='Nature of Trip', null=True, blank=True)
    accomodation = models.CharField(max_length=100, help_text='Accomodation', null=True, blank=True)
    group_size = models.CharField(max_length=100, help_text='Group Size', null=True, blank=True)

    # DEPARTURE SHOULD BE HERE

    # META
    meta_keywords = models.CharField(max_length=100, help_text='Meta Keywords', null=True, blank=True)
    meta_descrip = models.CharField(max_length=100, help_text='Meta Description', null=True, blank=True)

    def clean(self):
        if self.is_allowed and self.price is None:
            raise ValidationError("An active price must have a value.")
        if not self.is_allowed:
            self.price = None

        if not self.trip_map and not self.trip_map_link:
            raise ValidationError('Either image file or image link must be provided.')
        elif self.trip_map and self.trip_map_link:
            raise ValidationError('Please provide either image file or image link, not both.')

    def __str__(self):
        return self.title

class Departure(models.Model):
    class Status(models.TextChoices):
        GUA = 'Guaranteed'
        NOTGUA = 'Not Guaranteed'

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='departures')
    start_date = models.DateField(help_text='Departure Start Date')
    end_date = models.DateField(help_text='Departure End Date')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Price')
    currency = models.CharField(max_length=3, choices=Destination.Currency.choices, default=Destination.Currency.USD, null=True, blank=True, help_text='Currency')
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.GUA, help_text='Status')

    def clean(self):
        if self.price is None:
            raise ValidationError("Price must be provided for each departure.")
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date.")

    def __str__(self):
        return f"{self.destination.title} - {self.start_date} to {self.end_date}"


class GalleryImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='images/gallery', help_text='Upload an image file')

    def __str__(self):
        return f"Gallery image for {self.destination.title}"