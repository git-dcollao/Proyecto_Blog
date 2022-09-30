from distutils.command.clean import clean
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from UserBlog.forms import UserRegisterForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
    
        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'Porfavor verificar usuario o conrtasenia!')
        else:
            messages.info(request, 'Inicio de sesion fallido!')
        
        return redirect('AppBlogInicio')
            
    contexto = {
        'form' : AuthenticationForm()
        ,'titulo_form' : 'Login'
        ,'boton_envio' : 'Enviar'
    }
    
    return render(request, 'base_formulario.html', contexto)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.post, request.FILES)
        
        if form.is_valid():
            user = form.save()
            
            #avatar = Avatar(user=user, imagen=form.cleaned_data.get('imagen'))
            #avatar.save()
            
            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
            
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado!')
            
        return redirect('AppBlogInicio')
    
    contexto = {
        #'form': UserCreationForm(),
        'form': UserRegisterForm(), 
        'nombre_form': 'Registro'
    }
    
    return render(request, 'UserBlog/login.html', contexto)

@login_required
def editar_usuario(request):
    usuario = request.user
    
    form = UserRegisterForm(request.POST)
    
    if form.is_valid():
        
        data = form.cleaned_data
        
        usuario.username = data.get('username')
        usuario.email = data.get('email')
        usuario.last_name = data.get('last_name')
        
        usuario.save()
        
        messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
            
    else:
        messages.info(request, 'Tu usuario no pudo ser registrado!')
            
    return redirect('AppBlogInicio')
    
    contexto = {
        'form': UserRegisterForm(
            initial={
                'username': usuario.username,
                'email': usuario.email,
                'last_name': usuario.last_name
                }),
        'boton_envio': 'Registro',
    }

    return render(request, 'base_formulario.html', contexto)

    