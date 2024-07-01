from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "categorias/index.html")

def indumentaria(request):
    contexto = {"indumentaria": Indumentaria.objects.all()}
    return render(request, "categorias/indumentaria.html", contexto)

def maqmusculacion(request):
    contexto = {"maqmusculacion": Maqmusculacion.objects.all()}
    return render(request, "categorias/maqmusculacion.html", contexto)

def maqcardio(request):
    contexto = {"maqcardio": Maqcardio.objects.all()}
    return render(request, "categorias/maqcardio.html", contexto)

def accesorios(request):
    contexto = {"accesorios": Accesorios.objects.all()}
    return render(request, "categorias/accesorios.html", contexto)

#Formularios

#Agregar Accesorios
def agregaraccesorios(request):
    if request.method == "POST":
        miForm = formsAccesorios(request.POST)
        if miForm.is_valid():
            accesorio_nombre = miForm.cleaned_data.get("nombre")
            accesorio_tipo = miForm.cleaned_data.get("tipo")
            accesorio_precio = miForm.cleaned_data.get("precio")
            accesorio_descripcion = miForm.cleaned_data.get("descripcion")
            accesorio = Accesorios(nombre=accesorio_nombre, tipo=accesorio_tipo, precio=accesorio_precio, descripcion=accesorio_descripcion)
            accesorio.save()
            contexto = {"accesorios": Accesorios.objects.all() }
            return render(request, "categorias/accesorios.html", contexto)
    else:
        miForm = formsAccesorios()
    
    return render(request, "categorias/agregaraccesorios.html", {"form": miForm})

#Agregar Indumentaria
def agregarindumentaria(request):
    if request.method == "POST":
        miForm = formsIndumentaria(request.POST)
        if miForm.is_valid():
            indumentaria_nombre = miForm.cleaned_data.get("nombre")
            indumentaria_tipo = miForm.cleaned_data.get("tipo")
            indumentaria_precio = miForm.cleaned_data.get("precio")
            indumentaria_descripcion = miForm.cleaned_data.get("descripcion")
            indumentaria = Indumentaria(nombre=indumentaria_nombre, 
                                            tipo=indumentaria_tipo, precio=indumentaria_precio,
                                            descripcion=indumentaria_descripcion)
            indumentaria.save()
            contexto = {"indumentaria": Indumentaria.objects.all() }
            return render(request, "categorias/indumentaria.html", contexto)
    else:
        miForm = formsIndumentaria()
    
    return render(request, "categorias/agregarindumentaria.html", {"form": miForm})

#Agregar Maquinas Cardio
def agregarmaqcardio(request):
    if request.method == "POST":
        miForm = formsMaqcardio(request.POST)
        if miForm.is_valid():
            maqcardio_nombre = miForm.cleaned_data.get("nombre")
            maqcardio_tipo = miForm.cleaned_data.get("tipo")
            maqcardio_precio = miForm.cleaned_data.get("precio")
            maqcardio_descripcion = miForm.cleaned_data.get("descripcion")
            maqcardio = Maqcardio(nombre=maqcardio_nombre, tipo=maqcardio_tipo, precio=maqcardio_precio, descripcion=maqcardio_descripcion)
            maqcardio.save()
            contexto = {"maqcardio": Maqcardio.objects.all() }
            return render(request, "categorias/maqcardio.html", contexto)
    else:
        miForm = formsMaqcardio()
    
    return render(request, "categorias/agregarmaqcardio.html", {"form": miForm})

#Agregar Maquinas de Musculacion
def agregarmaqmusculacion(request):
    if request.method == "POST":
        miForm = formsMaqmusculacion(request.POST)
        if miForm.is_valid():
            maqmusculacion_nombre = miForm.cleaned_data.get("nombre")
            maqmusculacion_tipo = miForm.cleaned_data.get("tipo")
            maqmusculacion_precio = miForm.cleaned_data.get("precio")
            maqmusculacion_descripcion = miForm.cleaned_data.get("descripcion")
            maqmusculacion = Maqmusculacion(nombre=maqmusculacion_nombre, tipo=maqmusculacion_tipo, precio=maqmusculacion_precio, descripcion=maqmusculacion_descripcion)
            maqmusculacion.save()
            contexto = {"maqmusculacion": Maqmusculacion.objects.all() }
            return render(request, "categorias/maqmusculacion.html", contexto)
    else:
        miForm = formsMaqmusculacion()
    
    return render(request, "categorias/agregarmaqmusculacion.html", {"form": miForm})

#Buscar Indumentaria
def buscar_indumentaria(request):
    return render(request, "categorias/buscar_indumentaria.html")

def encontrarIndumentaria(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        indumentaria = Indumentaria.objects.filter(nombre__icontains=patron)
        contexto = {'indumentaria': indumentaria}    
    else:
        contexto = {'indumentaria': Indumentaria.objects.all()}
        
    return render(request, "categorias/indumentaria.html", contexto)

