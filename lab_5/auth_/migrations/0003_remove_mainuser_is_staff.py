# Generated by Django 3.1.7 on 2021-03-19 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0002_mainuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainuser',
            name='is_staff',
        ),
    ]
