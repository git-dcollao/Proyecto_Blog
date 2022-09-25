import datetime
from msilib.schema import Class
import django

from tempfile import template
from urllib import request

from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import render, redirect

from AppBlog.models import *
from AppBlog.forms import UsuarioForm, BusquedaUsuarioForms, CategoriaForm, TagsForm, EstadoForm


#=====================================================
# Crear vista de busqueda con formulario
#=====================================================

# Muestra los usuarios filtrados
def busqueda_usuario_post(request):
    usuario = request.GET.get('usuario')
    
    usuarios = Usuario.objects.filter(usuario__icontains=usuario)
    contexto = {
        'usuarios': usuarios        
    }
    
    return render(request, 'AppBlog/usuario_filtrado.html', contexto)
# Muestra todos los usaurios 
def busqueda_usuario(request):
    
    contexto = {
        'form': BusquedaUsuarioForms(),
    }
    
    return render(request, 'AppBlog/busqueda_usuario.html', contexto)
  

#=====================================================    
# Crear Vista de formularios
#=====================================================
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
        'categorias': categoria
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
        'tags': tag
    }
    
    return render(request, 'AppBlog/tag_formulario.html', contexto)

#Formulario de Estados 
#Borrador - Publicado - Baneado
#class EstadoList(ListView): 
#    model = Estado
#    template_name = 'AppBlog/estado.html'
    
def estado(request):
    estados = Estado.objects.all()
    contexto = {
        'estados': estados
    }
    
    return render(request, 'AppBlog/estado.html', contexto)

def estado_formulario(request):
    
    if request.method == 'POST':
        mi_formulario = EstadoForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            estado1 = Estado(nombre=data.get('nombre'))
            estado1.save()
            
            return redirect('AppBlogEstado')
        
        else:
            mensaje = 'Ocurrio un error no se pudo guardar los datos'
            
    
    contexto = {
        'form' : EstadoForm()
    }

    return render(request, 'AppBlog/estado_formulario.html', contexto)

def eliminar_estado(request, nombre):
    estado_eliminar = Estado.objects.get(nombre=nombre)
    estado_eliminar.delete()
    
    messages.info(request, f"El estado {estado_eliminar} fue eliminado con exito")
    
    return redirect("AppBlogEstado")
    
def editar_estado(request, nombre):
    estado_editar = Estado.objects.get(nombre=nombre)
    
    if request.method == 'POST':
        mi_formulario = EstadoForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            estado_editar.nombre = data.get('nombre')
            try:
                estado_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "La modificación fallo, porque el estado se encuentra duplicado")

            return redirect('AppBlogEstado')
        
        else:
            mensaje = 'Ocurrio un error no se pudo editar el dato'
            
    
    
    contexto = {
        'form': EstadoForm(
            initial={
                "nombre": estado_editar.nombre
            }
        )
    }
    return render(request, 'AppBlog/estado_formulario.html', contexto)




#Formulario de categoria 
def categoria(request):
    estados = Categoria.objects.all()
    contexto = {
        'categorias': categoria
    }
    
    return render(request, 'AppBlog/categoria.html', contexto)
#=====================================================
#=====================================================
#NO CREADOS AUN


def post(request):

    return render(request, 'index.html', {})

def comentarios(request):

    return render(request, 'index.html', {})

def inicio(request):

    return render(request, 'index.html', {})

def usuario(request):

    return render(request, 'index.html', {})

def tags(request):

    return render(request, 'index.html', {})