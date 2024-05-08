from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)
    nume = models.CharField(max_length=40, unique=True)
    prenume = models.CharField(max_length=40, unique=True)
    departament = models.CharField(max_length=20, null=False, blank=False)
    # username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    numar_telefon = models.IntegerField(null=True)
    # cui_societate = models.TextField(null=False, blank=False)

    # def approve_user(self):
    #     self.is_approved = True
    #     self.save()
    #
    #     # Trimiteți o notificare către superadmin
    #     subject = 'Cerere de aprobare cont utilizator nou'
    #     message = f'Utilizatorul {self.username} solicită aprobarea contului. \
    #         Aprobați utilizatorul aici: {reverse("approve_user", args=[self.id])}'
    #     send_mail(subject, message, 'purcareaalex91@yahoo.com', ['purcareaalex91@yahoo.com'])


class Companie(models.Model):
    is_superadmin = models.BooleanField(default=True)
    nume_companie = models.CharField(max_length=100, null=False, blank=False)
    nume_admin_cont = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    numar_telefon = models.IntegerField(null=True)
    cui_societate = models.CharField(max_length=10, null=False, blank=False)
    departament = models.CharField(max_length=20, null=False, blank=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)


# class ProfilUser(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user')
#     companie = models.ForeignKey(Companie, on_delete=models.CASCADE, related_name='company')
#     is_superadmin = models.BooleanField(default=False)
#     nume_user = models.CharField(max_length=20, null=False, blank=False)
#     prenume_user = models.CharField(max_length=20, null=False, blank=False)
#     departament = models.CharField(max_length=20, null=False, blank=False)
#     email = models.EmailField(null=False, blank=False)
#     nr_telefon = models.IntegerField(null=False, blank=False)
#     set_password = models.CharField(max_length=50, null=False, blank=False)
