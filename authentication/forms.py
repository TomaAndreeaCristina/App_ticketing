from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from authentication.models import CustomUser, Companie
from django import forms


class CreateUserForm(UserCreationForm):
    nume_companie = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'nume', 'prenume', 'departament', 'nume_companie', 'numar_telefon']

    def save(self, commit=True):
        user = super().save(commit=False)
        nume_companie = self.cleaned_data.get('nume_companie')

        if commit:
            user.save()
            # Verificăm dacă utilizatorul are deja o companie asociată
            if not user.companie:
                Companie.objects.create(nume_companie=nume_companie, user=user)

        return user
