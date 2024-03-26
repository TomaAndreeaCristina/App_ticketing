from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)
    departament = models.CharField(max_length=20, null=False, blank=False)
