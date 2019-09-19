from django.urls import path
from apps.articulo import views


app_name='articulo'

urlpatterns = [
    path('detalle/<int:pk>', views.ArticuloDetailView.as_view(), name='articulo_detalle'),
]

