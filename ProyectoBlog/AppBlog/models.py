from django.db import models
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
#Los usuarios seran los que creen sus post o realicen comentarios de los post
class Usuario(models.Model):
    #id_usuario = models.IntegerField(unique=True, auto_created=True)
    nombre = models.CharField(max_length=40)
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    lastlogin = models.DateTimeField()
    dateregistro = models.DateTimeField()
    datecupleanho = models.DateTimeField()
    estado = models.IntegerField() 
    #Activo - Inactivo - Bloqueado - Eliminado ...
    
    def __str__(self):
        return f"Usuario: {self.nombre}, {self.usuario}, {self.password}, {self.email}, {self.lastlogin}, {self.dataregistro}, {self.datecupleanho}, {self.estado}"
    
#Existen categorias de post
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Categoria: {self.id_categoria}, {self.nombre}"
    
#Recordatorios para hacer mas facil la busqueda
class Tag(models.Model):
    id_tag = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=200)
    relacion = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Tags: {self.tag}, {self.relacion}"

#Estados en los cuales puede estar el usuario 
#Activo - Inactivo - Bloqueado - Eliminado ...
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Estado: {self.nombre}"
    
#Post que publicaran los usuarios
class Post(models.Model):
    autor=models.CharField(max_length=200)
    titulo=models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #categoria = models.CharField(max_length=40)
    tags=models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    fechapublicacion=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='post', blank=True, null=True)#   ----- VER COMO SUBIR FOTOS ----
    estado=models.ForeignKey(Estado, null=True, blank=True, on_delete=models.CASCADE) #borrador - publicado - baneado
    
    def __str__(self):
        return f"Post: {self.autor}, {self.titulo}, {self.body}, {self.categoria}, {self.tags}, {self.fechapublicacion}, {self.imagen}, {self.estado}"
       
#Comentarios que realizaran los usuarios sobre los post
class Comentario(models.Model):
    #id_comentarios = models.IntegerField(unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    fecha = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()

    def __str__(self):
        return f"Comentario: {self.autor}, {self.post}"
    
