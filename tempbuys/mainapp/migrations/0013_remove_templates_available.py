# Generated by Django 4.1.2 on 2023-11-06 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_templates_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templates',
            name='available',
        ),
    ]