# Generated by Django 4.1.2 on 2023-11-14 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginregister', '0008_profile_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_verified',
        ),
    ]
