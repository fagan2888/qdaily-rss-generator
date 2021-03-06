# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 11:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('crawled', models.DateTimeField()),
            ],
        ),
    ]
