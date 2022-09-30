from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from UserBlog.forms import UserRegisterForm 

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