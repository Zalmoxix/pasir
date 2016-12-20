from django.contrib import admin
from .models import *
from .forms import GrupoForm

class GrupoAdmin(admin.ModelAdmin):
    form = GrupoForm

admin.site.register(Version)
admin.site.register(Imagen)
admin.site.register(Equipo)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Script)
admin.site.register(Log)


