from email.mime import image
import string
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .forms import RegisterForm
from django.contrib.auth.models import User
from products.models import Product

def index(request):
    return render(request, 'index.html', {
        'mensaje': 'Lista de productos'
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')

    return render(request, 'login.html', {
    })


def logout_view(request):
    logout (request)
    messages.success(request, 'Sesión Finalizada')
    return redirect ('login') 


def dashboardAdmin(request):
    return render(request, 'dashboardAdmin.html', {
    })


def dashboardCliente(request):
    return render(request, 'dashboardCliente.html', {
    })


def productos(request):

    products = Product.objects.all()

    return render(request, 'productos.html', {
    })


def registrarnuevocliente(request):
    return render(request, 'registrarnuevocliente.html', {
    })


def contacto(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']        
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('template.html', {
            'name': name,
            'email': email,                                
            'subject': subject,            
            'message': message,            
        })
    
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['contactoarepasjc@gmail.com']
        )
    
        email.fail_silently = False
        email.send()
    
    return render(request, 'contacto.html',{

    })

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST'and form.is_valid():
        

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect (index)

    return render (request, 'registro.html', {
        'form': form
        })

