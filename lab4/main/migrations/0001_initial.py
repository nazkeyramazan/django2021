# Generated by Django 3.1.7 on 2021-03-05 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Список задач')),
            ],
            options={
                'verbose_name': 'Список',
                'verbose_name_plural': 'Список задач ',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=1000, verbose_name='Название')),
                ('created_date', models.DateField(verbose_name='Дата создания')),
                ('due_on', models.DateField(verbose_name='Дата оканчания')),
                ('owner', models.CharField(max_length=255, verbose_name='Владельец')),
                ('mark', models.BooleanField(verbose_name='Статус')),
                ('todos', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Список', to='main.todo_list', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
