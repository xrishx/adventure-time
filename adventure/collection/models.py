from django.db import models
from adventure.destination.models import Destination

class Collection(models.Model):
    name = models.CharField(max_length=100, help_text='Collection Name')
    destination = models.ManyToManyField(Destination, help_text='Destination')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return f'{self.name} + {self.destination}'
    
    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'