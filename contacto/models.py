from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=70)
    telefono=models.CharField(max_length=8)
    email=models.EmailField()

    class Mate:
        verbose_name='Contacto'

    def __str__(self):
     return self.nombre
