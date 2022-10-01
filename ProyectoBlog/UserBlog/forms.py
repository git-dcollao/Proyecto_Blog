
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from UserBlog.models import Avatar


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"
    
   # return render (request, 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'last_name')
