# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maryamapp', '0002_auto_20171026_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
