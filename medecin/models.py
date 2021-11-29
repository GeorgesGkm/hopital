from django.db import models
from django.utils import timezone

# Create your models here.
from reception.models import Personne, Service


class Medecin(models.Model):
    personne = models.ForeignKey(Personne, null=True, on_delete=models.SET_NULL)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=200, null=True)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        template = '{0.personne}'
        return template.format(self)