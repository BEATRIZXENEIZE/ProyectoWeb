from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    dni = models.CharField(max_length=20, unique=True, verbose_name="DNI")
    domicilio = models.CharField(max_length=200, verbose_name="Domicilio")
    legajo = models.CharField(max_length=30, verbose_name="Legajo")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad / Materia")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.especialidad} (Legajo: {self.legajo})"
