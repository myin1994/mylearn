# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-26 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authordetail',
            name='sex',
            field=models.CharField(default='男', max_length=10),
        ),
    ]
