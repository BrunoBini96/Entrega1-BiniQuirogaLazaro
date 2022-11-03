from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import Doctores, Pacientes, Turnos

def inicio(request):
    
    return render(request,"inicio.html")

class DoctorList(ListView):

    model = Doctores
    template_name = 'doctores_list.html'
    context_object_name = "doctor"

class DoctorDetail(DetailView):

    model = Doctores
    template_name = 'doctores_detail.html'
    context_object_name = "doctor"

class DoctorCreate(CreateView):

    model = Doctores
    template_name = 'doctores_create.html'
    fields = ["nombre", "apellido", "dni", "consultorio"]
    success_url = ''

class DoctorUpdate(UpdateView):

    model = Doctores
    template_name = 'doctores_update.html'
    fields = ('__all__')
    success_url = ''

class DoctorDelete(DeleteView):

    model = Doctores
    template_name = 'doctores_delete.html'
    success_url = ''