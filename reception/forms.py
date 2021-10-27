from django import forms

from reception.models import Personne
from reception.models import Entreprises


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ('nom', 'sexe', 'email', 'adresse_physique', 'date_create')



























class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprises
        fields = '__all__'
