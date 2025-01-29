from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


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

def formulario(request):
    context={}
    return render(request, 'restaurante/formulario.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})
