# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20161030_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataentry',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='dataentry',
            name='start_time',
        ),
    ]
