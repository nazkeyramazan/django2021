# Generated by Django 3.1.7 on 2021-05-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0016_auto_20210515_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='role',
            field=models.SmallIntegerField(choices=[(2, 'manager'), (3, 'admin'), (1, 'customer')], default=1),
        ),
    ]
