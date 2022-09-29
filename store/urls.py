"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboardAdmin/', views.dashboardAdmin, name='dashboardAdmin'),
    path('dashboardCliente/', views.dashboardCliente, name='dashboardCliente'),
    path('productos/', views.productos, name='productos'),
    path('registrarnuevocliente/', views.registrarnuevocliente, name='registrarnuevocliente'),
    path('contacto/', views.contacto, name='contacto'),
    path('template/', views.contacto, name='template'),
    path('registro/', views.register, name='registro'),
    

]
