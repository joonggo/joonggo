# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20170219_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
