from django import forms 

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
    #id_categoria = forms.IntegerField(unique=True)
    nombre = forms.CharField(max_length=40)
    parent = forms.IntegerField()
    
class PostForm(forms.Form):
    #id_post = forms.IntegerField(unique=True)
    autor = forms.IntegerField()
    titulo = forms.CharField(max_length=200)
    body = forms.Textarea()
    category = forms.IntegerField()
    tags = forms.IntegerField()
    fechapublicacion = forms.DateField()
    ultimaactualizacion = forms.DateField()
    imagen = forms.CharField(max_length=200) #   ----- VER COMO SUBIR FOTOS ----
    estado = forms.IntegerField() #inicio - publicado - baneado
    
class TagsForm(forms.Form):
    #id_tags = forms.IntegerField(unique=True)
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
class BusquedaUsuarioForms(forms.Form):
    usuario = forms.CharField()
    