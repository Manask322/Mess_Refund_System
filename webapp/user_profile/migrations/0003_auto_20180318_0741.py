# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20180318_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Write about your self'),
        ),
    ]
