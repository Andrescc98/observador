from django.urls import path
from apps.usuario import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


app_name='usuario'

urlpatterns = [
    path('', login_required(views.ArticuloListView.as_view()), name='listar_articulo'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('crear_articulo/', login_required(views.ArticuloCreateView.as_view()), name='crear_articulo'),
    path('mostrar_articulo/<int:pk>',login_required(views.ArticuloDetailView.as_view()), name='mostrar_articulo'),
]
