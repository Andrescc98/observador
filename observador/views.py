from django.shortcuts import render
from django.views.generic import ListView
from apps.articulo.models import Articulo


class ArticuloListView(ListView):
    queryset = Articulo.objects.order_by('-f_publicacion')
    template_name = "articulo/listar_articulo.html"
    context_object_name='articulos'
    paginate_by=5
    
class CategoriaListView(ListView):
    template_name = "articulo/listar_articulo.html"
    context_object_name='articulos'
    paginate_by=5

    def get_queryset(self):
        return Articulo.objects.filter(Categoria=self.kwargs['cat'])
    