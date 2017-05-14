# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20170509_1408'),
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
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=3)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Instrument',
                'verbose_name_plural': 'Instruments',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=3)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.RemoveField(
            model_name='dataentry',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='dataentry',
            name='text',
        ),
        migrations.AlterField(
            model_name='dataentry',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 14, 15, 46, 22, 496017, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dataentry',
            name='instrument',
            field=models.ForeignKey(blank=True, null=True, to='app.Instrument'),
        ),
        migrations.AlterField(
            model_name='dataentry',
            name='observatory',
            field=models.ForeignKey(blank=True, null=True, to='app.Observatory'),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='em',
            field=models.ForeignKey(blank=True, null=True, to='app.Em'),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='type',
            field=models.ForeignKey(blank=True, null=True, to='app.Type'),
        ),
    ]
