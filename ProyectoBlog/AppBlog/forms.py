from dataclasses import fields
from django import forms
from django.forms import CharField, ModelForm
from .models import *


class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    usuario = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)
    email = forms.EmailField()
    lastlogin = forms.DateTimeField()
    dateregistro = forms.DateTimeField()
    datecupleanho = forms.DateTimeField()
    estado = forms.IntegerField() 
    #Activo - Inactivo - Bloqueado - Eliminado ...
    
class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    
class PostForm(forms.Form):
    #class Meta:
       # models = Post
       # fields = '__all__'
    autor = forms.CharField(max_length=200)
    titulo = forms.CharField(max_length=200)
    body = forms.Textarea()
    category = forms.IntegerField()
    tags = forms.IntegerField()
    fechapublicacion = forms.DateField()
    imagen = forms.CharField(max_length=200) #   ----- VER COMO SUBIR FOTOS ----
    estado = forms.IntegerField() #inicio - publicado - baneado
    
    
class TagsForm(forms.Form):
    tag = forms.CharField(max_length=200)
    relacion = forms.CharField(max_length=200)
    
class ComentariosForm(forms.Form):
    #id_comentarios = forms.IntegerField(unique=True)
    userId = forms.IntegerField()
    postId = forms.IntegerField()   
    titulo = forms.CharField(max_length=200)
    fecha = forms.DateField()

class EstadoForm(forms.Form):
    #id_estado = forms.IntegerField(unique=True)
    nombre = forms.CharField(max_length=100)
    

#=====================================================
# CLASES DE BUSQUEDAS
#=====================================================
#Busqueda de usaurios 
class BusquedaUsuarioForms(forms.Form):
    usuario = forms.CharField()

class BusquedaCategoriaForms(forms.Form):
    categoria = forms.CharField()
    
class BusquedaPostForms(forms.Form):
    titulo = CharField()

class BusquedaTagForms(forms.Form):
    tag = forms.CharField()
    
class BusquedaComnetarioForms(forms.Form):
    titulo = forms.CharField()

class BusquedaEstadoForms(forms.Form):
    tag = forms.CharField()
    