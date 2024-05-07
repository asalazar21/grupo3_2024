from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
        
    # path('', views.IndexListView.as_view(), name='index'),
    path('', login_required(views.IndexListView.as_view()), name='index'),
    path('correo/', login_required(views.EnviarCorreoView.as_view()), name='correo'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
 
    path('proyectos', views.ProyectoListView.as_view(), name='index_proyectos'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='detail_proyecto'),
    path('proyectos/<int:pk>/borrar/', views.ProyectoDeleteView.as_view(), name='delete_proyecto'),
    path('proyectos/<pk>/editar/', views.ProyectoUpdateView.as_view(), name='edit_proyecto'),
    path('proyectos/crear/', views.ProyectoCreateView.as_view(), name='create_proyectos'),
        

    path('tareas', views.TareaListView.as_view(), name='index_tareas'),
    path('tareas/<int:pk>/', views.TareaDetailView.as_view(), name='detail_tarea'),
    path('tareas/<int:pk>/borrar/', views.TareaDeleteView.as_view(), name='delete_tarea'),
    path('tareas/<pk>/editar/', views.TareaUpdateView.as_view(), name='edit_tarea'),
    path('tareas/crear/', views.TareaCreateView.as_view(), name='create_tareas'),

    
    path('empleados', views.EmpleadoListView.as_view(), name='index_empleados'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='detail_empleado'),
    path('empleados/<int:pk>/borrar/', views.EmpleadoDeleteView.as_view(), name='delete_empleado'),
    path('empleados/<pk>/editar/', views.EmpleadoUpdateView.as_view(), name='edit_empleado'),
    path('empleados/crear/', views.EmpleadoCreateView.as_view(), name='create_empleados'),
    
    path('clientes', views.ClienteListView.as_view(), name='index_clientes'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='detail_cliente'),
    path('clientes/<int:pk>/borrar/', views.ClienteDeleteView.as_view(), name='delete_cliente'),
    path('clientes/<pk>/editar/', views.ClienteUpdateView.as_view(), name='edit_cliente'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='create_clientes'),
    path('APIclientes/<int:pk>/', login_required(views.APIClienteDetailView.as_view()), name='API_detail_cliente'),
    path('APIclientes', login_required(views.APIClienteListView.as_view()), name='API_index_clientes'),



]