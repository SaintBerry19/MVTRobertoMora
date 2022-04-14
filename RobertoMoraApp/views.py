import datetime
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from RobertoMoraApp.models import Cliente,Proveedor,Material,Factura
from RobertoMoraApp.forms import ClienteFormulario,ProveedorFormulario,MaterialFormulario,FacturaFormulario

# Create your views here.

def inicio(request):

      return render(request, "RobertoMoraApp/Inicio.html")

def cliente(request):
      if request.method == 'POST':
            miFormulario= ClienteFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  cliente= Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'], profesion=informacion['profesion'], empresa=informacion['empresa'])
                  cliente.save()
            return render(request,'RobertoMoraApp/inicio.html')
      else:
            miFormulario=ClienteFormulario()
      return render (request, 'RobertoMoraApp/Cliente.html', {"miFormulario":miFormulario})

def proveedor(request):
      if request.method == "POST":
            miFormulario= ProveedorFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  proveedor= Proveedor(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'], profesion=informacion['profesion'],empresa=informacion['empresa'])
                  proveedor.save()
            return render(request,'RobertoMoraApp/inicio.html')
      else:
            miFormulario=ProveedorFormulario()
      return render (request, 'RobertoMoraApp/Proveedor.html', {"miFormulario":miFormulario})


def material(request):
      if request.method == "POST":
            miFormulario= MaterialFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  material= Material(nombre=informacion['nombre'], cantidad=informacion['cantidad'],fechaDeEntrega=datetime.datetime(informacion['fecha de entrega']), entregado=informacion['entregado'], facturado=informacion['facturado'])
                  material.save()
            return render(request,'RobertoMoraApp/inicio.html')
      else:
            miFormulario=MaterialFormulario()
      return render (request, 'RobertoMoraApp/Material.html', {"miFormulario":miFormulario})


def factura(request):
      if request.method == "POST":
            miFormulario= FacturaFormulario(request.POST)
            print (miFormulario)
            if miFormulario.is_valid:
                  informacion =miFormulario.cleaned_data
                  factura= Factura(numero=informacion['numero'], fechafactura=informacion['fechafactura'],total=informacion['total'] )
                  factura.save()
            return render(request,'RobertoMoraApp/inicio.html')
      else:
            miFormulario=FacturaFormulario()
      return render (request, 'RobertoMoraApp/Factura.html', {"miFormulario":miFormulario})

def buscarfactura (request):
      if request.GET["numero"]:
            numero=request.GET['numero']
            facturas= Factura.objects.filter(numero__icontains=numero)
            return render (request, "RobertoMoraApp/BuscarFactura.html",{"facturas":facturas ,"numero":numero} )
      else:
            respuesta="No enviaste datos"
      return render(request,"RobertoMoraApp/BuscarFactura.html",{"respuesta":respuesta})