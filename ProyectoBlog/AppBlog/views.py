import datetime

from tempfile import template
from urllib import request

from django.contrib import messages
from django.shortcuts import render, redirect

from AppBlog.models import *
from AppBlog.forms import UsuarioForm, BusquedaUsuarioForms, CategoriaForm, TagsForm


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
        'form': BusquedaUsuarioForms(),
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

def categoria_formulario(request):
    
    if  request.method == 'POST':
        mi_formulario = CategoriaForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            categoria1 = Categoria(nombre=data.get('nombre'),
                               parent=data.get('parent'))
            categoria1.save()
            
            return redirect('AppBlogCategoriaFormulario')
        
    
        else:
            mensaje = 'Ocurrio un error no se pudo guardar los datos'

        
    categoria = Categoria.objects.all()
    
    contexto = {
        'form': CategoriaForm(),
        'categoria': categoria
    }
    
    return render(request, 'AppBlog/categoria_formulario.html', contexto)

def tag_formulario(request):
    
    if  request.method == 'POST':
        mi_formulario = TagsForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            tag1 = Tags(tag=data.get('tag'),
                        relacion=data.get('relacion'))
            tag1.save()
            
            return redirect('AppBlogTagFormulario')
        
    
        else:
            mensaje = 'Ocurrio un error no se pudo guardar los datos'

        
    tag = Tags.objects.all()
    
    contexto = {
        'form': TagsForm(),
        'tag': tag
    }
    
    return render(request, 'AppBlog/tag_formulario.html', contexto)

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
