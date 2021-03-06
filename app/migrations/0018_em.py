# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_instrument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Em',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=3)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'EM',
                'verbose_name_plural': 'EMs',
            },
        ),
    ]
