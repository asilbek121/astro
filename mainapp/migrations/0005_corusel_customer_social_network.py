# Generated by Django 3.2.4 on 2021-07-07 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0004_auto_20210707_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1024, verbose_name='Tavsifi')),
                ('img', models.ImageField(upload_to='about/corusel')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Customer')),
                ('comment', models.CharField(max_length=255, verbose_name='Comment')),
                ('img', models.ImageField(upload_to='costumer')),
            ],
        ),
        migrations.CreateModel(
            name='Social_Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(blank=True, max_length=100, verbose_name='Telegram')),
                ('instagram', models.CharField(blank=True, max_length=100, verbose_name='Instagram')),
                ('twitter', models.CharField(blank=True, max_length=100, verbose_name='Twitter')),
                ('facebook', models.CharField(blank=True, max_length=100, verbose_name='Facebook')),
                ('site', models.CharField(blank=True, max_length=100, verbose_name='Offial site')),
                ('telephone', models.CharField(max_length=20, verbose_name='Telephone')),
            ],
        ),
    ]
