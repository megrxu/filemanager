# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disk', '0014_disk_disk_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='disk_mounted',
            field=models.IntegerField(default=0),
        ),
    ]
