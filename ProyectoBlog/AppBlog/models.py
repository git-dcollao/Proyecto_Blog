from django.db import models

# Create your models here.
#Los usuarios seran los que creen sus post o realicen comentarios de los post
class Usuario(models.Model):
    id = models.AutoField(unique=True)
    nombre = models.CharField(max_length=40)
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    lastlogin = models.DateTimeField()
    dateregistro = models.DateTimeField()
    datecupleanho = models.DateTimeField()
    estado = models.models.IntegerField()
    
#Existen categorias de post
class Categoria(models.Model):
    id = models.AutoField(unique=True)
    nombre = models.CharField(max_length=40)
    parent = models.IntegerField()
    
#Post que publicaran los usuarios
class Post(models.Model):
    id = models.AutoField(unique=True)
    UserID = models.IntegerField()
    titulo = models.CharField(max_length=40)
    body = models.CharField()
    category = models.IntegerField()
    tags = models.IntegerField()
    fechapublicacion = models.DateField()
    ultimaactualizacion = models.DateField()
    imagen = models.CharField() #   ----- VER COMO SUBIR FOTOS ----
    estado = models.IntegerField() #inicio - publicado - baneado
    
    
#Recordatorios para hacer mas facil la busqueda
class Tags(models.Model):
    id = models.AutoField(unique=True)
    tag = models.CharField()
    Relacion = models.CharField()
    
#Comentarios que realizaran los usuarios sobre los post
class Comentarios(models.Model):
    id = models.AutoField()
    UserId = models.IntegerField()
    PostId = models.IntegerField()   
    Titulo = models.CharField()
    fecha = models.DateField()

#Estados en los cuales puede estar el usuario 
#Activo - Inactivo - Bloqueado - Eliminado ...
class Estado(models.Model):
    id = models.AutoField(unique=True)
    nombre = models.CharField()
    