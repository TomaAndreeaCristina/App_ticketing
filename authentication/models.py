from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CustomUser(User):
    departament= models.CharField(max_length=20, null=False, blank=False)