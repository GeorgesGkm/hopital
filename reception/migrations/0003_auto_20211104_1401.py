# Generated by Django 3.2.8 on 2021-11-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_auto_20211027_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('nom', models.CharField(max_length=200, null=True)),
                ('nom_epouse', models.CharField(max_length=200, null=True)),
                ('nombre_enfant', models.IntegerField(null=True)),
                ('sexe', models.CharField(choices=[('masculin', 'masculin'), ('femmin', 'femmin')], max_length=200, null=True)),
                ('adresse_physique', models.CharField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='entreprises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('nombre_agent', models.IntegerField(null=True)),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='entreprises',
        ),
    ]
