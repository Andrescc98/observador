from django.shortcuts import render
from django.views.generic import FormView, DetailView, ListView
from apps.articulo.models import Articulo
from apps.articulo.forms import ArticuloForm
from django.urls import reverse_lazy


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "Articulo/articulo_detalle.html"


    