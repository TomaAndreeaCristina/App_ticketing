from django.forms import ModelForm
from servicii.models import ServiciiModel
from user.models import UserModel


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'