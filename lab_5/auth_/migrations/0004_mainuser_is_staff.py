# Generated by Django 3.1.7 on 2021-03-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0003_remove_mainuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='is_staff'),
        ),
    ]
