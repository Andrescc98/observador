from django.urls import path
from apps.articulo import views


app_name='articulo'

urlpatterns = [
    path('crear/', views.ArticuloCreateView.as_view(), name='articulo_crear'),
]

