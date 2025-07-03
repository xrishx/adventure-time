from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100, help_text='Full Name')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text='Star Rating (1-5)')
    review = models.TextField(max_length=1000, help_text='Review')
    image = models.ImageField(upload_to='images/reviews', null=True, blank=True, help_text='Upload an image file')
    show = models.BooleanField(default=False, help_text='Show?')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return self.name + f'(date created: {self.created_at.strftime("%Y-%m-%d %H:%M")})'
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'