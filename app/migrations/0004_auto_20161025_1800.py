# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-25 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161008_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoria',
            new_name='category',
        ),
    ]
