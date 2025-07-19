from django.db import models
from adventure.destination.models import Destination

class Activity(models.Model):
    name = models.CharField(max_length=255, help_text='Activity Name')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, help_text='Destination')
    image = models.ImageField(upload_to='images/activities', null=True, blank=True, help_text='Upload an image file')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return f'{self.name} + {self.destination}'
    
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'