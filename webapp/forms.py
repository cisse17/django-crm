from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

from django.contrib.auth.forms import AuthenticationForm

from django import forms

# inscription/ user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# connexion user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class AjoutInfosClient(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
                'prenom', 
                  'nom', 
                  'email', 
                  'telephone', 
                  'adresse',
                  'ville', 
                  'province', 
                  'pays' ]
        

class ModifierInfosClient(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
                'prenom', 
                  'nom', 
                  'email', 
                  'telephone', 
                  'adresse',
                  'ville', 
                  'province', 
                  'pays' ]

# pip install django-crispy-forms==1.14.0