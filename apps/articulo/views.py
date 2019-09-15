from django.shortcuts import render
from django.views.generic import CreateView
from apps.articulo.models import Articulo
from apps.articulo.forms import ArticuloForm
from django.urls import reverse_lazy


class ArticuloCreateView(CreateView):
    model = Articulo
    template_name = "Articulo/articulo_crear.html"
    form_class=ArticuloForm
    success_url=reverse_lazy('inicio')
