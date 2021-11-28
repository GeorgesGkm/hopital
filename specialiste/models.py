from django.db import models
from django.utils import timezone

# Create your models here.
from medecin.models import Medecin
from reception.models import Personne


class Specialiste(models.Model):
    personne = models.ForeignKey(Personne, null=True, on_delete=models.SET_NULL)
    dossier = models.ForeignKey(Medecin, null=True, on_delete=models.SET_NULL)
    description2= models.TextField(max_length=200, null=True)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        template = '{0.dossier}'
        return template.format(self)