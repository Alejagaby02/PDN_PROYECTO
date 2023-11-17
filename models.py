from django.db import models

# Create your models here.
class Auto(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return f' Auto{self.modelo} {self.marca} {self.color} {self.año}'
