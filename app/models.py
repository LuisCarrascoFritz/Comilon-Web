from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, rut, nombre, telefono, email, password=None, **extra_fields):
        if not rut:
            raise ValueError('El RUT es obligatorio.')
        if not email:
            raise ValueError('El correo electrónico es obligatorio.')

        email = self.normalize_email(email)
        user = self.model(rut=rut, nombre=nombre, telefono=telefono, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, nombre, telefono, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(rut, nombre, telefono, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT", help_text="Ingrese el RUT sin puntos y con guión (ej: 12345678-9).")
    nombre = models.CharField(max_length=150, verbose_name="Nombre Completo")
    telefono = models.CharField(max_length=15, verbose_name="Número de Teléfono")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['nombre', 'telefono', 'email']

    def __str__(self):
        return f"{self.nombre} ({self.rut})"
