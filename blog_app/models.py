from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=200)
    anio_lanzamiento = models.IntegerField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name="albumes")

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    duracion = models.CharField(max_length=10)  # Ejemplo: "3:45"
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="canciones")

    def __str__(self):
        return self.titulo
