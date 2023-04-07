from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserAccountManager

# Create your models here.
class UserAccount(AbstractUser):
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'password']
    objects = UserAccountManager()
    
    
    def __str__(self):
        return self.email
# Create your models here.
