# Generated by Django 4.1.2 on 2023-11-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField(default='123 123 1234')),
                ('country', models.CharField(default='Country', max_length=100)),
            ],
        ),
    ]
