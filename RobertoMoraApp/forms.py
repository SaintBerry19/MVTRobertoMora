from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    numeropedido= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    cantidad= forms.IntegerField()
    fechaDeEntrega = forms.DateField()  
    entregado = forms.BooleanField()
    facturado = forms.BooleanField()

class FacturaFormulario(forms.Form):
    numero=forms.IntegerField()
    fechafactura= forms.DateField()
    total=forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Contraseña*', widget=forms.PasswordInput)
    last_name=forms.CharField(label= 'Apellido')
    first_name=forms.CharField(label= 'Nombre')
    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2','last_name','first_name']
            help_texts= {k:"" for k in fields}
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Contraseña*', widget=forms.PasswordInput)
    last_name=forms.CharField(label= 'Apellido')
    first_name=forms.CharField(label= 'Nombre')
    class Meta:
            model = User
            fields = [ 'email', 'password1', 'password2','last_name','first_name']
            help_texts= {k:"" for k in fields}
    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user