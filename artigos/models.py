# Create your models here.

from django.db import models


class Utilizador(models.Model):
    username = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.username


class Artigo(models.Model):
    autor = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_publicacao = models.DateField()
    rating_final = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.artigo.titulo} - {self.utilizador.nome}'


class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    valor = models.IntegerField()
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.utilizador.nome} - {self.valor} - {self.artigo.titulo}'
