import datetime

from tempfile import template
from urllib import request

from django.contrib import messages
from django.shortcuts import render, redirect

from AppBlog.models import *
from AppBlog.forms import UsuarioForm, BusquedaUsuarioForm


# Crear vista de busqueda con formulario
def busqueda_usuario_post(request):
    usuario = request.GET.get('usuario')
    
    usuarios = Usuario.objects.filter(usuario__icontains=usuario)
    contexto = {
        'usuarios': usuarios        
    }
    
    return render(request, 'AppBlog/usuario_filtrado.html', contexto)
    
    
def busqueda_usuario(request):
    
    contexto = {
        'form': BusquedaUsuarioForm(),
    }
    
    return render(request, 'AppBlog/busqueda_usuario.html', contexto)
    
    
# Crear Vista de formularios
def usuario_formulario(request):
    
    if  request.method == 'POST':
        mi_formulario = UsuarioForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            usuario1 = Usuario(nombre=data.get('nombre'),
                               usuario=data.get('usuario'),
                               password=data.get('password'),
                               email=data.get('email'),
                               lastlogin=data.get('lastlogin'),
                               dateregistro=data.get('dateregistro'),
                               datecupleanho=data.get('datecupleanho'),
                               estado=data.get('estado'))
            usuario1.save()
            
            return redirect('AppBlogUsuarioFormulario')
        
    
        else:
            mensaje = 'Ocurrio un error no se pudo guardar los datos'

        
    usuario = Usuario.objects.all()
    
    contexto = {
        'form': UsuarioForm(),
        'usuarios': usuario
    }
    
    return render(request, 'AppBlog/usuario_formulario.html', contexto)

# Create your views here.

def inicio(request):

    return render(request, 'index.html', {})

def usuario(request):

    return render(request, 'index.html', {})

def tags(request):

    return render(request, 'index.html', {})

def categoria(request):

    return render(request, 'index.html', {})

def post(request):

    return render(request, 'index.html', {})

def comentarios(request):

    return render(request, 'index.html', {})
