# Generated by Django 3.2.4 on 2021-07-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_kurs'),
    ]

    operations = [
        migrations.CreateModel(
            name='man',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=50)),
                ('p', models.CharField(max_length=100)),
            ],
        ),
    ]