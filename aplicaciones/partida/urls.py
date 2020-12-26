from django.contrib import admin
from django.urls import path
from . import views

app_name = "partida_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name = 'inicio' ),
    path('partidas/', views.PartidaListView.as_view(), name = 'lista_partidas' ),
    path('crear-partida/', views.PartidaCreateView.as_view(), name = 'crear_partida' ),
    path('editar-partida/<pk>/', views.PartidaUpdateView.as_view(), name = 'editar_partida' ),
    path('eliminar-partida/<pk>/', views.PartidaDeleteView.as_view(), name = 'eliminar_partida'),
]
