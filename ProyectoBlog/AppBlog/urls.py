from django.urls import path

from AppBlog.views import * 
#usuario, tags, categoria, post, comentarios

urlpatterns = [
    path('', inicio, name='AppBlogInicio'),
    path('usuario/', usuario, name='AppBlogUsuario'),
    path('tags/', tags, name='AppBlogTags'),
    path('categoria/', categoria, name='AppBlogCategoria'),
    path('post/', post, name='AppBlogPost'),
    path('comentarios/', comentarios, name='AppBlogComentarios'),
    path('usuario_formulario/', usuario_formulario, name='AppBlogUsuarioFormulario'),
    path('busqueda_usuario/', busqueda_usuario, name='AppBlogBusquedaUsuario'),
    path('busqueda_usuario_post/', busqueda_usuario_post, name='AppBlogBusquedaUsuarioPost'),
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
