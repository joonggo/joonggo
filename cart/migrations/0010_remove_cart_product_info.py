# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 16:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20170729_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_info',
        ),
    ]
