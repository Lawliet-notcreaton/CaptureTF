from django.db import models

# Create your models here.
class Ticket(models.Model):

    topic = models.CharField('Тема', max_length=50,)
    message = models.TextField('Cooбщение', max_length=200)

