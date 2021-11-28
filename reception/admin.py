from django.contrib import admin

# Register your models here.
from .models import Agent, Personne, Entreprise, Service

admin.site.register(Personne)
admin.site.register(Agent)
admin.site.register(Entreprise)
admin.site.register(Service)