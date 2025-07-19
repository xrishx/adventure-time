from django.db import models

class Package(models.Model):
    name= models.CharField(max_length=100, help_text='Package Name')
    package_image = models.ImageField(upload_to='images/packages', null=True, blank=True, help_text='Upload an image file')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + f'(date created: {self.created_at.strftime("%Y-%m-%d %H:%M")})'
    
    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'
