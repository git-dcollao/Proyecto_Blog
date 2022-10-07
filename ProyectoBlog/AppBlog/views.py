import datetime
from msilib.schema import Class
import django

from tempfile import template
from urllib import request
from django.urls import is_valid_path

from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import render, redirect

from AppBlog.models import *
from AppBlog.forms import UsuarioForm, BusquedaUsuarioForms, CategoriaForm, TagsForm, EstadoForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


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
@login_required
def busqueda_usuario(request):
    
    contexto = {
        'form': BusquedaUsuarioForms(),
        'titulo_form': 'Usuario Formulario',
        'boton_envio': 'Actualizar'
    }
    
    return render(request, 'base_formulario.html', contexto)
  

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
   
def estado(request):
    estados = Estado.objects.all()
    
    contexto = {
        'estados_list': estados
        
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
        'form' : EstadoForm(),
        'titulo_form': 'Estado Formulario',
        'boton_envio': 'Crear'
    }

    return render(request, 'base_formulario.html', contexto)

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
        ),
        'titulo_form': 'Estado Formulario',
        'boton_envio': 'Actualizar'
    }
    return render(request, 'base_formulario', contexto)

#Formulario de categoria 
def categoria(request):
    categoria = Categoria.objects.all()
    
    contexto = {
        'categorias': categoria
    }
    
    return render(request, 'AppBlog/categoria.html', contexto)

#Para mostrar todos los post
def post(request):
    
    post1 = Post.objects.all()
    post1.save()
    contexto = {
        'posts': post1
        
    }
    
    return render(request, 'AppBlog/post.html', contexto)

def post_formulario(request):
    if request.method == 'POST':
        mi_formulario = PostForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            post1 = Post(autor=data.get('autor'), 
                         titulo=data.get('titulo'),
                         body=data.get('body'),
                         category = data.get('category'),
                         tag = data.get('tag'),
                         fehcapublicacion=data.get('fechapublicacion'),
                         ultimaactualizacion=data.get('ultimaactualizacion'),
                         imagen=data.get('imagen'),
                         estado=data.get('estado')
                         )
            post1.save()
            
            return redirect('AppBlogInicio')
        
        else:
            mensaje = 'Ocurrio un error no se pudo guardar los datos'
            
    contexto = {
        'form': PostForm()
        ,'titulo_form': 'Registro de Post'
        ,'boton_envio': 'Publicar'
    }

    return render(request, 'AppBlog/post_formulario.html', contexto)

def tag_formulario(request):
    if request.method == 'POST':
        mi_formulario = TagsForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            tag1 = Tag(tag=data.get('tag'), 
                         relacion=data.get('relacion')
                         )
            tag1.save()
            
            return redirect('AppBlogInicio')
        
        else:
            mensaje = 'Ocurrio un error no se pudo guardar los datos'
         
    contexto = {
        'form': TagsForm()
        ,'titulo_form': 'Registro de Tag'
        ,'boton_envio': 'Enviar' 
    }
    
    return render(request, 'AppBlog/tag_formulario.html', contexto)




#=====================================================
#=====================================================
#NO CREADOS AUN




def comentarios(request):

    return render(request, 'index.html', {})

def inicio(request):

    return render(request, 'inicio.html', {})

def usuario(request):

    return render(request, 'index.html', {})

def tags(request):

    return render(request, 'index.html', {})

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#                       LISTOS
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

def aboutme(request):
    
    return render(request, 'aboutme.html', {})

def contacto(request):
	if request.method == "POST":
		message_name = request.POST['contact-name']
		message_email = request.POST['contact-email']
		message = request.POST['contact-message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['daniel.collao@gmail.com'], # To Email
			)

		return render(request, 'contacto.html', {'message_name': message_name})

	else:
		return render(request, 'contacto.html', {})



#no lo he hecho para ver todos los post pero que sean restringido solo usuarios logeados
class postList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'AppBlog/post.html' 