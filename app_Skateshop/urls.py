# Contenido de app_Skateshop/urls.py (ACTUALIZADO)
from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio_skateshop, name='inicio_skateshop'),
    
    # Rutas CRUD de Clientes
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_clientes, name='ver_clientes'),
    path('cliente/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/actualizar_post/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),
    
    # Rutas CRUD de Proveedores
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/actualizar_post/<int:pk>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),

    # Rutas futuras para Producto (solo placeholders)
    # path('producto/...', views.alguna_funcion_producto, name='...'),
]