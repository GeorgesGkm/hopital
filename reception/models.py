from django.db import models
from django.utils import timezone
# Create your models here.

# models for Entreprise.
class Entreprise(models.Model):
    entreprise = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    nombre_agent = models.IntegerField(null=True)
    adresse = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        template = '{0.entreprise}','{1.adresse}'
        return template.format(self)

# models for Service.
class Service(models.Model):
    nom_servcie = models.CharField(max_length=200, null=True)
    nombre_medecin = models.IntegerField(null=True)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        template = '{0.nom_servcie}'
        return template.format(self)

# models for Personne or Patient.
class Personne(models.Model):
    type_de_service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    SEXES = (('masculin', 'masculin'),
             ('femmin', 'femmin'))
    nom = models.CharField(max_length=200, null=True)
    sexe = models.CharField(max_length=200, null=True, choices=SEXES)
    email = models.EmailField(max_length=200, null=True)
    adresse_physique = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        template = '{0.nom}'
        return template.format(self)
# models for Agent.
class Agent(models.Model):
    SEXES = (('masculin', 'masculin'),
             ('femmin', 'femmin'))
    type_de_service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    entreprise = models.ForeignKey(Entreprise, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=200, null=True)
    nom = models.CharField(max_length=200, null=True)
    nom_epouse = models.CharField(max_length=200, null=True)
    nombre_enfant = models.IntegerField(null=True)
    sexe = models.CharField(max_length=200, null=True, choices=SEXES)
    adresse_physique = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        template = '{0.nom}'
        return template.format(self)