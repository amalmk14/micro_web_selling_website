# Generated by Django 4.1.2 on 2023-11-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_paymentfailed'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='host_name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]