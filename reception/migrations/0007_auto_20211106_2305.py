# Generated by Django 3.2.8 on 2021-11-06 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0006_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='entreprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reception.entreprise'),
        ),
        migrations.AddField(
            model_name='agent',
            name='type_de_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reception.service'),
        ),
        migrations.AddField(
            model_name='personne',
            name='type_de_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reception.service'),
        ),
    ]