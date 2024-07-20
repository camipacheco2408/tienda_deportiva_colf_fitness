from django.contrib import admin

# Register your models here.
from .models import *

class accesoriosAdmin(admin.ModelAdmin):
    list_display =("nombre", "tipo", "precio", "descripcion")
    list_filter = ("nombre","tipo")
    
    
class indumentariaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "precio", "descripcion")
    list_filter = ("nombre","tipo")
    
class maqcadioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "precio", "descripcion")
    list_filter = ("nombre","tipo")
    
class maqmusculacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "precio", "descripcion")
    list_filter = ("nombre","tipo")
    
admin.site.register(Accesorios, accesoriosAdmin)
admin.site.register(Indumentaria, indumentariaAdmin)
admin.site.register(Maqcardio, maqcadioAdmin)
admin.site.register(Maqmusculacion, maqmusculacionAdmin)
