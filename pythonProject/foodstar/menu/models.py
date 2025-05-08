from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')