# Generated by Django 2.2.6 on 2020-01-30 11:56

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=pyuploadcare.dj.models.ImageField(null=True),
        ),
    ]
