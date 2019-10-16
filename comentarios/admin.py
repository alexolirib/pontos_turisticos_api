from django.contrib import admin

from comentarios.actions import aprova_comentarios, reprovar_comentarios
from comentarios.models import Comentario

class ComentarioAdimin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions= [aprova_comentarios, reprovar_comentarios]

admin.site.register(Comentario, ComentarioAdimin)


