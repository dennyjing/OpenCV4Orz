# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20160710_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='dilate_ksize',
            field=models.CharField(blank=True, default=(5, 5), max_length=16, null=True),
        ),
    ]
