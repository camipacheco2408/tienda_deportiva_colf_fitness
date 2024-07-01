from django.urls import path, include
from colf.views import *

urlpatterns = [
    path('', home, name= "home"),
    path('indumentaria/', indumentaria, name="indumentaria"),
    path('maqmusculacion/', maqmusculacion, name="maqmusculacion"),
    path('maqcardio/', maqcardio, name="maqcardio"),
    path('accesorios/', accesorios, name="accesorios"),
    
#____ Formularios
    path('agregaraccesorios/', agregarmaqmusculacion, name="agregaraccesorios"),
    path('agregarindumentaria/', agregarindumentaria, name="agregarindumentaria"),
    path('agregarmaqcardio/', agregarmaqcardio, name="agregarmaqcardio"),
    path('agregarmaqmusculacion/', agregarmaqmusculacion, name="agregarmaqmusculacion"),

    path('buscar_indumentaria/', buscar_indumentaria, name="buscar_indumentaria"),
    path('encontrarIndumentaria/', encontrarIndumentaria, name="encontrarIndumentaria"),
]


