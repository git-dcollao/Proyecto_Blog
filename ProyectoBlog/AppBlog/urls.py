from django.contrib import admin
from django.conf.urls.static import static
from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path, include
from . import views

from AppBlog.views import *

#usuario, tags, categoria, post, comentarios, estado
urlpatterns = [
    path('', inicio, name='AppBlogInicio'),
    path('aboutme.html', views.aboutme, name='AppBlogAboutme'),
    path('contacto.html', views.contacto, name='AppBlogContacto'),
    
    path('usuario/', usuario, name='AppBlogUsuario'),
    path('usuario_formulario/', usuario_formulario, name='AppBlogUsuarioFormulario'),
    path('busqueda_usuario/', busqueda_usuario, name='AppBlogBusquedaUsuario'),
    path('busqueda_usuario_post/', busqueda_usuario_post, name='AppBlogBusquedaUsuarioPost'),
    
    
    path('post/<int:id>', busqueda_post, name='AppBlogBusquedaPost'),
    path('post_categoria/<int:id>/<str:nombre>', busqueda_post_categoria, name='AppBlogPostCategoria'),
    
    path('post/', post, name='AppBlogPost'),
    path('post_formulario/', post_formulario, name='AppBlogPostFormulario'),
    path('tag_formulario/', tag_formulario, name='AppBlogTagFormulario'),
    
    path('categoria/', categoria, name='AppBlogCategoria'), # sirve para modificar
    path('categoria_formulario/', categoria_formulario, name='AppBlogCategoriaFormulario'),
    path('busqueda_categoria/', busqueda_categoria, name='AppBlogBusquedaCategoria'),
    path('busqueda_categoria_post/', busqueda_categoria_post, name='AppBlogBusquedaCategoriaPost'),
    path('editar_categoria/<int:id_categoria>', editar_categoria, name='AppBlogEditarCategoria'),
    path('eliminar_categoria/<int:id_categoria>', eliminar_categoria, name='AppBlogEliminarCategoria'),
    
    #path('busqueda_estado/', busqueda_estado, name='AppBlogBusquedaEstado'),
    path('estado/', estado, name='AppBlogEstado'),
    path('estado_formulario/', estado_formulario, name='AppBlogEstadoFormulario'),
    path('editar_estado/<str:nombre>', editar_estado, name='AppBlogEditarEstado'),
    path('eliminar_estado/<str:nombre>', eliminar_estado, name='AppBlogEliminarEstado'),
    
    path('comentarios/', comentarios, name='AppBlogComentarios'),
    
    
    
   # path('tag_formulario/', tag_formulario, name='AppBlogTagFormulario'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)