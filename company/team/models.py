from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, help_text= 'Team member name')
    position = models.CharField(max_length=100, help_text= 'Team member position')
    description = models.TextField(max_length=1000, help_text= 'Team member description')
    image = models.ImageField(upload_to='images/team', null=True, blank=True, help_text='Upload an image file')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + f'(last updated: {self.updated_at.strftime("%Y-%m-%d %H:%M")})'
    
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'