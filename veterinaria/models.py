from django.db import models

# Create your models here.

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    tipoAnimal = models.CharField(max_length=100)
    fnac = models.DateField()
    sexo = models.CharField(max_length=1)