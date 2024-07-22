# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Utilizador(models.Model):
    username = models.CharField(max_length=100, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


class Artigo(models.Model):
    autor = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_publicacao = models.DateField()
    media_ratings = models.FloatField(default=0)

    def __str__(self):
        return self.titulo

    def atualizar_media_rating(self):
        ratings = Rating.objects.all().filter(artigo=self)
        if ratings.exists():
            temp = 0
            for rating in ratings:
                temp += rating.valor
            self.media_ratings = round((temp / ratings.count()), 1)
        else:
            self.media_ratings = 0
        self.save()


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.artigo.titulo} - {self.utilizador.username}'


class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    valor = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('artigo', 'utilizador')

    def __str__(self):
        return f'{self.utilizador.username} - {self.valor} - {self.artigo.titulo}'
