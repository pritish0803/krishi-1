# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 15:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
        ('crop_warehouse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='enter', max_length=500)),
                ('pin', models.IntegerField(default=10)),
                ('aadhar', models.IntegerField(default=11)),
                ('crops', models.ManyToManyField(null=True, to='crop_warehouse.Crop')),
                ('markets', models.ManyToManyField(null=True, to='market.Market')),
                ('transportation', models.ManyToManyField(null=True, to='transport.Transportation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('warehouses', models.ManyToManyField(null=True, to='crop_warehouse.Warehouse')),
            ],
        ),
    ]
