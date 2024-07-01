from django.db import models

# Categorias de Productos: 

# Indumentaria deportiva
class Indumentaria(models.Model):
    nombre=models.CharField(max_length=80)
    tipo=models.CharField(max_length=60)
    descripcion=models.IntegerField()
    precio=models.CharField(max_length=1000)

def __str__(self):
        return f"{self.nombre},{self.tipo},{self.descripcion},{self.precio}"

# Maquinas de Musculacion
class Maqmusculacion(models.Model):
    nombre=models.CharField(max_length=80)
    tipo=models.CharField(max_length=60)
    descripcion=models.IntegerField()
    precio=models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.nombre},{self.tipo},{self.descripcion},{self.precio}"

# Maquinas de Cardio
class Maqcardio(models.Model):
    nombre=models.CharField(max_length=80)
    tipo=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    precio=models.CharField(max_length=1000)
    
def __str__(self):
        return f"{self.nombre},{self.tipo},{self.descripcion},{self.precio}"
    
# Accesorios de gimnasio
class Accesorios(models.Model):
    nombre=models.CharField(max_length=80)
    tipo=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    precio=models.CharField(max_length=1000)

def __str__(self):
        return f"{self.nombre},{self.tipo},{self.descripcion},{self.precio}"