# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-20 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recentfiles',
            name='location',
        ),
    ]
