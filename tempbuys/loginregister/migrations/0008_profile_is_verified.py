# Generated by Django 4.1.2 on 2023-11-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginregister', '0007_emailverificationtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
