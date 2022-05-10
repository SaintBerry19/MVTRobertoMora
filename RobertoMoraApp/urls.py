from django.urls import path

from RobertoMoraApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio,name='Inicio' ), 
    path('Cliente', views.cliente, name='Cliente'),
    path('Proveedor', views.proveedor,name='Proveedor'),
    path('Material', views.material,name='Material'),
    path('Factura', views.factura,name='Factura'),
    path('Busquedas', views.busquedas, name='Busquedas'),
    #Factura
    path('BuscarNumeroFactura/', views.buscarnumerofactura),
    path('BuscarFechaFactura/', views.buscarfechafactura),
    path('BuscarTotalFactura/', views.buscartotalfactura),
    #Cliente
    path('BuscarNombreCliente/', views.buscarnombrecliente),
    path('BuscarApellidoCliente/', views.buscarapellidocliente),
    path('BuscarEmailCliente/', views.buscaremailcliente),
    path('BuscarProfesionCliente/', views.buscarprofesioncliente),
    path('BuscarEmpresaCliente/', views.buscarempresacliente),
    #Proveedor
    path('BuscarNombreProveedor/', views.buscarnombreproveedor),
    path('BuscarApellidoProveedor/', views.buscarapellidoproveedor),
    path('BuscarEmailProveedor/', views.buscaremailproveedor),
    path('BuscarProfesionProveedor/', views.buscarprofesionproveedor),
    path('BuscarEmpresaProveedor/', views.buscarempresaproveedor),
    #Material
    path('BuscarNumeroPedidoMaterial/', views.buscarnumeropedidomaterial),
    path('BuscarNombreMaterial/', views.buscarnombrematerial),
    path('BuscarCantidadMaterial/', views.buscarcantidadmaterial),
    path('BuscarFechaDeEntrega/', views.buscarfechaDeEntrega),
    #Lecturas
    #clientes
    path('LeerCliente/', views.leercliente),
    path('eliminarcliente/<cliente_nombre>/', views.eliminarcliente, name="EliminarCliente"),
    path('editarcliente/<cliente_nombre>/', views.editarcliente, name="EditarCliente"),
    #proveedor
    path('LeerProveedor/', views.leerproveedor),
    path('eliminarproveedor/<proveedor_nombre>/', views.eliminarproveedor, name="EliminarProveedor"),
    path('editarproveedor/<proveedor_nombre>/', views.editarproveedor, name="EditarProveedor"),
    #material
    path('LeerMaterial/', views.leermaterial),
    path('eliminarmaterial/<material_nombre>/', views.eliminarmaterial, name="EliminarMaterial"),
    path('editarmaterial/<material_nombre>/', views.editarmaterial, name="EditarMaterial"),
    #facturas
    path('LeerFactura/', views.leerfactura),
    path('eliminarfactura/<factura_numero>/', views.eliminarfactura, name="EliminarFactura"),
    path('editarfactura/<factura_numero>/', views.editarfactura, name="EditarFactura"),
    #logins
    path('login', views.login_request,name='Login'),
    path('register', views.register,name='Register'),
    path('EditarPerfil', views.editarPerfil,name='EditarPerfil'),
    path('logout', LogoutView.as_view(template_name='RobertoMoraApp/logout.html'),name='logout'),
    # #CRUDS VIEWS CBV
    # path('material/list',views.MaterialList.as_view(),name='List'),
    # path(r'^(?P<pk>\d+)$', views.MaterialDetalle.as_view(), name='Detail'),
    # path(r'^nuevo$', views.MaterialCreacion.as_view(), name='New'),
    # path(r'^editar/(?P<pk>\d+)$', views.MaterialUpdate.as_view(), name='Edit'),
    # path(r'^borrar/(?P<pk>\d+)$', views.MaterialDelete.as_view(), name='Delete'),

]

