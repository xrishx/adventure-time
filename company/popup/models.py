from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Popup(models.Model):
    title = models.CharField(max_length=100, help_text='Popup Title')
    image_file = models.ImageField(upload_to='images/popup', null=True, blank=True, help_text='Upload an image file')
    image_link = models.URLField(null=True, blank=True, max_length=500, help_text='Image Link')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.image_file and not self.image_link:
            raise ValidationError('Either image file or image link must be provided.')
        elif self.image_file and self.image_link:
            raise ValidationError('Please proivide either image file or image link, not both')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Pop Up'
        verbose_name_plural = 'Pop Ups'