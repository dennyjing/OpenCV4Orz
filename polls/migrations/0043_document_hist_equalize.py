# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0042_auto_20160715_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='hist_equalize',
            field=models.BooleanField(default=False),
        ),
    ]
