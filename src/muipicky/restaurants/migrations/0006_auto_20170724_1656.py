# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurantlocation_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]