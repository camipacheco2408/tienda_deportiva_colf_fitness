from django.shortcuts import render, redirect
from .models import *
from .forms import *
#______
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

#______
from django.urls import reverse_lazy

#______
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

#______
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect



# Vistas
#___ Home
def home(request):
    return render(request, "categorias/index.html")

#___ Acerca de Colf Fitness
def acerca(request):
    return render(request, "categorias/acerca.html")

@login_required


#_______ Indumentaria
def indumentaria(request):
    contexto = {"indumentaria": Indumentaria.objects.all()}
    return render(request, "categorias/indumentaria.html", contexto)

    #_____ Create, Update, Delete
    
    
def es_administrador(user):
    return user.is_superuser
    
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class IndumentariaCreate(CreateView):
    model = Indumentaria
    form_class = IndumentariaForm
    template_name = 'categorias/indumentaria_form.html'
    success_url = reverse_lazy('indumentaria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class IndumentariaUpdate(UpdateView):
    model = Indumentaria
    form_class = IndumentariaForm
    template_name = 'categorias/indumentaria_form.html'
    success_url = reverse_lazy('indumentaria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class IndumentariaDelete(DeleteView):
    model = Indumentaria
    success_url = reverse_lazy('indumentaria')
    template_name = 'categorias/indumentaria_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'delete'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

        #Buscar Indumentaria
        
@login_required
def buscar_indumentaria(request):
    return render(request, "categorias/buscar_indumentaria.html")

@login_required
def encontrarIndumentaria(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        indumentaria = Indumentaria.objects.filter(nombre__icontains=patron)
        contexto = {'indumentaria': indumentaria}    
    else:
        contexto = {'indumentaria': Indumentaria.objects.all()}
        
    return render(request, "categorias/list_indumentaria.html", contexto)


#____________________________________ Accesorios________________________________________________________
def es_administrador(user):
    return user.is_superuser

def accesorios(request):
    contexto = {"accesorios": Accesorios.objects.all()}
    return render(request, "categorias/accesorios.html", contexto)

    #_____ Create, Update, Delete

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class AccesorioCreate(CreateView):
    model = Accesorios
    form_class = AccesoriosForm
    template_name = 'categorias/accesorio_form.html'
    success_url = reverse_lazy('accesorios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class AccesorioUpdate(UpdateView):
    model = Accesorios
    form_class = AccesoriosForm
    template_name = 'categorias/accesorio_form.html'
    success_url = reverse_lazy('accesorios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class AccesorioDelete(DeleteView):
    model = Accesorios
    template_name = 'categorias/accesorio_confirm_delete.html'
    success_url = reverse_lazy('accesorios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'delete'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

# Vista para buscar accesorios
@login_required
def buscar_accesorios(request):
    return render(request, "categorias/buscar_accesorios.html")

@login_required
def encontrar_accesorios(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        accesorios = Accesorios.objects.filter(nombre__icontains=patron)
        contexto = {'accesorios': accesorios}    
    else:
        contexto = {'accesorios': Accesorios.objects.all()}
        
    return render(request, "categorias/list_accesorios.html", contexto)

#__________________________Maquinas de Musculacion______________________________

def es_administrador(user):
    return user.is_superuser


def maqmusculacion(request):
    contexto = {"maqmusculacion": Maqmusculacion.objects.all()}
    return render(request, "categorias/maqmusculacion.html", contexto)

    #_____ Create, Update, Delete

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class MaqMusculacionCreate(CreateView):
    model = Maqmusculacion
    form_class = MaqMusculacionForm
    template_name = 'categorias/maqmusculacion_form.html'
    success_url = reverse_lazy('maqmusculacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class MaqMusculacionUpdate(UpdateView):
    model = Maqmusculacion
    form_class = MaqMusculacionForm
    template_name = 'categorias/maqmusculacion_form.html'
    success_url = reverse_lazy('maqmusculacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class MaqMusculacionDelete(DeleteView):
    model = Maqmusculacion
    template_name = 'categorias/maqmusculacion_confirm_delete.html'
    success_url = reverse_lazy('maqmusculacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'delete'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('maqmusculacion')

# Vista para buscar Maqmusculacion
@login_required
def buscar_maqmusculacion(request):
    return render(request, "categorias/buscar_maqmusculacion.html")

@login_required
def encontrar_maqmusculacion(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        maqmusculacion = Maqmusculacion.objects.filter(nombre__icontains=patron)
        contexto = {'maqmusculacion': maqmusculacion}    
    else:
        contexto = {'maqmusculacion': Maqmusculacion.objects.all()}
        
    return render(request, "categorias/list_maqmusculacion.html", contexto)

#__________________________Maquinas de Cardio______________________________
def es_administrador(user):
    return user.is_superuser

def maqcardio(request):
    contexto = {"maqcardio": Maqcardio.objects.all()}
    return render(request, "categorias/maqcardio.html", contexto)

#_____ Create, Update, Delete

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class MaqCardioCreate(CreateView):
    model = Maqcardio
    form_class = MaqCardioForm
    template_name = 'categorias/maqcardio_form.html'
    success_url = reverse_lazy('maqcardio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class MaqCardioUpdate(UpdateView):
    model = Maqcardio
    form_class = MaqCardioForm
    template_name = 'categorias/maqcardio_form.html'
    success_url = reverse_lazy('maqcardio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_administrador), name='dispatch')
class MaqCardioDelete(DeleteView):
    model = Maqcardio
    template_name = 'categorias/maqcardio_confirm_delete.html'
    success_url = reverse_lazy('maqcardio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'delete'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('maqcardio')

# Vista para buscar Maqmusculacion
@login_required
def buscar_maqcardio(request):
    return render(request, "categorias/buscar_maqcardio.html")

@login_required
def encontrar_maqcardio(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        maqcardio = Maqcardio.objects.filter(nombre__icontains=patron)
        contexto = {'maqcardio': maqcardio}    
    else:
        contexto = {'maqcardio': Maqcardio.objects.all()}
        
    return render(request, "categorias/list_maqcardio.html", contexto)




#___________________________________Login/logout/regitracion___________________________________________________

def loginRequest(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, request.POST)
        if miForm.is_valid():
            usuario = request.POST["username"]
            clave = request.POST["password"]
            user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            # avatar
            try:
                avatar = Avatar.objects.get(user=user).imagen.url
            except Avatar.DoesNotExist:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #_________
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy("login"))
    else:
            miForm = AuthenticationForm()
    return render(request, "categorias/login.html",{"form": miForm})

#____ 
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            user = miForm.cleaned_data.get("username")
            if User.objects.filter(username=user).exists():
                miForm.add_error(
                    "username", "Nombre de usuario no se encuentra disponible."
                )
            else:
                miForm.save()
                return redirect(reverse_lazy("home"))
    else:
            miForm = RegistroForm()
    return render(request, "categorias/registro.html",{"form":miForm})

# Edicion de Perfil/ Avatar
@login_required
def editarProfile(request):
    usuario = request.user

    if request.method == "POST":
        miForm = UserEditForm(request.POST, instance=usuario)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy("home"))  
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, "categorias/editarPerfil.html", {"form": miForm})
    
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "categorias/cambiar_clave.html"
    success_url = reverse_lazy("home")
    
    
    
@login_required  
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = request.user
            imagen = miForm.cleaned_data["imagen"]
            # Eliminar avatares antiguos del usuario
            avatarViejo = Avatar.objects.filter(user=usuario)
            if avatarViejo.exists():
                avatarViejo.delete()
            # Guardar el nuevo avatar
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            
            # Actualizar el avatar en la sesión del usuario
            imagen_url = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen_url
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    
    return render(request, "categorias/agregarAvatar.html", {"form": miForm})