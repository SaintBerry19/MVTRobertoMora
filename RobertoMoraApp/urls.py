from django.urls import path

from RobertoMoraApp import views

urlpatterns = [
   
    path('', views.inicio,name='Inicio' ), 
    path('Cliente', views.cliente, name='Cliente'),
    path('Proveedor', views.proveedor,name='Proveedor'),
    path('Material', views.material,name='Material'),
    path('Factura', views.factura,name='Factura'),
    path('BusquedaFactura', views.busquedafactura, name='BusquedaFactura'),
    path('BuscarFactura/', views.buscarfactura),
]

