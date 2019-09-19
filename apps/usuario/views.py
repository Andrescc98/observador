from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from apps.articulo.models import Articulo
from django.urls import reverse_lazy
from apps.articulo.forms import ArticuloForm



class ArticuloListView(ListView):
    queryset = Articulo.objects.order_by('-f_publicacion')
    template_name = "usuario/articulo_listar.html"


class ArticuloCreateView(CreateView):
    model = Articulo
    form_class=ArticuloForm
    template_name = 'usuario/articulo_crear.html'
    success_url=reverse_lazy('usuario:listar_articulo')


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "usuario/articulo_detalle.html"


