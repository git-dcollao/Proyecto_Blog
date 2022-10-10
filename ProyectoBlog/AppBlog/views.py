import datetime
from gc import get_objects
import django

from tempfile import template
from urllib import request
from django.urls import is_valid_path

from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from AppBlog.models import *
from AppBlog.forms import UsuarioForm, BusquedaUsuarioForms, CategoriaForm, TagsForm, EstadoForm, PostForm, ComentariosForm
from AppBlog.forms import BusquedaCategoriaForms, BusquedaPostForms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from .models import Post
from ckeditor.fields import RichTextField

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
 
def busqueda_post_post(request):
    nombre = request.GET.get('post')
    
    categoria = Categoria.objects.filter(nombre__icontains=nombre)
        
    contexto = {
        'categorias': categoria,
        'form_titulo': 'Busqueda categoria por nombre',
        'titulo_form': 'Busqueda de Categorias',
        'boton_envio': 'Buscar'
                
    }

    return render(request, 'AppBlog/base_filtrado.html', contexto)


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


#Para mostrar todos los post
@login_required()
def post(request):
    post = Post.objects.all()
    contexto = {
        'form': PostForm(),
        'posts': post,
        'titulo_form': 'Formulario de Post',
        'boton_envio': 'Crear'
    }
    
    return render(request, 'AppBlog/post.html', contexto)

@login_required()
def post_formulario(request):
    if request.method == 'POST':
        mi_formulario = PostForm(request.POST, files=request.FILES)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            post1 = Post(autor = data.get('user.username'), 
                         titulo = data.get('titulo'),
                         body = data.get('body'),
                         categoria = data.get('categoria'),
                         tag = data.get('tag'),
                         fehcapublicacion = datetime.date.today() ,
                         imagen = data.get('imagen'),
                         estado = data.get('estado')
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

def busqueda_post(request, id):
    post = Post.objects.get(id=id)
    post = Post.objects.filter(id__icontains=id)
        
    contexto = {
        'posts': post,
        'form_titulo': 'Busqueda post por nombre',
        'titulo_form': 'Busqueda de Post',
        'boton_envio': 'Siguiente'
                
    }

    return render(request, 'AppBlog/articulodetalles.html', contexto)

def busqueda_post_categoria(request, id, nombre):
    post = Post.objects.get(id=id)
    post = Post.objects.filter(id__icontains=id)
        
    contexto = {
        'posts': post,
        'form_titulo': 'Busqueda post por nombre',
        'post_tipo': nombre,
        'boton_envio': 'Siguiente'
                
    }

    return render(request, 'AppBlog/post_list.html', contexto)



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


#Formulario de categoria 
def categoria(request):
    categoria = Categoria.objects.all()
    
    contexto = {
        'form': CategoriaForm(),
        'categorias': categoria,
        'boton_envio': 'Crear'
    }
    
    return render(request, 'AppBlog/categoria.html', contexto)

def categoria_formulario(request):
    if request.method == 'POST':
        mi_formulario = CategoriaForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            categoria1 = Categoria(id_categoria=data.get('id_categoria'), 
                                   nombre=data.get('nombre'))
            try:
                categoria1.save()
                messages.info(request,'Los datos fueron ingresados con exito')
                
            except django.db.utils.IntegrityError:
                messages.error(request,"Ocurrio un error no se pudo guardar los datos")
                
            return redirect('AppBlogCategoria')
        
        else:
            messages.error(request,"Ocurrio un error no se pudo guardar los datos")
    
    categorias = Categoria.objects.all()
    
    contexto = {
        'form': CategoriaForm(),
        'titulo_form': 'Ingreso de Categoria',
        'boton_envio': 'Crear',
        'categorias': categorias,
    }

    return render(request, 'AppBlog/categoria_formulario.html', contexto)

def eliminar_categoria(request, id_categoria):
    categoria_eliminar = Categoria.objects.get(id_categoria=id_categoria)
    try:
        categoria_eliminar.delete()
        messages.info(request, f"La categoria {categoria_eliminar} fue eliminada con exito")
    except django.db.utils.IntegrityError:
        messages.error(request, f"Ocurrio un error no pudo ser eliminada la categoria: {categoria_eliminar}")

    return redirect("AppBlogCategoria")

def editar_categoria(request, id_categoria):
    categoria_editar = Categoria.objects.get(id_categoria=id_categoria)
    
    if request.method == 'POST':
        mi_formulario = CategoriaForm(request.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            categoria_editar.id_categoria = data.get('id_categoria')
            categoria_editar.nombre = data.get('nombre')
            
            try: 
                categoria_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request," La modificación fallo  ")
                
            return redirect('AppBlogCategoria')
            
    contexto = {
        'form': CategoriaForm(
            initial={
                "parent": categoria_editar.id_categoria,
                "nombre": categoria_editar.nombre
                }
            ),
        'titulo_form': 'Formulario de Categoria',
        'boton_envio': 'Actualizar'
    }
    
    return render(request, 'AppBlog/categoria_formulario.html', contexto)

def busqueda_categoria_post(request):
    nombre = request.GET.get('nombre')
    
    categoria = Categoria.objects.filter(nombre__icontains=nombre)
        
    contexto = {
        'categorias': categoria,
        'form_titulo': 'Busqueda categoria por nombre',
        'titulo_form': 'Busqueda de Categorias',
        'boton_envio': 'Buscar'
                
    }

    return render(request, 'AppBlog/base_filtrado.html', contexto)

def busqueda_categoria(request):
    
    contexto = {
        'form': BusquedaCategoriaForms(),
        'titulo_form': 'Busqueda de Categorias',
        'boton_envio': 'Buscar'
                
    }

    return render(request, 'forms/Busquedas.html', contexto)
    
    
    
#=====================================================
#=====================================================
def comentarios(request):

    return render(request, 'index.html', {})

def comentario_formulario(request):
    #post = get_object_or_404(Post, id_post=id_post)
    
    #contexto = {        'form':     }
    
    if request.method == 'POST':
        mi_formulario = ComentariosForm(request.POST)
        #mi_formulario = ComentariosForm.objects.all()
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            comentarios1 = Comentario(
                userId= data.get('id_user'), 
                postId=data.get('id'), 
                titulo=data.get('titulo'), 
                fecha=data.get('fecha'))
            try:
                comentarios1.save()
                messages.info(request,'Los datos fueron ingresados con exito')
                
            except django.db.utils.IntegrityError:
                messages.error(request,"Ocurrio un error no se pudo guardar los datos")
                
            return redirect('AppBlogComentario')
        
        else:
            messages.error(request,"Ocurrio un error no se pudo guardar los datos")
    
    comentarios = Comentario.objects.all()
    
    contexto = {
        'form': ComentariosForm(),
        'titulo_form': 'Ingreso de Comentario',
        'boton_envio': 'Crear',
        'comentarios': comentarios,
    }

    return render(request, 'AppBlog/comentarios_formulario.html', contexto)    

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
def inicio(request):
    post = Post.objects.all()
    contexto = {
        'posts' : post
    }
    return render(request, 'AppBlog/inicio.html', contexto )    






#--------------------------------------------------
#  CODIFGO NO UTILIZADO
#--------------------------------------------------

#def busqueda_post(request):
# 
#    contexto = {
#        'form': BusquedaPostForms(),
#        'titulo_form': 'Busqueda de Titulos de Post',
#        'boton_envio': 'Buscar'           
#    }
#    return render(request, 'AppBlog/Busqueda_categoria.html', contexto)
