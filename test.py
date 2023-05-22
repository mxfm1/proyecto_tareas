#Forms
class CrearTareasform(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=Estados.objects.all())
    etiqueta = forms.ModelChoiceField(queryset=Etiqueta.objects.all())
    fecha_vencimiento = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    usuario = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Tareas
        fields = ['titulo','descripcion','fecha_vencimiento','estado','etiqueta','usuario'] 
        
    def save(self,commit=True):
        tarea = super().save(commit=False)
        # estado_nombre = self.cleaned_data.get('estado')
        # estado = Estados.objects.get(estado=estado_nombre)
        # tarea.estado = estado 
        
        # etiqueta_nombre = self.cleaned_data.get('nombre_etiqueta')
        # et_name = Etiqueta.objects.get(nombre_etiqueta=etiqueta_nombre)
        # tarea.nombre_etiqueta = et_name
        tarea.etiqueta = self.cleaned_data['etiqueta']
        tarea.estado = self.cleaned_data['estado']
        tarea.usuario_id = self.cleaned_data['usuario'].id
        print(self.cleaned_data)
        print(tarea)
        print(tarea.usuario_id)
        if commit:
            tarea.save()
        return tarea
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'usuario': self.request.user}
        return kwargs   
    
#Views 

class CrearTarea(LoginRequiredMixin,CreateView):
    model = Tareas
    form_class = CrearTareasform
    template_name = 'accounts/crear_tarea.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):  
        form.instance.usuario_id = self.request.user.id   
        print(f'form isntance: {form.instance}')
        print(f'form isntance usuario: {form.instance.usuario}')
        print(f'request: {self.request.user}')
        return super().form_valid(form)
    
# Urls

path('tareas/crear',CrearTarea.as_view(),name='crear_tarea'),