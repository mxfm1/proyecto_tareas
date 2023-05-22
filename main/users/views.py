import datetime
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView 
from django.views.generic.detail import DetailView
from .models import Tareas,User

from .forms.forms import CreateUserForm,LoginForm,CrearTareasForm
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages


#Vista que controla las tareas desplegadas del usuario
@login_required
def home(request):

    tipo_tareas = request.GET.get('tipo_tareas')
    user = request.user.id
    
    tareas = Tareas.objects.filter(usuario_id=user,estado__estado='pendiente').order_by('fecha_vencimiento')
    
    # if tipo_tareas == 'todas':
    #     tareas = Tareas.objects.filter(usuario_id=user).order_by('-fecha_vencimiento')    
    # if tipo_tareas == 'pendiente':
    #     tareas = tareas.filter(estado__estado='pendiente').order_by('-fecha_vencimiento')
    # elif tipo_tareas == 'en progreso':
    #     tareas = Tareas.objects.filter(usuario_id=user,estado__estado='en progreso')
    # elif tipo_tareas == 'completado':
    #     tareas = Tareas.objects.filter(usuario_id=user,estado__estado='completado')
    context = {'tareas':tareas}
    return render(request, 'accounts/home.html', context=context)

class DetalleTarea(View):
    template_name = 'accounts/detalle_tarea.html'
    
    def get(self,request,pk):
        tarea = get_object_or_404(Tareas,pk=pk)
        context = {'tarea':tarea}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        tarea = get_object_or_404(Tareas,pk=pk)
        accion = request.POST.get('accion')
        if accion == 'borrar':
            tarea.delete()
            return redirect('home')
        return render(request,self.template_name,{'tarea':tarea})
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            user = form.cleaned_data.get('username')
            messages.success(request, 'Usuario ' + user + ' fue creado exitosamente.')
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
    return redirect('login')

@login_required(login_url='login')
def tareas(request):
    context = {'request':request}
    return render(request,'site/task.html',context)

# class CrearTarea(LoginRequiredMixin, CreateView):
#     model = Tareas
#     form_class = CrearTareasForm
#     template_name = 'accounts/crear_tarea.html'
#     success_url = reverse_lazy('home')
    
#     def form_valid(self,form):
#         form.instance.usuario = self.request.user.id
#         print(f'form isntance: {form.instance}')
#         print(f'form isntance usuario: {form.instance.usuario}')
#         print(f'request: {self.request.user}')
#         return super().form_valid(form)

class CrearTarea(LoginRequiredMixin,CreateView):
    model = Tareas
    form_class = CrearTareasForm
    template_name = 'accounts/crear_tarea.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    