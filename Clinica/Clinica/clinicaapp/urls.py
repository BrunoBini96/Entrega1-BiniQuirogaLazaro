from django.urls import path
from .views import inicio, formularioPaciente, pacientes, turnos, doctores, DoctorCreate, DoctorDetail

urlpatterns = [
    path("",inicio),
    path("formularioPacientes/", formularioPaciente, name = 'PacientesFormulario'),
    path('pacientes/', pacientes , name = "Pacientes"),
    path('doctores/', doctores, name = "Doctores"),
    path('turnos/', turnos, name = "Turnos"),
    path('registrar-doctor/', DoctorCreate.as_view(), name="RegistrarDoctor"),
    path('detalle-doctor/', DoctorDetail.as_view(), name="DetalleDoctor"),
]
