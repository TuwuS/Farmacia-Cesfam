from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medicamento(models.Model):
    codigo = models.AutoField(primary_key=True)	
    descripcion	= models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    contenido = models.PositiveSmallIntegerField()
    gramaje	= models.PositiveSmallIntegerField()
    precio = models.PositiveSmallIntegerField()
    cantidad = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0}"
        return texto.format(self.descripcion)

class Medico(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)

class Empleado(models.Model):
    CARGOS = (
        ('M', 'Médico'),
        ('A', 'Administrador'),
        ('F', 'Farmaceutico'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=20,choices=CARGOS)
    def get_cargo(id):
        try:
            h =User.objects.get(pk=id)
            cargo = h.empleado.cargo
            return  cargo
        except Empleado.DoesNotExist:
            return None

    def __str__(self):
        texto = "{0}, Cargo: {1}"
        return texto.format(self.user, self.cargo)

class Prescripcion(models.Model):
    prescripcion_id = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.CharField(max_length=40)
    correo = models.EmailField()
    telefono = models.PositiveSmallIntegerField()
    fecha_entrega = models.DateField()
    fecha_expira = models.DateField()
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    comprimidos = models.PositiveSmallIntegerField(default=0)
    frecuencia_hrs = models.PositiveSmallIntegerField(default=0)
    dias_tratamiento = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        texto = "Medico: {0}, Paciente: {1}, Receta: {2}"
        return texto.format(self.medico.nombre, self.paciente, self.medicamento.descripcion)
