# Generated by Django 3.2.8 on 2021-11-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_auto_20211104_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('nombre_agent', models.IntegerField(null=True)),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Agents',
            new_name='Agent',
        ),
    ]