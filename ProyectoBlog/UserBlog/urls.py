
from django.contrib.auth.views import LogoutView
from django.urls import path

from UserBlog.views import *

urlpatterns = [
    path('login/', login_request, name='UserBlogLogin'),
    path('registro/', register, name='UserBlogRegister'),
    path('logout/', LogoutView.as_view(template_name='UserBlog/logout.html'), name='UserBlogLogout'),
    path('editar/', editar_usuario, name='UserBlogEditar'),
    path('avatar/', upload_avatar, name='UserBlogAvatar'),
]
