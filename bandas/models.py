# Create your models here.
from django.db import models


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='bandas/fotos/', null=True, blank=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='bandas/capas/', null=True, blank=True)
    lancamento = models.DateField()

    def __str__(self):
        return self.titulo


class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    duracao = models.DurationField()
    link_spotify = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo
