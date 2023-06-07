from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    image = models.ImageField(verbose_name='Картинка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Услуги' # множест 
        verbose_name = "Услуги" 

class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    comment = models.TextField(verbose_name='Комментарии')
    image =models.ImageField(verbose_name='Фотография')
    work = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Отзывы' # множест 
        verbose_name = "Отзывы" 