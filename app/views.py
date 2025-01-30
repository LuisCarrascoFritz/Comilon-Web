from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
# Función para verificar si el usuario es admin
def es_admin(user):
    return user.is_superuser

# Vistas generales
def index(request):
    return render(request, 'restaurante/index.html')

def reserva(request):
    return render(request, 'restaurante/reserva.html')

def platillos(request):
    return render(request, 'restaurante/platillos.html')

def platillo(request):
    return render(request, 'restaurante/platillo.html')

def soporte(request):
    return render(request, 'restaurante/soporte.html')

def inicioSesion(request):
    return render(request, 'restaurante/inicioSesion.html')

def registro(request):
    return render(request, 'restaurante/registro.html')

def es_admin(user):
    return user.is_superuser

def subirProducto(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:  # Si es admin, lo redirige
                login(request, user)
                return redirect(reverse("admin_dashboard")) # Redirige a la vista protegida
            else:
                messages.error(request, "No tienes permisos de administrador.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "restaurante/index.html")  # Si falla, vuelve a login

# Vista protegida del admin
@login_required
@user_passes_test(es_admin)
def admin_dashboard(request):
    return render(request, "restaurante/subirProducto.html")
