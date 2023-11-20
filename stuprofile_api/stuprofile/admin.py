from django.contrib import admin
from .models import Competencia, Materia, Docente, Bloom

# Register your models here.

# Registre os modelos no admin
admin.site.register(Competencia)
admin.site.register(Materia)
admin.site.register(Docente)
class BloomAdmin(admin.ModelAdmin):
    list_display = ('docente', 'competencia', 'i_index', 'j_index')  # Lista de campos a serem exibidos na lista de Blooms

admin.site.register(Bloom, BloomAdmin)
