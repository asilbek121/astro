# Generated by Django 3.2.4 on 2021-07-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Yunalishi')),
                ('muddati', models.IntegerField(help_text='oy', verbose_name='Davomiyligi')),
                ('dars_soni', models.IntegerField(help_text='haftasiga', verbose_name='Darslar soni')),
                ('group', models.CharField(choices=[('групповой', 'групповой'), ('индивидуальный', 'индивидуальный'), ('мини группа', 'мини группа')], max_length=255, verbose_name='Guruh shakli')),
                ('price', models.IntegerField(verbose_name='Narxi(oy)')),
                ('img', models.ImageField(blank=True, upload_to='course')),
                ('description', models.TextField(verbose_name='Tavsifi')),
            ],
        ),
        migrations.DeleteModel(
            name='kurs',
        ),
    ]
