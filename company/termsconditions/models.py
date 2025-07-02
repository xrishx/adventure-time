from django.db import models

# Create your models here.
class TermsConditions(models.Model):
    content = models.TextField(unique=True, help_text='Terms and Conditions Content')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return f'Terms and Conditions (last updated: {self.updated_at.strftime("%Y-%m-%d %H:%M")})'
    
    class Meta:
        verbose_name = 'Terms and Conditions'
        verbose_name_plural = 'Terms and Conditions'