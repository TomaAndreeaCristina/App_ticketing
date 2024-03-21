from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class ServiciiModel(models.Model):
    categorie_servicii = models.CharField(max_length=50,null=False)
    nume_angajat = models.CharField(max_length=50,null=False)

    def __str__(self):
        return f"{self.categorie_servicii} - {self.nume_angajat}"