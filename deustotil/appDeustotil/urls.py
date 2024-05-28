from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
        
    path('', login_required(views.IndexListView.as_view()), name='index'),
    path('correo/', login_required(views.EnviarCorreoView.as_view()), name='correo'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
 
    path('proyectos', login_required(views.ProyectoListView.as_view()), name='index_proyectos'),
    path('proyectos/<int:pk>/', login_required(views.ProyectoDetailView.as_view()), name='detail_proyecto'),
    path('proyectos/<int:pk>/borrar/', login_required(views.ProyectoDeleteView.as_view()), name='delete_proyecto'),
    path('proyectos/<pk>/editar/', login_required(views.ProyectoUpdateView.as_view()), name='edit_proyecto'),
    path('proyectos/crear/', login_required(views.ProyectoCreateView.as_view()), name='create_proyectos'),    

    path('tareas', login_required(views.TareaListView.as_view()), name='index_tareas'),
    path('tareas/<int:pk>/', login_required(views.TareaDetailView.as_view()), name='detail_tarea'),
    path('tareas/<int:pk>/borrar/', login_required(views.TareaDeleteView.as_view()), name='delete_tarea'),
    path('tareas/<pk>/editar/', login_required(views.TareaUpdateView.as_view()), name='edit_tarea'),
    path('tareas/crear/', login_required(views.TareaCreateView.as_view()), name='create_tareas'),
    
    path('empleados', login_required(views.EmpleadoListView.as_view()), name='index_empleados'),
    path('empleados/<int:pk>/', login_required(views.EmpleadoDetailView.as_view()), name='detail_empleado'),
    path('empleados/<int:pk>/borrar/', login_required(views.EmpleadoDeleteView.as_view()), name='delete_empleado'),
    path('empleados/<pk>/editar/', login_required(views.EmpleadoUpdateView.as_view()), name='edit_empleado'),
    path('empleados/crear/', login_required(views.EmpleadoCreateView.as_view()), name='create_empleados'),
    
    path('clientes', login_required(views.ClienteListView.as_view()), name='index_clientes'),
    path('clientes/<int:pk>/', login_required(views.ClienteDetailView.as_view()), name='detail_cliente'),
    path('clientes/<int:pk>/borrar/', login_required(views.ClienteDeleteView.as_view()), name='delete_cliente'),
    path('clientes/<pk>/editar/', login_required(views.ClienteUpdateView.as_view()), name='edit_cliente'),
    path('clientes/crear/', login_required(views.ClienteCreateView.as_view()), name='create_clientes'),
    path('APIclientes', login_required(views.APIClienteListView.as_view()), name='API_index_clientes'),

]