from django.db import models
from django.utils import timezone
# Create your models here.

class Personne(models.Model):
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
























class Entreprises(models.Model):
    SEXES = (('masculin', 'masculin'),
             ('femmin', 'femmin'))
    entreprise = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    nom = models.CharField(max_length=200, null=True)
    nom_epouse = models.CharField(max_length=200, null=True)
    nombre_enfant = models.IntegerField(max_length=200, null=True)
    sexe = models.CharField(max_length=200, null=True, choices=SEXES)
    adresse_physique = models.CharField(max_length=200, null=True)
    date_debuts = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        template = '{0.entreprise}'
        return template.format(self)