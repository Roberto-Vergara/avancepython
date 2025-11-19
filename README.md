from django.contrib.auth.models import AbstractUser
from django.db import models

class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"
    
class HoraMedica(models.Model):
    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuarios_asignados'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
    rut = models.CharField(max_length=20, unique=True)
    rutdef = models.CharField(max_length=20)
    profesional = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True, blank=True)
    cesfam = models.CharField(max_length=100)
    seccioncesfam = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
