# Generated by Django 3.2.8 on 2021-11-06 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0004_auto_20211106_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='entreprise',
        ),
    ]