from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from core.models import UsuarioPersonalizado, Producto, Pedido  # Ajusta 'core' a tu app de modelos

User = get_user_model()

def admin_dashboard(request):
    total_usuarios = UsuarioPersonalizado.objects.count()
    total_productos = Producto.objects.count()
    total_pedidos = Pedido.objects.count()

    ultimos_usuarios = UsuarioPersonalizado.objects.order_by('-date_joined')[:5]

    context = {
        'total_usuarios': total_usuarios,
        'total_productos': total_productos,
        'total_pedidos': total_pedidos,
        'ultimos_usuarios': ultimos_usuarios,
    }
    return render(request, 'dashboard/dashboard.html', context)


def gestion_usuarios(request):
    usuarios = UsuarioPersonalizado.objects.all()
    return render(request, 'dashboard/gestion_usuarios.html', {'usuarios': usuarios})


def eliminar_usuario(request, user_id):
    if request.method == 'POST':
        usuario = get_object_or_404(User, id=user_id)
        usuario.delete()
        return redirect('gestion_usuarios')


def gestion_productos(request):
    productos = Producto.objects.all()
    return render(request, 'dashboard/gestion_productos.html', {'productos': productos})

def gestion_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'dashboard/gestion_pedidos.html', {'pedidos': pedidos})


def gestion_reportes(request):
    return render(request, 'dashboard/gestion_reportes.html')

def configuracion(request):
    return render(request, 'dashboard/configuracion.html')
