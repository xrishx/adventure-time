from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import random

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

    def create_admin(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        return self.create_user(email, password, **extra_fields)    

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager() # type: ignore

class OTP(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(random.randint(10000, 99999))
        super().save(*args, **kwargs)