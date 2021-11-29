from django import forms

from reception.models import Personne
from reception.models import Agent
from reception.models import Entreprise
from reception.models import Service


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ('nom', 'sexe', 'email', 'adresse_physique', 'date_create')


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'