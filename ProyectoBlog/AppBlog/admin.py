from django.contrib import admin

from AppBlog.models import Usuario, Categoria, Post, Tag, Comentario, Estado




# Register your models here.
admin.site.register(Usuario)
admin.site.register(Categoria) 
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comentario)
admin.site.register(Estado)
