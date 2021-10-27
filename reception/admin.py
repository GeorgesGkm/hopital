from django.contrib import admin

# Register your models here.
from .models import Entreprises, Personne

admin.site.register(Personne)
admin.site.register(Entreprises)