# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 20:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_remove_artist_pageid'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 17, 20, 26, 36, 867624, tzinfo=utc), verbose_name='date added'),
        ),
    ]
