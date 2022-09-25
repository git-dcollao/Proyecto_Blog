from django.contrib import admin

from AppBlog.models import Usuario, Categoria, Post, Tags, Comentarios, Estado



# Register your models here.
admin.site.register(Usuario)
admin.site.register(Categoria) 
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Comentarios)
admin.site.register(Estado)
