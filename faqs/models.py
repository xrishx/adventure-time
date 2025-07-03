from django.db import models

# Create your models here.
class Faq(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    # destination = models.ForeignKey('adventure.destination', on_delete=models.CASCADE, help_text='Destination')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return self.title + f'(last updated: {self.updated_at.strftime("%Y-%m-%d %H:%M")})'

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'