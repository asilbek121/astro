from django.db import models



class Course(models.Model):
    group_option = [
        ('групповой', 'групповой'),
        ('индивидуальный', 'индивидуальный'),
        ('мини группа', 'мини группа')
    ]

    name = models.CharField(max_length=255, verbose_name='Yunalishi')
    muddati = models.IntegerField(verbose_name='Davomiyligi', help_text='oy')
    dars_soni = models.IntegerField(verbose_name='Darslar soni', help_text='haftasiga')
    group = models.CharField("Guruh shakli", max_length=255, choices=group_option)
    price = models.IntegerField(verbose_name='Narxi(oy)')

    img = models.ImageField(upload_to='course', blank=True)
    description = models.TextField(verbose_name='Tavsifi')



def __str__(self):
    return self.name

class Student(models.Model):
    last_name = models.CharField(max_length=50, verbose_name="Last name")
    first_name = models.CharField(max_length=50, verbose_name="First name")
    age = models.IntegerField(verbose_name='Age')
    phone = models.CharField(max_length=50, verbose_name='Phone number')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')

    def __str__(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.course)


class kurs_detail(models.Model):
    Kurs_tavsifi = models.CharField(max_length=1000, blank=True)
    kimdan = models.CharField(max_length=1000, blank=True)
    qatnashuvchilar_soni = models.CharField(max_length=100, blank=True)
    yozilish_qoydalari = models.TextField(blank=True)

