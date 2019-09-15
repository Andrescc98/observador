from django import forms
from django.forms import ModelForm
from apps.articulo.models import Articulo

class ArticuloForm(forms.ModelForm):
    """Form definition for Articulo."""

    class Meta:
        """Meta definition for Articuloform."""

        model = Articulo
        fields = [
            'Periodista',
            'titulo',
            'contenido',
            'Categoria',
            'imagen',
        ]
        labels={
            'Periodista':'Periodista',
            'titulo':'Titulo',
            'contenido':'Contenido',
            'Categoria':'Categoria',
            'imagen':'Imagen',
        }
        widgets={
            'Periodista':forms.Select(attrs={'class':'form-control'}),
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
            'Categoria':forms.Select(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'custom-file-input'}),
        }