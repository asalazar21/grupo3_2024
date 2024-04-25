from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Proyecto, Tarea, Empleado, Cliente, EstadoTarea, Prioridad, Responsable
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from .forms import EmpleadoForm, ProyectoForm, TareaForm, ClienteForm, PrioridadForm, ResponsableForm, EstadoTareaForm

# Create your views here.


class IndexListView(ListView):
    def get(self, request, *args, **kwargs):
        proyectos = Proyecto.objects.all()[:5]
        tareas = Tarea.objects.all()[:5]
        empleados = Empleado.objects.all()[:5]
        clientes = Cliente.objects.all()[:5]
        context = {'lista_proyectos': proyectos, 'lista_tareas': tareas, 'lista_empleados': empleados, 'lista_clientes': clientes}
        return render(request,'index.html', context)        
        

#LISTA DE TODOS LOS DATOS DE LAS 5 PRIMERAS TAREAS
class TareaListView(ListView):
    model = Tarea
    template_name = 'index_tareas.html'  
    context_object_name = 'lista_tareas'
    # queryset = Proyecto.objects.order_by('nombre')  #¿poner aqui?
    paginate_by = 10


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html' 


class TareaDeleteView(DeleteView):
    model = Tarea
    success_url = reverse_lazy('index_tareas') 
    

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('index_tareas')    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TareaUpdateView(UpdateView):
    model = Tarea
    template_name = 'appGestionMantenimientoEquipos/tarea_edit.html'
    success_url = reverse_lazy('index_tareas')
    fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'responsable', 'nivel_prioridad', 'estado_tarea']


# ------------------


class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'index_proyectos.html'  
    context_object_name = 'lista_proyectos' 
    paginate_by = 10
    # queryset = Proyecto.objects.order_by('nombre')  #¿poner aqui?



class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html' 


class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('index_proyectos') 


class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('index_proyectos')    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    template_name = 'appGestionMantenimientoEquipos/proyecto_edit.html'
    success_url = reverse_lazy('index_proyectos')
    fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'presupuesto', 'cliente', 'tarea_a_realizar', 'responsable']

# ------------------

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'index_empleados.html'  
    context_object_name = 'lista_empleados'
    paginate_by = 10
    # queryset = Proyecto.objects.order_by('dni')  #¿poner aqui? o 'dni'?


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html' 


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('index_empleados') 
    
    
class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('index_empleados')    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'appGestionMantenimientoEquipos/empleado_edit.html'
    success_url = reverse_lazy('index_empleados')
    fields = ['dni', 'nombre', 'apellidos', 'email', 'telefono']

# ------------------


class ClienteListView(ListView):
    model = Cliente
    template_name = 'index_proveedores.html'
    queryset = Cliente.objects.order_by('nombre')
    context_object_name = 'lista_clientes'
    paginate_by = 10

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente.html'

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('index_clientes')

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('index_clientes') 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'appGestionMantenimientoEquipos/cliente_edit.html'
    success_url = reverse_lazy('index_clientes')
    fields = ['nombre','telefono','direccion',]
