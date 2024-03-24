from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)

