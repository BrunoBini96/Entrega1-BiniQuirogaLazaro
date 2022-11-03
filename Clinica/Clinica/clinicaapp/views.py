from .forms import PacienteFormulario
from django.shortcuts import render
from .models import Pacientes, Doctores, Turnos

def inicio(request):
    
    return render(request,"inicio.html")

def pacientes(request):
    return render(request,'pacientes.html')

def doctores(request):
    return render(request,'doctores.html')

def turnos(request):
    return render(request, 'turnos.html')



def formularioPaciente (request):
    if request.method == 'POST':
        
        mi_formulario = PacienteFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            paciente = Pacientes(nombre=data['nombre'], apellido=data['apellido'], dni = data['dni'], telefono = data['telefono'], turno = data['turno'], obra_social = data['obra_social'])
            paciente.save()
    else:
        mi_formulario = PacienteFormulario()
    return render (request,'pacienteFormulario.html', {'mi_formulario': mi_formulario})  

  