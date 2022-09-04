from django.urls import path

from AppBlog.views import *

urlpatterns = [
    path('', inicio, name='AppBlogInicio'),
    #path('BlogNew/', BlogCRUD, name='AppBlogCrud'),
    #path('blogBuscar/', BlogBuscar, name='AppBlogBuscar'),
   # path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
   # path('busqueda_camada/', busqueda_camada, name='AppCoderBusquedaCamada'),
   # path('busqueda_camada_post/', busqueda_camada_post, name='AppCoderBusquedaCamadaPost'),
   # path('eliminar_curso/<int:camada>', eliminar_curso, name='AppCoderEliminarCurso'),
   # path('editar_curso/<int:camada>', editar_curso, name='AppCoderEditarCurso'),
]
