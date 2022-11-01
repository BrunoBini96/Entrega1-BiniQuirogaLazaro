from django.db import models
from unittest.util import _MAX_LENGTH
class Turnos(models.Model):
    doctor = models.CharField(max_length=20)
    paciente = models.CharField(max_length=20)
    horario = models.TimeField
    fecha = models.DateField
    consultorio = models.CharField

class Doctores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    especialidad = models.IntegerField
    consultorio = models.IntegerField

class Pacientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=20)
    turno = models.BooleanField
    obra_social = models.IntegerField
    