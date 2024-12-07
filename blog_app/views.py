from django.shortcuts import render
from .models import Artista, Album, Cancion
from .forms import ArtistaForm, AlbumForm, CancionForm, BuscarAlbumForm

def inicio(request):
    return render(request, "blog_app/inicio.html")

def crear_artista(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArtistaForm()
    return render(request, "blog_app/formulario.html", {"form": form, "titulo": "Agregar Artista"})

def crear_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlbumForm()
    return render(request, "blog_app/formulario.html", {"form": form, "titulo": "Agregar Álbum"})

def crear_cancion(request):
    if request.method == "POST":
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CancionForm()
    return render(request, "blog_app/formulario.html", {"form": form, "titulo": "Agregar Canción"})

def buscar_album(request):
    albumes = []
    if request.method == "POST":
        form = BuscarAlbumForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            albumes = Album.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarAlbumForm()
    return render(request, "blog_app/buscar.html", {"form": form, "albumes": albumes})
