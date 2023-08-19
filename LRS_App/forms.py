from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UploadedFile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1' ,'password2','email','first_name','last_name' )

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'file','filetype']