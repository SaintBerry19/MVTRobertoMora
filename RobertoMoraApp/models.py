from django.db import models


class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    empresa=models.CharField(max_length=30)

class Proveedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    empresa=models.CharField(max_length=30)

class Material(models.Model):
    nombre= models.CharField(max_length=30)
    cantidad= models.IntegerField()
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()
    facturado = models.BooleanField()

class Factura(models.Model):
    numero=models.IntegerField()
    fechafactura= models.DateField()
    total=models.IntegerField()