from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('reserva', views.reserva, name='reserva'),
    path('platillos', views.platillos, name='platillos'),
    path('platillo', views.platillo, name='platillo1'),
    path('soporte', views.soporte, name='soporte'),
    path('inicioSesion', views.soporte, name='inicioSesion'),
    path('formulario', views.soporte, name='formulario'),

    path('register/', register, name='register'),



]