# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 06:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellina', '0002_nlrequest_sub_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='nlrequest',
            name='frequency',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nlrequest',
            name='sub_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 2, 6, 9, 21, 294906)),
        ),
        migrations.AlterField(
            model_name='translation',
            name='num_votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
