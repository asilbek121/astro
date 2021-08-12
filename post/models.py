from django.db import models

class post2(models.Model):
    img = models.ImageField(upload_to="img")
    data = models.DateTimeField('vaqti')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.title