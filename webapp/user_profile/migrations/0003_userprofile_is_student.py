# Generated by Django 2.1.7 on 2019-03-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20190323_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
