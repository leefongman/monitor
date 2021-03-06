# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min1', models.FloatField()),
                ('min5', models.FloatField()),
                ('min15', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev', models.CharField(max_length=256)),
                ('total', models.IntegerField()),
                ('used', models.IntegerField()),
                ('available', models.IntegerField()),
                ('percent', models.CharField(max_length=10)),
                ('mpoint', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('used', models.IntegerField()),
                ('free', models.IntegerField()),
                ('shared', models.IntegerField()),
                ('buffers', models.IntegerField()),
                ('cached', models.IntegerField()),
            ],
        ),
    ]
