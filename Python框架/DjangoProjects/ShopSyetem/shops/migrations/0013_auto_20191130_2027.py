# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-30 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0012_shopcar_gnumber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='ShopCar',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
