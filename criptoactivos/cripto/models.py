from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genero(models.Model):
 id_genero = models.AutoField(db_column='idGenero', primary_key=True) 
 genero = models.CharField(max_length=20, blank=False, null=False)

 def __str__(self):
    return str(self.genero)


class Alumno(models.Model):
 rut = models.CharField(primary_key=True, max_length=10)
 nombre = models.CharField(max_length=20)
 apellido_paterno = models.CharField(max_length=20)
 apellido_materno = models.CharField(max_length=20)
 fecha_nacimiento = models.DateField(blank=False, null=False) 
 id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero') 
 telefono = models.CharField(max_length=45)
 email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
 direccion = models.CharField(max_length=50, blank=True, null=True) 
 activo = models.IntegerField()
 def __str__(self):
    return str(self.nombre)+" "+str(self.apellido_paterno) 
 

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Compra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Aquí asumimos que el ID del usuario administrador es 1
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    run = models.CharField(max_length=12)
    cryptocurrency = models.CharField(max_length=10)
    local_currency_amount = models.DecimalField(max_digits=10, decimal_places=2)
    crypto_amount = models.DecimalField(max_digits=10, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.cryptocurrency}"