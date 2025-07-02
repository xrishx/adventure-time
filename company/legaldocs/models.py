from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class LegalDocs(models.Model):
    image_file = models.ImageField(upload_to='images/legaldocs', null=True, blank=True, help_text='Upload an image file')
    image_link = models.URLField(null=True, blank=True, max_length=500, help_text='Image Link')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def clean(self):
        if not self.image_file and not self.image_link:
            raise ValidationError('Either image file or image link must be provided.')
        elif self.image_file and self.image_link:
            raise ValidationError('Please proivide either image file or image link, not both')

    def __str__(self):
        return f'Legal Docs (last updated: {self.updated_at.strftime("%Y-%m-%d %H:%M")})'

    class Meta:
        verbose_name = 'Legal Dococument'
        verbose_name_plural = 'Legal Documents'

    