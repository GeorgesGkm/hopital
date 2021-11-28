from django import forms
from medecin.models import Medecin


class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = '__all__'
