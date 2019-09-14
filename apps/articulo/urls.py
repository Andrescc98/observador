from django.urls import path
from apps.articulo import views


app_name='articulo'

urlpatterns = [
    path('', views.ArticuloListView.as_view(), name='articulo_listar'),
]

