# Generated by Django 3.2.8 on 2021-11-24 23:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reception', '0008_service_nombre_medecin'),
        ('medecin', '0002_rename_dossier_medecin_personne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description2', models.TextField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('dossier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medecin.medecin')),
                ('personne', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reception.personne')),
            ],
        ),
    ]