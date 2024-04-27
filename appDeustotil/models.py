from django.db import models

#Clase Cliente referencia al campo cliente de la clase Proyecto
class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


#Clase Prioridad referencia al campo prioridad de la clase Tarea
class Prioridad (models.Model):
    prioridad = models.CharField(max_length=5,unique=True)

    def __str__(self):
        return self.prioridad
    

#Clase EstadoTarea referencia al campo estado_tarea de la clase Tarea
class EstadoTarea (models.Model):
    estado = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.estado


#Clase Empleado
class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=15)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre + " " + self.apellidos
    
#Clase Tarea
class Tarea(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)    #1-N MIRAR SI ES ASI!!!!!!!!
    nivel_prioridad =  models.ForeignKey(Prioridad, on_delete=models.CASCADE) #1-N MIRAR SI ES ASI!!!!!!!!
    estado_tarea =   models.ForeignKey(EstadoTarea, on_delete=models.CASCADE)   #1-N MIRAR SI ES ASI!!!!!!!!
    notas = models.CharField(max_length=500)
    
    def __str__(self):
        return self.nombre


#Clase Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarea_a_realizar = models.ManyToManyField(Tarea)   #N-M MIRAR SI ES ASI!!!!!!!!
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE) #1-N MIRAR SI ES ASI!!!!!!!!
    
    def __str__(self):
        return self.nombre