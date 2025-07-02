from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='Blog Title')
    reading_time = models.CharField(max_length=20, help_text='Reading Time')
    description = models.TextField(max_length=1000, help_text='Blog Description')
    image_file = models.ImageField(upload_to='images/blogs', null=True, blank=True, help_text='Upload an image file')
    popular = models.BooleanField(default=False, help_text='Mark as popular?')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Published at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    def __str__(self):
        return self.title + f' (published date: {self.created_at.strftime("%Y-%m-%d %H:%M")})'
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
