from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class HomepageVideo(models.Model):
    video_file = models.FileField(null = True, blank=True, upload_to='video/homepage_videos', help_text='Upload a video file')
    video_link = models.URLField(null=True, blank=True, max_length=500, help_text='Video Link')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Position(models.TextChoices):
        HERO = 'hero', 'Hero'
        MIDDLE = 'middle', 'Middle'

    position = models.CharField(max_length=20, choices=Position.choices, unique=True, help_text='Video Position')

    def clean(self):
        if not self.video_file and not self.video_link:
            raise ValidationError('Either video file or video link must be provided.')
        elif self.video_file and self.video_link:
            raise ValidationError('Please proivide either video file or video link, not both')

    def __str__(self):
        return f"Homepage Video - {self.position}"
    
    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"