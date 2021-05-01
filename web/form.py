from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog,ProfileImg

from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserProfile(ModelForm):
    class Meta:
        model = ProfileImg
        fields = '__all__'
        exclude = ['user']


class Useredit(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class PostBlog(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['user']