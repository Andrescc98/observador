from django.contrib import admin
from apps.articulo.models import Articulo, Categoria


class ArticuloAdmin(admin.ModelAdmin):
    list_display=('titulo', 'Periodista', 'f_publicacion')
    list_filter=('f_publicacion',)
    


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Categoria)