# Generated by Django 3.1.7 on 2021-05-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0009_auto_20210511_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='role',
            field=models.SmallIntegerField(choices=[(2, 'manager'), (3, 'admin'), (1, 'customer')], default=1),
        ),
    ]