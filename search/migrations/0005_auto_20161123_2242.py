# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_artist_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='profession',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
    ]
