# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-05 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20180205_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinprices',
            name='five_day_predictions',
            field=models.FloatField(max_length=10),
        ),
    ]
