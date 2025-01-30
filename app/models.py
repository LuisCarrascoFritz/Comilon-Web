from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect

class Users(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    gmail = models.EmailField(unique=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descipcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    
    def __str__(self):
        return self.nombre

    
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        imagen = request.FILES['imagen']  # Aquí se obtiene el archivo de imagen

        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen
        )
        producto.save()
        return redirect('productos_lista')  # Redirigir a la lista de productos o donde desees
    return render(request, 'crear_producto.html')




