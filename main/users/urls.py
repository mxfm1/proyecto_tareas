from django.urls import path
from .views import registerPage,loginPage,home,logoutUser,tareas

urlpatterns = [
    path('home/',home,name='home'),
    path('register/',registerPage,name='registro'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('tareas/',tareas,name='tareas')
]
