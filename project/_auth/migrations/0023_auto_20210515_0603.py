# Generated by Django 3.1.7 on 2021-05-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0022_auto_20210515_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='role',
            field=models.SmallIntegerField(choices=[(3, 'admin'), (2, 'manager'), (1, 'customer')], default=1),
        ),
    ]
