# Generated by Django 3.2.8 on 2021-11-28 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0008_service_nombre_medecin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='type_de_service',
        ),
    ]