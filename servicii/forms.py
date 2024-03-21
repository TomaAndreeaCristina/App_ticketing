from django.forms import ModelForm
from servicii.models import ServiciiModel

class ServiciiForm(ModelForm):
    class Meta:
        model = ServiciiModel
        fields = '__all__'