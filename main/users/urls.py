from django.urls import path
from .views import registerPage,loginPage,home,logoutUser,tareas,CrearTarea, DetalleTarea,ActualizarTarea

urlpatterns = [
    path('home/',home,name='home'),
    path('register/',registerPage,name='registro'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('tareas/',tareas,name='tareas'),
    path('tareas/crear',CrearTarea.as_view(),name='crear_tarea'),
    path('tareas/<int:pk>',DetalleTarea.as_view(),name='detalle_tarea'),
    path('tareas/actualizar/<int:pk>',ActualizarTarea.as_view(),name='actualizar_tarea'),
]
