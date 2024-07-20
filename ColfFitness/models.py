from django.db import models
from django.contrib.auth.models import User
import os

# Categorias de Productos: 

# Indumentaria deportiva
class Indumentaria(models.Model):
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='indumentaria/', default='indumentaria/default.jpg')

    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.descripcion}, {self.precio}"

# Maquinas de Musculacion
class Maqmusculacion(models.Model):
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='maqmusculacion/', null=True, blank=True) 
    
    def __str__(self):
        return f"{self.nombre},{self.tipo},{self.descripcion},{self.precio}"

# Maquinas de Cardio
class Maqcardio(models.Model):
    nombre=models.CharField(max_length=80)
    tipo=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    precio=models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='maqcardio/', null=True, blank=True) 
    
def __str__(self):
        return f"{self.nombre},{self.tipo},{self.descripcion},{self.precio}"
    
# Accesorios de gimnasio
class Accesorios(models.Model):
    nombre=models.CharField(max_length=80)
    tipo=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    precio=models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='accesorios/', null=True, blank=True) 

def __str__(self):
        return f"{self.nombre},{self.tipo},{self.descripcion},{self.precio}"

# Clase Avatar  
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', default='avatares/default.png')

    def __str__(self):
        return f"Avatar de {self.user.username}"