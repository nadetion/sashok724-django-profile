# Generated by Django 2.1.2 on 2019-03-05 04:44

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190305_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skin',
            field=models.ImageField(upload_to=authentication.models.skin_upload_to),
        ),
    ]
