from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    pass

class Moto(models.Model):
    marca       = models.CharField(max_length=50)
    modelo      = models.CharField(max_length=150)
    cilindraje  = models.PositiveIntegerField()
    foto        = models.ImageField(upload_to='moto')
    color       = models.CharField(max_length=50)
    placa       = models.CharField(max_length=50, unique=True)
 
    def __str__(self):
        return self.marca + " " + self.modelo
 
 
class Usuario(AbstractBaseUser,PermissionsMixin):
    nombre      = models.CharField(max_length= 100)
    apodo       = models.CharField(max_length= 100, unique=True)
    apellido    = models.CharField(max_length= 100)
    email       = models.EmailField(max_length=100, unique=True)
    foto        = models.ImageField(upload_to='perfil', null=True, blank=True)
    cedula      = models.PositiveIntegerField(null=True, blank=True)
    telefono    = models.IntegerField(null=True, blank=True)
    direccion   = models.CharField(max_length=50, blank=True, null=True)
    ciudad      = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
   # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
    
    def __str__ (self):
        return self.nombre + " "+self.apellido
 
class Historia(models.Model):
    moto        = models.ForeignKey('Moto', on_delete=models.PROTECT)
    usuario     = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    estado =[('vendido', 'Vendido'),('Propietario', 'Propietario'),('Pendiente', 'Pendiente')]
    propiedad   = models.CharField(max_length=11, choices=estado, default='Propietario')
 
class Mantenimiento(models.Model):
    nombre      = models.CharField(max_length=200)
    fecha       = models.DateTimeField()
    observacion = models.CharField(max_length=500)
    moto        = models.ForeignKey('Moto', on_delete=models.CASCADE)
 
    def __str__ (self):
        return self.nombre
