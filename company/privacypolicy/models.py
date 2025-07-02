from django.db import models

# Create your models here.
class PrivacyPolicy(models.Model):
    content = models.TextField(unique=True, help_text='Privacy Policy Content')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return f'Privacy Policy'
    
    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policies'
