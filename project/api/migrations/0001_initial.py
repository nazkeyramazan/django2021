# Generated by Django 3.1.7 on 2021-04-18 08:35

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Surname')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='No data', max_length=10000)),
                ('price', models.IntegerField(default='No data', verbose_name='Book price')),
                ('author', models.ManyToManyField(to='api.Author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='No description, add description', verbose_name='Book category description')),
            ],
            options={
                'verbose_name': 'Book category',
                'verbose_name_plural': 'Book categories',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Main category',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='Publisher country')),
                ('country', models.CharField(max_length=255, verbose_name='Publisher country')),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.book')),
                ('num_pages', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Book detail',
                'verbose_name_plural': 'Books details',
            },
            bases=('api.book',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bookcategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.maincategory', verbose_name='Book name'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.publisher', verbose_name='Publsiher'),
        ),
    ]