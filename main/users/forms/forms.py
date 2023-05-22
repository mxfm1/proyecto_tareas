from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from ..models import Etiqueta, Estados, Tareas

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

# class CrearTareasForm(forms.ModelForm):
#     estado = forms.ChoiceField(choices=Estados.ESTADO_CHOICES)
#     etiqueta = forms.ChoiceField(choices=Etiqueta.ETIQUETA_CHOICES)
#     usuario = forms.CharField(widget=forms.HiddenInput)
    
#     class Meta:
#         model = Tareas
#         fields = ['titulo','descripcion','fecha_vencimiento','estado','etiqueta','usuario']
    
#     def save(self,commit=True):
#         tarea = super().save(commit=False)
#         # estado_pendiente = Estados.objects.get(estado='pendiente')
#         # tarea.estado = estado_pendiente
#         tarea.usuario_id = self.cleaned_data['usuario']
#         print(self.cleaned_data)
#         print(tarea)
#         print(tarea.usuario_id)
#         if commit:
#             tarea.save()
#         return tarea

class CrearTareasForm(forms.ModelForm):
    
    fecha_vencimiento = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    estado = forms.ModelChoiceField(queryset=Estados.objects.all())
    etiqueta = forms.ModelChoiceField(queryset=Etiqueta.objects.all())
    
    class Meta:
        model = Tareas
        fields = ['titulo','descripcion','fecha_vencimiento','estado','etiqueta']
        
    def save(self,commit=True):
        tarea = super().save(commit=False)
        if commit:
            tarea.save()
        return tarea
    

    
    