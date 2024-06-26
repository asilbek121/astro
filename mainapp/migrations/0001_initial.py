# Generated by Django 3.2.4 on 2021-06-25 11:55

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Home_image')),
                ('title', models.CharField(max_length=100, verbose_name='Sarlavha')),
                ('any_text', models.TextField(max_length=255, verbose_name='any_text')),
                ('link', models.CharField(max_length=20, verbose_name='button')),
            ],
        ),
        migrations.CreateModel(
            name='Malumot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
                ('img', models.ImageField(upload_to='post_image', verbose_name='img')),
            ],
        ),
        migrations.CreateModel(
            name='obunachilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='man', verbose_name='img')),
                ('name', models.TextField(max_length=50, verbose_name='ism')),
                ('text', models.TextField(max_length=100, verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='post_image', verbose_name='img')),
                ('data', models.DateTimeField(verbose_name='data')),
                ('date', models.DateField(default=datetime.date.today)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('full_text', models.TextField(verbose_name='full_text')),
            ],
        ),
    ]
