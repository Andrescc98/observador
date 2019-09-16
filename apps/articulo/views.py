from django.shortcuts import render
from django.views.generic import FormView, DetailView, ListView
from apps.articulo.models import Articulo
from apps.articulo.forms import ArticuloForm
from django.urls import reverse_lazy


class ArticuloCreateView(FormView):
    model = Articulo
    form_class=ArticuloForm
    template_name = "Articulo/articulo_crear.html"
    success_url=reverse_lazy('inicio')


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "Articulo/articulo_detalle.html"


    