from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "other"),
    )
    
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)
    #is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, blank=True, choices= GENDER_CHOICES)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    