from django.contrib.auth import logout, authenticate, login,get_user_model
from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from .forms import LoginForm, RegistroForm 
from .models import Producto,Pedido, UsuarioPersonalizado
from django.contrib import messages




User = get_user_model() 
def dashboard_admin(request):
    total_usuarios = User.objects.count()
    total_productos = 100  # ejemplo, ajusta según tu modelo Producto
    total_pedidos = 50    # ejemplo, ajusta según tu modelo Pedido

    # Obtener últimos usuarios registrados (los 5 más recientes por ejemplo)
    ultimos_usuarios = User.objects.order_by('-date_joined')[:5]

    context = {
        'total_usuarios': total_usuarios,
        'total_productos': total_productos,
        'total_pedidos': total_pedidos,
        'ultimos_usuarios': ultimos_usuarios,
    }
    return render(request, 'tu_template.html', context)


def eliminar_usuario(request, user_id):
    if request.method == 'POST':
        usuario = get_object_or_404(User, id=user_id)
        usuario.delete()
        return redirect('gestion_usuarios')  # Cambia esto según tu vista de lista

def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role')  # Puedes guardarlo en perfil extendido si lo tienes
        is_active = request.POST.get('status') == 'on'
        password = User.objects.make_random_password()  # O pide un password

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active
        )
        

        return redirect('gestion_usuarios')  # Cambia esto según tu vista principal
    


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=password)

            if user is not None:
                login(request, user)  # <- LOGIN SIEMPRE QUE SEA VÁLIDO
                
                if user.is_staff:
                    return redirect('dashboard')  # vista del admin
                else:
                    return redirect('index')   # vista del usuario normal
            else:
                error_message = "Datos inválidos"
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def admin_dashboard(request):
    total_usuarios = UsuarioPersonalizado.objects.count()
    total_productos = Producto.objects.count()
    total_pedidos = Pedido.objects.count()

    context = {
        'total_usuarios': total_usuarios,
        'total_productos': total_productos,
        'total_pedidos': total_pedidos,
    }
    return render(request, 'core/dashboard.html', context)
def gestion_productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/gestion_productos.html', {'productos': productos})
def gestion_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'core/gestion_pedidos.html', {'pedidos': pedidos})
def gestion_productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/gestion_productos.html', {'productos': productos})

#Registro de usuario

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')  # O a donde quieras redirigir
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})



#metodo home 
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def portfolio(request):
    return HttpResponse(request,"core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")

def index(request):
    return render(request, "core/index.html")



def gestion_usuarios(request):
    usuarios = UsuarioPersonalizado.objects.all()
    return render(request, 'core/gestion_usuario.html', {'usuarios': usuarios})

def gestion_reportes(request):
    # Puedes personalizar los datos mostrados
    pedidos = Pedido.objects.all()
    productos = Producto.objects.all()
    usuarios = UsuarioPersonalizado.objects.all()

    return render(request, 'core/gestion_reportes.html', {
        'pedidos': pedidos,
        'productos': productos,
        'usuarios': usuarios
    })

def configuracion(request):
    return render(request, 'core/configuracion.html')






