from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),

    # Gestión de usuarios
    path('usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('usuarios/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Gestión de productos
    path('productos/', views.gestion_productos, name='gestion_productos'),

    # Gestión de pedidos
    path('pedidos/', views.gestion_pedidos, name='gestion_pedidos'),

    # Reportes y configuración
    path('reportes/', views.gestion_reportes, name='gestion_reportes'),
    path('configuracion/', views.configuracion, name='configuracion'),
]