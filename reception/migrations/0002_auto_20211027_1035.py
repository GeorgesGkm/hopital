# Generated by Django 3.2.8 on 2021-10-27 10:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entreprises',
            old_name='date_debut',
            new_name='date_debuts',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='date_debut',
        ),
        migrations.AddField(
            model_name='personne',
            name='date_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
