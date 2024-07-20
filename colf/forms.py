from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


# Indumentaria deportiva
class formsIndumentaria(forms.Form):
    nombre=forms.CharField(max_length=80, required=True)
    tipo=forms.CharField(max_length=60, required=True)
    precio=forms.IntegerField(required=True)
    descripcion=forms.CharField()
    
    
# Maquinas de Musculacion
class formsMaqmusculacion(forms.Form):
    nombre=forms.CharField(max_length=80, required=True)
    tipo=forms.CharField(max_length=60, required=True)
    precio=forms.IntegerField(required=True)
    descripcion=forms.CharField()
    

# Maquinas de Cardio
class formsMaqcardio(forms.Form):
    nombre=forms.CharField(max_length=80, required=True)
    tipo=forms.CharField(max_length=60, required=True)
    precio=forms.IntegerField(required=True)
    descripcion=forms.CharField()
    
    
# Accesorios de gimnasio
class formsAccesorios(forms.Form):
    nombre=forms.CharField(max_length=80, required=True)
    tipo=forms.CharField(max_length=60, required=True)
    precio=forms.IntegerField(required=True)
    descripcion=forms.CharField()
    
# Login

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
    
class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Correo electrónico')
    first_name = forms.CharField(label='Nombre', max_length=100)
    last_name = forms.CharField(label='Apellido', max_length=100)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        
class IndumentariaForm(forms.ModelForm):
    class Meta:
        model = Indumentaria
        fields = ['nombre', 'tipo', 'descripcion', 'precio', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class': 'form-control-file', 'id': 'id_imagen'})
        
        
class AccesoriosForm(forms.ModelForm):
    class Meta:
        model = Accesorios
        fields = ['nombre', 'tipo', 'descripcion', 'precio', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class': 'form-control-file', 'id': 'id_imagen'})
        
        
class MaqMusculacionForm(forms.ModelForm):
    class Meta:
        model = Maqmusculacion
        fields = ['nombre', 'tipo', 'descripcion', 'precio', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class': 'form-control-file', 'id': 'id_imagen'})
        
class MaqCardioForm(forms.ModelForm):
    class Meta:
        model = Maqcardio
        fields = ['nombre', 'tipo', 'descripcion', 'precio', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class': 'form-control-file', 'id': 'id_imagen'})
        