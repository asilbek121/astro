from django.db import models

class carousel(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    p = models.CharField(max_length=200)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.title1


class man(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=50)
    p = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Social_Network(models.Model):
    telegram = models.CharField(max_length=100, blank=True, verbose_name='Telegram')
    instagram = models.CharField(max_length=100, blank=True, verbose_name='Instagram')
    twitter = models.CharField(max_length=100, blank=True, verbose_name='Twitter')
    facebook = models.CharField(max_length=100, blank=True, verbose_name='Facebook')
    site = models.CharField(max_length=100, blank=True, verbose_name='Offial site')
    telephone = models.CharField(max_length=20, verbose_name='Telephone')


class about(models.Model):
    img1 = models.ImageField(upload_to='img', blank=True)
    text1 = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=100)
    img2 = models.ImageField(upload_to='img', blank=True)
    text2 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title