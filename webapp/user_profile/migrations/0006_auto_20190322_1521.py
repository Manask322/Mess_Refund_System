# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-22 15:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0005_auto_20190322_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messmanager',
            fields=[
                ('mess', models.IntegerField(primary_key=True, serialize=False)),
                ('qrcode', models.TextField(max_length=500)),
                ('is_active', models.BinaryField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Messmanager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='mess',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='block',
            field=models.IntegerField(),
        ),
    ]
