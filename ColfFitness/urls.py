<<<<<<< HEAD
"""
URL configuration for ColfFitness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('colf.urls'))
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
#____ Home
    path('', home, name= "home"),

#____ Acerca    
    path('acerca/', acerca, name="acerca"),
    
#____ Indumentaria 
        #____ CRUD
    path('indumentaria/', indumentaria, name="indumentaria"),
    path('create/', IndumentariaCreate.as_view(), name='indumentaria_create'),
    path('update/<int:pk>/', IndumentariaUpdate.as_view(), name='indumentaria_update'),
    path('delete/<int:pk>/', IndumentariaDelete.as_view(), name='indumentaria_delete'),
        #____ buscar Indumentaria
    path('buscar_indumentaria/', buscar_indumentaria, name="buscar_indumentaria"),
    path('encontrarIndumentaria/', encontrarIndumentaria, name="encontrar_indumentaria"),
    
    
    #____ accesorios
    path('accesorios/', accesorios, name="accesorios"),  
    path('accesorios/create/', AccesorioCreate.as_view(), name='accesorios_create'),
    path('accesorios/<int:pk>/update/', AccesorioUpdate.as_view(), name='accesorios_update'),
    path('accesorios/<int:pk>/delete/', AccesorioDelete.as_view(), name='accesorios_delete'),
    path('buscar_accesorios/', buscar_accesorios, name='buscar_accesorios'),
    path('encontrar_accesorios/', encontrar_accesorios, name='encontrar_accesorios'),


    #____ Maquinas de musculacion
    path('maqmusculacion/', maqmusculacion, name="maqmusculacion"),
    path('maqmusculacion/create/', MaqMusculacionCreate.as_view(), name='maqmusculacion_create'),
    path('maqmusculacion/<int:pk>/update/', MaqMusculacionUpdate.as_view(), name='maqmusculacion_update'),
    path('maqmusculacion/<int:pk>/delete/', MaqMusculacionDelete.as_view(), name='maqmusculacion_delete'),
    path('buscar_maqmusculacion/', buscar_maqmusculacion, name='buscar_maqmusculacion'),
    path('encontrar_maqmusculacion/', encontrar_maqmusculacion, name='encontrar_maqmusculacion'),



    #____ Maquinas de Cardio
    path('maqcardio/', maqcardio, name="maqcardio"),
    path('maqcardio/create/', MaqCardioCreate.as_view(), name='maqcardio_create'),
    path('maqcardio/<int:pk>/update/', MaqCardioUpdate.as_view(), name='maqcardio_update'),
    path('maqcardio/<int:pk>/delete/', MaqCardioDelete.as_view(), name='maqcardio_delete'),
    path('buscar_maqcardio/', buscar_maqcardio, name='buscar_maqcardio'),
    path('encontrar_maqcardio/', encontrar_maqcardio, name='encontrar_maqcardio'),


    #____ Seccion Login-Logout-Registro
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="categorias/logout.html"), name="logout"),
    path('registro/', register, name="registro"),  


    #____ Edicion de Perfil / Avatar
    path('perfil/', editarProfile, name="perfil"),
    path('cambiar_clave/', CambiarClave.as_view(), name='cambiar_clave'),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]


>>>>>>> 18882607a11a899b06f689ec6aeb5fd28bb4a7c3
