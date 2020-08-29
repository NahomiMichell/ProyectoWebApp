from django.db import models

# Create your models here.

class Adopcion(models.Model):
    nombre=models.CharField(max_length=15)
    descripcion=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to = 'adopcion')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Mate:
        verbose_name='Adopcion'

    def __str__(self):
        return self.nombre
