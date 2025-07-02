from django.db import models

# Create your models here.
class VisaInformation(models.Model):
    content = models.TextField(unique=True, help_text='Visa Information Content')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return f'Visa and Information (last updated: {self.updated_at.strftime("%Y-%m-%d %H:%M")})'
    
    class Meta:
        verbose_name = 'Visa and Information'
        verbose_name_plural = 'Visa and Information'