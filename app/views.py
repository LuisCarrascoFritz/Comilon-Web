from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context={}
    return render(request, 'restaurante/index.html', context)

def reserva(request):
    context={}
    return render(request, 'restaurante/reserva.html', context)

def platillos(request):
    context={}
    return render(request, 'restaurante/platillos.html', context)

def platillo(request):
    context={}
    return render(request, 'restaurante/platillo.html', context)

def soporte(request):
    context={}
    return render(request, 'restaurante/soporte.html', context)

def inicioSesion(request):
    context={}
    return render(request, 'restaurante/inicioSesion.html', context)

def registro(request):
    context={}
    return render(request, 'restaurante/registro.html', context)

def subirProducto(request):
    context={}
    return render(request, 'restaurante/subirProducto.html', context)
