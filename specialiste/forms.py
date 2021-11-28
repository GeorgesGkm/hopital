from django import forms
from specialiste.models import Specialiste


class SpecialisteForm(forms.ModelForm):
    class Meta:
        model = Specialiste
        fields = '__all__'