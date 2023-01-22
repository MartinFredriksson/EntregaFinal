from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} "

class imagenes(models.Model):
    imagen = models.ImageField(upload_to = "image")
    User = models.ForeignKey(User, on_delete=models.CASCADE)

class mensajes(models.Model):
    emisor = User
    receptor = User
    texto = models.CharField(max_length=2000)
    leido = models.BooleanField()
