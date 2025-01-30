from django.urls import path
from . import views
from .views import admin_dashboard  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('reserva', views.reserva, name='reserva'),
    path('platillos', views.platillos, name='platillos'),
    path('platillo', views.platillo, name='platillo1'),
    path('soporte', views.soporte, name='soporte'),
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),
    path('registro', views.registro, name='registro'),
    path('subirProducto', views.subirProducto, name='subirProducto'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),  
]

if settings.DEBUG:  # Solo para desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
