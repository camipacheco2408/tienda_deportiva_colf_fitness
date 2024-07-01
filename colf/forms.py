from django import forms

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
    