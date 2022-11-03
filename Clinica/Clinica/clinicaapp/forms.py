from django import forms

class TurnoFormulario(forms.Form):
    doctor = forms.CharField()
    paciente = forms.CharField()
    horario = forms.TimeField()
    fecha = forms.DateField()
    consultorio = forms.CharField()

class DoctorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.CharField()
    especialidad = forms.IntegerField()
    consultorio = forms.IntegerField()

class PacienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.CharField()
    telefono = forms.CharField()
    turno = forms.BooleanField()
    obra_social = forms.IntegerField()