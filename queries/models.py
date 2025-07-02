from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=100, help_text= 'Querer name')
    phone_number = PhoneNumberField(help_text= 'Querer phone number')
    message = models.TextField(max_length= 240, help_text= 'Querer message')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return self.name + f'(date created: {self.created_at.strftime("%Y-%m-%d %H:%M")})'

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'