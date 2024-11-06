from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    publicacion = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='libros')

    def __str__(self) -> str:
        return self.titulo
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    libros = models.ManyToManyField(Libro, related_name='autores')