# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170218_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
