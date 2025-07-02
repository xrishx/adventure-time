from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, help_text= 'Team member name')
    position = models.CharField(max_length=100, help_text= 'Team member position')
    description = models.TextField(max_length=1000, help_text= 'Team member description')
    image = models.ImageField(upload_to='images/team', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'