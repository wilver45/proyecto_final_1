from django.contrib import admin
from django.urls import path, include
from . import views  # Vistas públicas de tu sitio

urlpatterns = [
    
    path('admin/', admin.site.urls),

   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('index/', views.index, name='index'),

    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),

    
    path('dashboard/', include('dashboard.urls')),
]