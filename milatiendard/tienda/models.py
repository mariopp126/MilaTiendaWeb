from django.db import models

# Create your models here.

# tienda/models.py

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')

class Opiniones(models.Model):
    autor = models.CharField(max_length=100)
    comentario = models.TextField()
    rating = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
