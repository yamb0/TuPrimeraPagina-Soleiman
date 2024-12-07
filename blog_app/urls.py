from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("crear-artista/", views.crear_artista, name="crear_artista"),
    path("crear-album/", views.crear_album, name="crear_album"),
    path("crear-cancion/", views.crear_cancion, name="crear_cancion"),
    path("buscar-album/", views.buscar_album, name="buscar_album"),
]
