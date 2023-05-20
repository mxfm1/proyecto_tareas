from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms.forms import CreateUserForm,LoginForm
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request,'accounts/home.html')

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            user = form.cleaned_data.get('username')
            messages.success(request, 'Usuario ' + user + 'fue creado exitosamente.')
            return redirect('login')
    context = {'form':form}
    return render(request,'accounts/register.html',context)

def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Usuario o contraseña incorrectas. ')
    form = LoginForm()    
    context = {'form':form}
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def tareas(request):
    context = {'request':request}
    return render(request,'site/task.html',context)