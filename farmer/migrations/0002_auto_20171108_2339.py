# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='aadhar',
            field=models.IntegerField(default=111222),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pin',
            field=models.IntegerField(default=0),
        ),
    ]
