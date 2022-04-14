from django import forms

class ClienteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)
    empresa=forms.CharField(max_length=30)

class ProveedorFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)
    empresa=forms.CharField(max_length=30)

class MaterialFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    cantidad= forms.IntegerField()
    fechaDeEntrega = forms.DateField()  
    entregado = forms.BooleanField()
    facturado = forms.BooleanField()

class FacturaFormulario(forms.Form):
    numero=forms.IntegerField()
    fechafactura= forms.DateField()
    total=forms.IntegerField()

