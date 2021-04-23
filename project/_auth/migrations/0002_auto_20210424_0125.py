# Generated by Django 3.1.7 on 2021-04-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='mainuser',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='mainuser',
            name='role',
            field=models.SmallIntegerField(choices=[(3, 'admin'), (1, 'customer'), (2, 'manager')], default=1),
        ),
    ]