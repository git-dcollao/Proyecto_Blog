from django.db import models
from django.views.generic import ListView, DetailView

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
    #id_categoria = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=40)
    parent = models.IntegerField()
    
    def __str__(self):
        return f"Categoria: {self.nombre}, {self.parent}"
    
#Post que publicaran los usuarios
class Post(models.Model):
    #id_post = models.IntegerField(unique=True)
    autor = models.IntegerField()
    titulo = models.CharField(max_length=200)
    body = models.TextField()
    category = models.IntegerField()
    tags = models.IntegerField()
    fechapublicacion = models.DateField()
    ultimaactualizacion = models.DateField()
    imagen = models.CharField(max_length=200) #   ----- VER COMO SUBIR FOTOS ----
    estado = models.IntegerField() #borrador - publicado - baneado
    
    def __str__(self):
        return f"Post: {self.autor}, {self.titulo}, {self.body}, {self.category}, {self.tags}, {self.fechapublicacion}, {self.ultimaactualizacion}, {self.imagen}, {self.estado}"
        
#Recordatorios para hacer mas facil la busqueda
class Tag(models.Model):
    #id_tags = models.IntegerField(unique=True)
    tag = models.CharField(max_length=200)
    relacion = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Tags: {self.tag}, {self.relacion}"
    
#Comentarios que realizaran los usuarios sobre los post
class Comentario(models.Model):
    #id_comentarios = models.IntegerField(unique=True)
    userId = models.IntegerField()
    postId = models.IntegerField()   
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()

    def __str__(self):
        return f"Comentario: {self.userId}, {self.postId}, {self.titulo}, {self.fecha}"
    
#Estados en los cuales puede estar el usuario 
#Activo - Inactivo - Bloqueado - Eliminado ...
class Estado(models.Model):
    #id_estado = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Estado: {self.nombre}"
    