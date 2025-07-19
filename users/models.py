from django.db import models
from django.utils import timezone
import random

class PasswordResetOTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=10)

    def save(self, *args, **kwargs):
        if not self.otp:
            self.otp = str(random.randint(10000, 99999))
        super().save(*args, **kwargs)