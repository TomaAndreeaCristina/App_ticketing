from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from authentication.models import CustomUser


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'departament']

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)