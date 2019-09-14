from django.shortcuts import render
from django.views.generic import ListView
from apps.articulo.models import Articulo

class ArticuloListView(ListView):
    model = Articulo
    template_name = "articulo/listar_articulo.html"
    context_object_name='articulos'
