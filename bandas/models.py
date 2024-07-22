# Create your models here.
from django.db import models


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='bandas', null=True, blank=True)
    descricao = models.CharField(max_length=500)
    lancamento_primeiro_album = models.IntegerField()
    banda_ativa = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='albuns', null=True, blank=True)
    lancamento = models.DateField()

    def __str__(self):
        return self.titulo


class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=6)
    link_spotify = models.URLField(null=True, blank=True)
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.titulo
