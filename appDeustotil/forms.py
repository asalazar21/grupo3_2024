from django import forms
from django.shortcuts import render
from .models import Proyecto, Tarea, Empleado,Cliente, Prioridad, Responsable, EstadoTarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'comentarios': forms.Textarea(attrs={'cols': 40, 'rows': 10}),  #mirar si ooner comentarios  o no. sino borrar
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        

# IGUAL HAY QUE BORRAR ESTOS ULTIMOS 3(si no vamos a querer usarlos)
# SI AL FINAL NO LO USAMOS(XXX_form.html), BORRARLO DE AQUI
class PrioridadForm(forms.ModelForm):
    class Meta:
        model = Prioridad
        fields = '__all__'

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = '__all__'
        
class EstadoTareaForm(forms.ModelForm):
    class Meta:
        model = EstadoTarea
        fields = '__all__'
    

