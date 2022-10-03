from django.urls import path
from . import views

from AppBlog.views import *
#usuario, tags, categoria, post, comentarios, estado
urlpatterns = [
    path('', inicio, name='AppBlogInicio'),
    path('aboutme.html', views.aboutme, name='AppBlogAboutme'),
    path('contacto.html', views.contacto, name='AppBlogContacto'),
    path('usuario/', usuario, name='AppBlogUsuario'),
    path('estado/', estado, name='AppBlogEstado'),
    
    
    path('tags/', tags, name='AppBlogTags'),
    path('categoria/', categoria, name='AppBlogCategoria'),
    path('post/', post, name='AppBlogPost'),
    path('comentarios/', comentarios, name='AppBlogComentarios'),
    path('usuario_formulario/', usuario_formulario, name='AppBlogUsuarioFormulario'),
    path('categoria_formulario/', categoria_formulario, name='AppBlogCategoriaFormulario'),
    path('tag_formulario/', tag_formulario, name='AppBlogTagFormulario'),
    path('busqueda_usuario/', busqueda_usuario, name='AppBlogBusquedaUsuario'),
    path('busqueda_usuario_post/', busqueda_usuario_post, name='AppBlogBusquedaUsuarioPost'),
    path('estado_formulario/', estado_formulario, name='AppBlogEstadoFormulario'),
    path('eliminar_estado/<str:nombre>', eliminar_estado, name='AppBlogEliminarEstado'),
    path('editar_estado/<str:nombre>', editar_estado, name='AppBlogEditarEstado')
    
    
   # path('categoria_formulario/', categoria_formulario, name='AppBlogCategoriaFormulario'),
   # path('tags_formulario/', tags_formulario, name='AppBlogTagsFormulario'),    
    #path('BlogNew/', BlogCRUD, name='AppBlogCrud'),
    #path('blogBuscar/', BlogBuscar, name='AppBlogBuscar'),
   # path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
   # path('busqueda_camada/', busqueda_camada, name='AppCoderBusquedaCamada'),
   # path('busqueda_camada_post/', busqueda_camada_post, name='AppCoderBusquedaCamadaPost'),
   # path('eliminar_curso/<int:camada>', eliminar_curso, name='AppCoderEliminarCurso'),
   # path('editar_curso/<int:camada>', editar_curso, name='AppCoderEditarCurso'),
]
