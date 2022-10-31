from django.shortcuts import render

class Turnos():
    
    def __init__(self, doctor, dni_paciente, horario, fecha, consultorio):
        self.__doctor = doctor
        self.__paciente = dni_paciente
        self.__horario = horario
        self.__fecha = fecha
        self.__consultorio = consultorio

    def corroborar_turno(self, dni):
        if (self.__turno == False and dni == self.__paciente):
            self.__turno = True
            return True
        else:
            return False

    def __str__(self):
            return f'Fecha: {self.fecha} \nHora: {self.horario} \nDr/Dra: {self.doctor}'

class Doctores():
    
    def __init__(self, nombre, apellido, dni, especialidad, consultorio):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__especialidad = especialidad
        self._consultorio = consultorio

    def __str__(self):
        return f'{self.__nombre} {self.__apellido} \nEspecialidad: {self.__especialidad}'


class Pacientes():
    
    def __init__(self, nombre, apellido, dni, telefono, obra_social):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__telefono = telefono
        self.__turno = None
        self.__obraSocial = obra_social

    def __str__(self):
        return f'{self.__nombre} {self.__apellido}'
        