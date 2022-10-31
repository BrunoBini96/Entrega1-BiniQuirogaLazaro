from django.db import models

class Turnos(models.Model):
    doctor = models.CharField(MAX_LENGTH = 20)
    paciente = models.CharField(MAX_LENGTH = 8)
    horario = models.TimeField
    fecha = models.DateField
    consultorio = models.CharField

class Doctores(models.Model):
    nombre = models.CharField(MAX_LENGTH = 20)
    apellido = models.CharField(MAX_LENGTH = 20)
    dni = models.CharField(MAX_LENGTH = 8)
    especialidad = models.IntegerField
    consultorio = models.IntegerField

class Pacientes():
    nombre = models.CharField(MAX_LENGTH = 20)
    apellido = models.CharField(MAX_LENGTH = 20)
    dni = models.CharField(MAX_LENGTH = 8)
    telefono = models.CharField(MAX_LENGTH = 20)
    turno = models.BooleanField
    obra_social = models.IntegerField