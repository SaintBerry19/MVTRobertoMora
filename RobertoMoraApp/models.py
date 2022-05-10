from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    empresa=models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre}  - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion} - Empresa: {self.empresa}"

class Proveedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    empresa=models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre}  -  Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion} - Empresa: {self.empresa}"

class Material(models.Model):
    numeropedido= models.IntegerField()
    nombre= models.CharField(max_length=30)
    cantidad=models.IntegerField()
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()
    facturado = models.BooleanField()
    def __str__(self):
        return f"Numero Pedido: {self.numeropedido}  -  Nombre: {self.nombre} -  Cantidad: {self.cantidad}  - Fecha De Entrega:   { self.fechaDeEntrega} - Entregado: {self.entregado} - Facturado: {self.facturado}"

class Factura(models.Model):
    numero=models.IntegerField()
    fechafactura= models.DateField() 
    total=models.IntegerField()
    def __str__(self):
        return f"Numero: {self.numero} - Fecha De Factura: {self.fechafactura} - Total: {self.total}"

class Avatar(models.Model):
    #vinculo con el usuario
    user=models.ForeignKey (User, on_delete=models.CASCADE)
    #subcarpeta avatares de media :)
    imagen=models.ImageField(upload_to='avatares', default="imagen7.png", null=True, blank = True)