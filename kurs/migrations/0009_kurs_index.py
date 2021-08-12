# Generated by Django 3.2.4 on 2021-07-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurs', '0008_course_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='kurs_index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=255, verbose_name='Yunalishi')),
                ('muddati1', models.IntegerField(help_text='oy', verbose_name='Davomiyligi')),
                ('dars_soni1', models.IntegerField(help_text='haftasiga', verbose_name='Darslar soni')),
                ('group1', models.CharField(choices=[('групповой', 'групповой'), ('индивидуальный', 'индивидуальный'), ('мини группа', 'мини группа')], max_length=255, verbose_name='Guruh shakli')),
                ('price1', models.IntegerField(verbose_name='Narxi(oy)')),
                ('img1', models.ImageField(blank=True, upload_to='course')),
                ('description1', models.TextField(verbose_name='Tavsifi')),
            ],
        ),
    ]
