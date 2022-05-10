from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from RobertoMoraApp.models import Cliente,Proveedor,Material,Factura, Avatar
from RobertoMoraApp.forms import UserEditForm,UserRegisterForm,ClienteFormulario,ProveedorFormulario,MaterialFormulario,FacturaFormulario, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

# Create your views here.
@login_required
def inicio(request):

      avatares=Avatar.objects.filter(user=request.user.id)
      try:
       return render(request, "RobertoMoraApp/Inicio.html",{"url":avatares[0].imagen.url})
      except IndexError:
        return render(request, "RobertoMoraApp/Inicio.html")    
            

#LOGIN

def login_request(request):
      if request.method == "POST":
            form= AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                  usuario=form.cleaned_data.get('username')
                  contra=form.cleaned_data.get('password')
                  user=authenticate(username=usuario,password=contra)
                  if user is not None:
                        login(request,user)
                        try:
                         avatares=Avatar.objects.filter(user=request.user.id)
                         return render(request,"RobertoMoraApp/Inicio.html",{"mensaje":f"Bienvenido {usuario}","url":avatares[0].imagen.url})
                        except IndexError:
                           return render(request, "RobertoMoraApp/Inicio.html",{"mensaje":f"Bienvenido {usuario}"})
                  else:
                        return render(request,"RobertoMoraApp/Inicio.html",{"mensaje": "Error, datos incorrectos"})
            else:
                  return render(request,"RobertoMoraApp/Inicio.html",{"mensaje":"Error, formulario erroneo"})
      form =AuthenticationForm()
      return render(request,"RobertoMoraApp/login.html",{'form':form})

#REGISTER
def register(request):
      if request.method == "POST":
            #form= UserCreationForm(request.POST)
            form=UserRegisterForm(request.POST)
            if form.is_valid():
                  user=form.save()
                  login(request,user)
                  messages.success(request,"El registro fue un éxito")
                  return render(request,"RobertoMoraApp/Inicio.html", {"mensaje":"Usuario Creado :)"})
            messages.error(request, "No se logró el registro, información invalida")    
      else:
         #form=UserCreationForm()
         form=UserRegisterForm()
      return render(request,"RobertoMoraApp/registro.html",{'form':form})

#EDITARPERFIL
@login_required
def editarPerfil(request):
      #Instancia de login
      usuario=request.user 
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.method == 'POST':
            miFormulario=UserEditForm(request.POST,instance=usuario )
            if miFormulario.is_valid():
                  usuario=miFormulario.save()
                  login(request,usuario)
                  try:
                   return render (request, 'RobertoMoraApp/Inicio.html',{"url":avatares[0].imagen.url})
                  except:
                   return render (request, 'RobertoMoraApp/Inicio.html')
      else:
            #Creo el formulario con los datos que voy a modificar
            miFormulario=UserEditForm(initial={'email':usuario.email})
            try:
                  return render(request, "RobertoMoraApp/editarPerfil.html",{"miFormulario":miFormulario, "usuario":usuario,"url":avatares[0].imagen.url})
            except IndexError:
                  return render(request, "RobertoMoraApp/editarPerfil.html",{"miFormulario":miFormulario, "usuario":usuario})

#DEFINICION; LECTURA Y ESCRITURA DE CLIENTE

@login_required
def leercliente(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      cliente=Cliente.objects.all()
      try: 
       contexto = {"cliente":cliente,"url":avatares[0].imagen.url}
       return render(request, 'RobertoMoraApp/LeerCliente.html',contexto)
      except IndexError:
       contexto = {"cliente":cliente}
      return render(request, 'RobertoMoraApp/LeerCliente.html',contexto)

@login_required
def eliminarcliente(request,cliente_nombre,):
      avatares=Avatar.objects.filter(user=request.user.id)
      cliente=Cliente.objects.get (nombre=cliente_nombre)
      cliente.delete()
      cliente=Cliente.objects.all()
      try: 
       contexto = {"cliente":cliente,"url":avatares[0].imagen.url}
       return render(request, 'RobertoMoraApp/LeerCliente.html',contexto)
      except IndexError:
       contexto = {"cliente":cliente}
      return render(request, 'RobertoMoraApp/LeerCliente.html',contexto)

@login_required
def editarcliente(request,cliente_nombre):
      avatares=Avatar.objects.filter(user=request.user.id)
      cliente=Cliente.objects.get (nombre=cliente_nombre)
      if request.method == 'POST':
            miFormulario= ClienteFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  cliente.nombre=informacion['nombre']
                  cliente.apellido=informacion['apellido']
                  cliente.email=informacion['email']
                  cliente.profesion=informacion['profesion']
                  cliente.empresa=informacion['empresa']
                  cliente.save()
                  try:
                      return render(request,'RobertoMoraApp/Cliente.html',{"url":avatares[0].imagen.url})   
                  except IndexError:
                      return render(request,'RobertoMoraApp/Cliente.html') 
      else:
            miFormulario=ClienteFormulario(initial={'nombre': cliente.nombre,'apellido':cliente.apellido, 'email':cliente.email, 'profesion':cliente.profesion, 'empresa':cliente.empresa})
            try:
                  return render(request, 'RobertoMoraApp/EditarCliente.html',{'miFormulario':miFormulario, 'cliente_nombre':cliente_nombre, "url":avatares[0].imagen.url})
            except IndexError:
                  return render(request, 'RobertoMoraApp/EditarCliente.html',{'miFormulario':miFormulario, 'cliente_nombre':cliente_nombre})

@login_required
def cliente(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.method == 'POST':
            miFormulario= ClienteFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  cliente= Cliente(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'], profesion=informacion['profesion'], empresa=informacion['empresa'])
                  cliente.save()
                  try:
                        return render(request,'RobertoMoraApp/Cliente.html',{"url":avatares[0].imagen.url})
                  except IndexError:
                        return render(request,'RobertoMoraApp/Cliente.html')
      else:
            miFormulario=ClienteFormulario()
            try:  
                  return render (request, 'RobertoMoraApp/Cliente.html', {"miFormulario":miFormulario,"url":avatares[0].imagen.url})
            except:
                  return render (request, 'RobertoMoraApp/Cliente.html', {"miFormulario":miFormulario})

#DEFINICION; LECTURA Y ESCRITURA DE PROVEEDOR

@login_required
def leerproveedor(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      proveedor=Proveedor.objects.all()
      try:
            contexto = {"proveedor":proveedor, "url":avatares[0].imagen.url}
            return render(request, 'RobertoMoraApp/LeerProveedor.html',contexto)
      except IndexError:
            contexto = {"proveedor":proveedor}
            return render(request, 'RobertoMoraApp/LeerProveedor.html',contexto)

@login_required
def eliminarproveedor(request,proveedor_nombre):
      avatares=Avatar.objects.filter(user=request.user.id)
      proveedor=Proveedor.objects.get (nombre=proveedor_nombre)
      proveedor.delete()
      proveedor=Proveedor.objects.all()
      try:
            contexto = {"proveedor":proveedor, "url":avatares[0].imagen.url}
            return render(request, 'RobertoMoraApp/LeerProveedor.html',contexto)
      except IndexError:
            contexto = {"proveedor":proveedor}
            return render(request, 'RobertoMoraApp/LeerProveedor.html',contexto)

@login_required
def editarproveedor(request,proveedor_nombre):
      avatares=Avatar.objects.filter(user=request.user.id) 
      proveedor=Proveedor.objects.get (nombre=proveedor_nombre)
      if request.method == 'POST':
            miFormulario= ProveedorFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  proveedor.nombre=informacion['nombre']
                  proveedor.apellido=informacion['apellido']
                  proveedor.email=informacion['email']
                  proveedor.profesion=informacion['profesion']
                  proveedor.empresa=informacion['empresa']
                  proveedor.save()
                  try:
                        return render(request,'RobertoMoraApp/Proveedor.html',{"url":avatares[0].imagen.url})     
                  except IndexError:
                        return render(request,'RobertoMoraApp/Proveedor.html')  
      else:
            miFormulario=ProveedorFormulario(initial={'nombre': proveedor.nombre,'apellido':proveedor.apellido, 'email':proveedor.email, 'profesion':proveedor.profesion, 'empresa':proveedor.empresa})
            try:
                  return render(request, 'RobertoMoraApp/EditarProveedor.html',{'miFormulario':miFormulario, 'proveedor_nombre':proveedor_nombre, "url":avatares[0].imagen.url})
            except IndexError:
                  return render(request, 'RobertoMoraApp/EditarProveedor.html',{'miFormulario':miFormulario, 'proveedor_nombre':proveedor_nombre})

@login_required
def proveedor(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.method == "POST":
            miFormulario= ProveedorFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  proveedor= Proveedor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'], profesion=informacion['profesion'],empresa=informacion['empresa'])
                  proveedor.save()
                  try:
                        return render(request,'RobertoMoraApp/Proveedor.html',{"url":avatares[0].imagen.url})
                  except IndexError:
                        return render(request,'RobertoMoraApp/Proveedor.html')                        
      else:
            miFormulario=ProveedorFormulario()
            try:
                  return render (request, 'RobertoMoraApp/Proveedor.html', {"miFormulario":miFormulario,"url":avatares[0].imagen.url})
            except IndexError:
                  return render (request, 'RobertoMoraApp/Proveedor.html', {"miFormulario":miFormulario})


#DEFINICION; LECTURA Y ESCRITURA DE MATERIAL
@login_required
def leermaterial(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      material=Material.objects.all()
      try:
            contexto = {"material":material,"url":avatares[0].imagen.url}
            return render(request, 'RobertoMoraApp/LeerMaterial.html',contexto)
      except IndexError:
            contexto = {"material":material}
            return render(request, 'RobertoMoraApp/LeerMaterial.html',contexto)

@login_required
def eliminarmaterial(request,material_nombre):
      avatares=Avatar.objects.filter(user=request.user.id)
      material=Material.objects.get (nombre=material_nombre)
      material.delete()
      material=Material.objects.all()
      try:
            contexto = {"material":material,"url":avatares[0].imagen.url}
            return render(request, 'RobertoMoraApp/LeerMaterial.html',contexto)
      except IndexError:
            contexto = {"material":material}
            return render(request, 'RobertoMoraApp/LeerMaterial.html',contexto)

@login_required
def editarmaterial(request,material_nombre):
      avatares=Avatar.objects.filter(user=request.user.id)
      material=Material.objects.get (nombre=material_nombre)
      if request.method == 'POST':
            miFormulario= MaterialFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  material.nombre=informacion['nombre']
                  material.numeropedido=informacion['numeropedido']
                  material.cantidad=informacion['cantidad']
                  material.fechaDeEntrega=informacion['fechaDeEntrega']
                  material.entregado=informacion['entregado']
                  material.facturado=informacion['facturado']
                  material.save()
                  try:
                        return render(request,'RobertoMoraApp/Material.html',{"url":avatares[0].imagen.url})   
                  except IndexError: 
                        return render(request,'RobertoMoraApp/Material.html')  
      else:
            miFormulario=MaterialFormulario(initial={'nombre': material.nombre,'numeropedido':material.numeropedido, 'cantidad':material.cantidad, 'fechaDeEntrega':material.fechaDeEntrega, 'entregado':material.entregado, 'facturado':material.facturado})
            try:
                  return render(request, 'RobertoMoraApp/EditarMaterial.html',{'miFormulario':miFormulario, 'material_nombre':material_nombre,"url":avatares[0].imagen.url})
            except IndexError:
                  return render(request, 'RobertoMoraApp/EditarMaterial.html',{'miFormulario':miFormulario, 'material_nombre':material_nombre})
      
@login_required
def material(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.method == "POST":
            miFormulario= MaterialFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  material= Material(numeropedido= informacion['numeropedido'],nombre=informacion['nombre'], cantidad=informacion['cantidad'],fechaDeEntrega=informacion['fechaDeEntrega'], entregado=informacion['entregado'], facturado=informacion['facturado'])
                  material.save()
                  try:
                        return render(request,'RobertoMoraApp/Material.html',{"url":avatares[0].imagen.url})
                  except IndexError:
                        return render(request,'RobertoMoraApp/Material.html')
      else:
            miFormulario=MaterialFormulario()
            try: 
                  return render (request, 'RobertoMoraApp/Material.html', {"miFormulario":miFormulario,"url":avatares[0].imagen.url})
            except IndexError:
                  return render (request, 'RobertoMoraApp/Material.html', {"miFormulario":miFormulario})

#DEFINICION; LECTURA Y ESCRITURA DE FACTURA
@login_required
def leerfactura(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      factura=Factura.objects.all()
      try:
            contexto = {"factura":factura,"url":avatares[0].imagen.url}
            return render(request, 'RobertoMoraApp/LeerFactura.html',contexto)
      except IndexError:
            contexto = {"factura":factura}
            return render(request, 'RobertoMoraApp/LeerFactura.html',contexto)           

@login_required
def eliminarfactura(request,factura_numero):
      avatares=Avatar.objects.filter(user=request.user.id)
      factura=Factura.objects.get (numero=factura_numero)
      factura.delete()
      factura=Factura.objects.all()
      try:
            contexto = {"factura":factura,"url":avatares[0].imagen.url}
            return render(request, 'RobertoMoraApp/LeerFactura.html',contexto)
      except IndexError:
            contexto = {"factura":factura}
            return render(request, 'RobertoMoraApp/LeerFactura.html',contexto)  

@login_required
def editarfactura(request,factura_numero):
      avatares=Avatar.objects.filter(user=request.user.id)
      factura=Factura.objects.get (numero=factura_numero)
      if request.method == 'POST':
            miFormulario= FacturaFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  factura.numero=informacion['numero']
                  factura.fechafactura=informacion['fechafactura']
                  factura.total=informacion['total']
                  factura.save()
                  try: 
                        return render(request,'RobertoMoraApp/Factura.html',{"url":avatares[0].imagen.url})
                  except IndexError: 
                        return render(request,'RobertoMoraApp/Factura.html')   
      else:
            miFormulario=FacturaFormulario(initial={'numero': factura.numero,'fechafactura':factura.fechafactura, 'total':factura.total})
            try:
                  return render(request, 'RobertoMoraApp/EditarFactura.html',{'miFormulario':miFormulario, 'factura_numero':factura_numero,"url":avatares[0].imagen.url})
            except IndexError:
                  return render(request, 'RobertoMoraApp/EditarFactura.html',{'miFormulario':miFormulario, 'factura_numero':factura_numero})                 

@login_required
def factura(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.method == "POST":
            miFormulario= FacturaFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  factura= Factura(numero=informacion['numero'], fechafactura=informacion['fechafactura'],total=informacion['total'] )
                  factura.save()
                  try:
                        return render(request,'RobertoMoraApp/Factura.html',{"url":avatares[0].imagen.url})
                  except IndexError:
                        return render(request,'RobertoMoraApp/Factura.html')
      else:
            miFormulario=FacturaFormulario()
            try:
                  return render (request, 'RobertoMoraApp/Factura.html', {"miFormulario":miFormulario,"url":avatares[0].imagen.url})
            except IndexError:
                  return render (request, 'RobertoMoraApp/Factura.html', {"miFormulario":miFormulario})
   


#BUSQUEDAS
@login_required
def busquedas (request):
 avatares=Avatar.objects.filter(user=request.user.id)
 try:
      return render(request, "RobertoMoraApp/Busquedas.html",{"url":avatares[0].imagen.url})
 except IndexError:

      return render(request, "RobertoMoraApp/Busquedas.html")     

#Buscar Clientes

@login_required
def buscarnombrecliente (request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            cliente= Cliente.objects.filter(nombre__icontains=nombre)
            try:
                  return render (request, "RobertoMoraApp/BuscarNombreCliente.html",{"cliente":cliente ,"nombre":nombre,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNombreCliente.html",{"cliente":cliente ,"nombre":nombre} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarNombreCliente.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNombreCliente.html",{"respuesta":respuesta} )          

@login_required
def buscarapellidocliente (request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["apellido"]:
            apellido=request.GET['apellido']
            cliente= Cliente.objects.filter(apellido__icontains=apellido)
            try:
                  return render (request, "RobertoMoraApp/BuscarApellidoCliente.html",{"cliente":cliente ,"apellido":apellido,"url":avatares[0].imagen.url} )
            except:
                  return render (request, "RobertoMoraApp/BuscarApellidoCliente.html",{"cliente":cliente ,"apellido":apellido} )

      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarApellidoCliente.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarApellidoCliente.html",{"respuesta":respuesta} )


@login_required
def buscaremailcliente(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["email"]:
            email=request.GET['email']
            cliente= Cliente.objects.filter(email__icontains=email)
            try:
                  return render (request, "RobertoMoraApp/BuscarEmailCliente.html",{"cliente":cliente ,"email":email,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarEmailCliente.html",{"cliente":cliente ,"email":email} )

      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarEmailCliente.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarEmailCliente.html",{"respuesta":respuesta} )                  

@login_required
def buscarprofesioncliente(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["profesion"]:
            profesion=request.GET['profesion']
            cliente= Cliente.objects.filter(profesion__icontains=profesion)
            try:
                  return render (request, "RobertoMoraApp/BuscarProfesionCliente.html",{"cliente":cliente ,"profesion":profesion,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarProfesionCliente.html",{"cliente":cliente ,"profesion":profesion} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarProfesionCliente.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarProfesionCliente.html",{"respuesta":respuesta} )                 

@login_required
def buscarempresacliente(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["empresa"]:
            empresa=request.GET['empresa']
            cliente= Cliente.objects.filter(empresa__icontains=empresa)
            try:
                  return render (request, "RobertoMoraApp/BuscarEmpresaCliente.html",{"cliente":cliente ,"empresa":empresa,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarEmpresaCliente.html",{"cliente":cliente ,"empresa":empresa} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarEmpresaCliente.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarEmpresaCliente.html",{"respuesta":respuesta} )
   

#Buscar Proveedores
@login_required
def buscarnombreproveedor (request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            proveedor= Proveedor.objects.filter(nombre__icontains=nombre)
            try:
                  return render (request, "RobertoMoraApp/BuscarNombreProveedor.html",{"proveedor":proveedor ,"nombre":nombre,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNombreProveedor.html",{"proveedor":proveedor ,"nombre":nombre} )
                 
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarNombreProveedor.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNombreProveedor.html",{"respuesta":respuesta} )


@login_required
def buscarapellidoproveedor (request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["apellido"]:
            apellido=request.GET['apellido']
            proveedor= Proveedor.objects.filter(apellido__icontains=apellido)
            try:
                  return render (request, "RobertoMoraApp/BuscarApellidoProveedor.html",{"proveedor":proveedor ,"apellido":apellido,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarApellidoProveedor.html",{"proveedor":proveedor ,"apellido":apellido} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarApellidoProveedor.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarApellidoProveedor.html",{"respuesta":respuesta} )


@login_required
def buscaremailproveedor(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["email"]:
            email=request.GET['email']
            proveedor= Proveedor.objects.filter(email__icontains=email)
            try:
                  return render (request, "RobertoMoraApp/BuscarEmailProveedor.html",{"proveedor":proveedor ,"email":email,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarEmailProveedor.html",{"proveedor":proveedor ,"email":email} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarEmailCliente.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except:
                  return render (request, "RobertoMoraApp/BuscarEmailCliente.html",{"respuesta":respuesta} )

@login_required
def buscarprofesionproveedor(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["profesion"]:
            profesion=request.GET['profesion']
            proveedor= Proveedor.objects.filter(profesion__icontains=profesion)
            try:
                  return render (request, "RobertoMoraApp/BuscarProfesionProveedor.html",{"proveedor":proveedor ,"profesion":profesion,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarProfesionProveedor.html",{"proveedor":proveedor ,"profesion":profesion} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarProfesionProveedor.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarProfesionProveedor.html",{"respuesta":respuesta} )


@login_required
def buscarempresaproveedor(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["empresa"]:
            empresa=request.GET['empresa']
            proveedor= Proveedor.objects.filter(empresa__icontains=empresa)
            try:
                  return render (request, "RobertoMoraApp/BuscarEmpresaProveedor.html",{"proveedor":proveedor ,"empresa":empresa,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarEmpresaProveedor.html",{"proveedor":proveedor ,"empresa":empresa} ) 
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarEmpresaProveedor.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarEmpresaProveedor.html",{"respuesta":respuesta} )


#Buscar Materiales
@login_required
def buscarnumeropedidomaterial(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["numeropedido"]:
            numeropedido=request.GET['numeropedido']
            material= Material.objects.filter(numeropedido__icontains=numeropedido)
            try:
                  return render (request, "RobertoMoraApp/BuscarNumeroPedidoMaterial.html",{"material":material,"numeropedido":numeropedido,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNumeroPedidoMaterial.html",{"material":material,"numeropedido":numeropedido} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarNumeroPedidoMaterial.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNumeroPedidoMaterial.html",{"respuesta":respuesta} )


@login_required
def buscarnombrematerial(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            material= Material.objects.filter(nombre__icontains=nombre)
            try:
                  return render (request, "RobertoMoraApp/BuscarNombreMaterial.html",{"material":material,"nombre":nombre,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNombreMaterial.html",{"material":material,"nombre":nombre} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarNombreMaterial.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNombreMaterial.html",{"respuesta":respuesta} )


@login_required
def buscarcantidadmaterial (request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["cantidad"]:
            cantidad=request.GET['cantidad']
            material= Material.objects.filter(cantidad__icontains=cantidad)
            try:
                  return render (request, "RobertoMoraApp/BuscarCantidadMaterial.html",{"material":material ,"cantidad":cantidad,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarCantidadMaterial.html",{"material":material ,"cantidad":cantidad} )          
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarCantidadMaterial.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarCantidadMaterial.html",{"respuesta":respuesta} )
                 

@login_required
def  buscarfechaDeEntrega(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["fechaDeEntrega"]:
            fechaDeEntrega=request.GET['fechaDeEntrega']
            material= Material.objects.filter(fechaDeEntrega__icontains=fechaDeEntrega)
            try:
                  return render (request, "RobertoMoraApp/BuscarFechaDeEntrega.html",{"material":material ,"fechaDeEntrega":fechaDeEntrega,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarFechaDeEntrega.html",{"material":material ,"fechaDeEntrega":fechaDeEntrega} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarFechaDeEntrega.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarFechaDeEntrega.html",{"respuesta":respuesta} )


#Buscar Facturas
@login_required
def buscarnumerofactura (request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["numero"]:
            numero=request.GET['numero']
            facturas= Factura.objects.filter(numero__icontains=numero)
            try:
                  return render (request, "RobertoMoraApp/BuscarNumeroFactura.html",{"facturas":facturas ,"numero":numero,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNumeroFactura.html",{"facturas":facturas ,"numero":numero} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarNumeroFactura.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarNumeroFactura.html",{"respuesta":respuesta} )
                 

@login_required
def  buscarfechafactura(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["fechafactura"]:
            fechafactura=request.GET['fechafactura']
            facturas= Factura.objects.filter(fechafactura__icontains=fechafactura)
            try:
                  return render (request, "RobertoMoraApp/BuscarFechaFactura.html",{"facturas":facturas ,"fechafactura":fechafactura,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarFechaFactura.html",{"facturas":facturas ,"fechafactura":fechafactura} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarFechaFactura.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarFechaFactura.html",{"respuesta":respuesta} )


@login_required
def buscartotalfactura(request):
      avatares=Avatar.objects.filter(user=request.user.id)
      if request.GET["total"]:
            total=request.GET['total']
            facturas= Factura.objects.filter(total__icontains=total)
            try:
                  return render (request, "RobertoMoraApp/BuscarTotalFactura.html",{"facturas":facturas ,"total":total,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarTotalFactura.html",{"facturas":facturas ,"total":total} )
      else:
            respuesta="No enviaste datos"
            try:
                  return render (request, "RobertoMoraApp/BuscarTotalFactura.html",{"respuesta":respuesta,"url":avatares[0].imagen.url} )
            except IndexError:
                  return render (request, "RobertoMoraApp/BuscarTotalFactura.html",{"respuesta":respuesta} )

# #VIEWS CRUD easy way:
# class MaterialList(ListView):
#       model=Material
#       template_name="RobertoMoraApp/materiales_list.html"

# class MaterialDetalle(DetailView):
#       model=Material
#       template_name="RobertoMoraApp/materiales_detalle.html"

# class MaterialCreacion(CreateView):
#       model=Material
#       success_url="/RobertoMoraApp/material/list"
#       fields=['numeropedido','nombre','cantidad','fechaDeEntrega','entregado','facturado'] 

# class MaterialUpdate(UpdateView):
#       model=Material
#       success_url="/RobertoMoraApp/material/list"
#       fields=['numeropedido','nombre','cantidad','fechaDeEntrega','entregado','facturado'] 

# class MaterialDelete(UpdateView):
#       model=Material
#       success_url="/RobertoMoraApp/material/list"
