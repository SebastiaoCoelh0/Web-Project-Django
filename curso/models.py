# Create your models here.
from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.IntegerField()
    apresentacao = models.CharField(max_length=500)
    objetivos = models.CharField(max_length=500)
    competencias = models.CharField(max_length=500)
    ects = models.IntegerField()
    duracao_semestres = models.IntegerField()
    departamento = models.CharField(max_length=255)
    contacto_direcao = models.CharField(max_length=255)
    email_direcao = models.EmailField()
    contacto_secretaria = models.CharField(max_length=255)
    email_secretaria = models.EmailField()
    disciplinas = models.ManyToManyField('Disciplina', related_name='cursos')

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.FloatField()
    codigo_leitura = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    descricao = models.CharField(max_length=500)
    conceitos_aplicados = models.CharField(max_length=500)
    tecnologias_usadas = models.CharField(max_length=500)
    imagem = models.ImageField()
    video_link = models.URLField()
    github_link = models.URLField()
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"Projeto da disciplina {self.disciplina.nome}"


class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=255)
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=255)
    disciplinas = models.ManyToManyField(Disciplina, related_name='docentes')

    def __str__(self):
        return self.nome
