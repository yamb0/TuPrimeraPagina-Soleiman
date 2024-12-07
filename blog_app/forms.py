from django import forms
from .models import Artista, Album, Cancion

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = '__all__'

class BuscarAlbumForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False)
