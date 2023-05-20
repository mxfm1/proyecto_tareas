from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label='Primer Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.CharField(label='E-mail')
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'placeholder':'Contraseña...'}))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(attrs={'placeholder':'Confirma tu contraseña...'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        
class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password',widget=forms.PasswordInput)
