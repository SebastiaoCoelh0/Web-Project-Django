# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Curso, Disciplina, Projeto


def curso_view(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'curso/curso.html', context)


def disciplina_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    projetos = Projeto.objects.filter(disciplina=disciplina)
    context = {
        'disciplina': disciplina,
        'projetos': projetos
    }
    return render(request, 'curso/disciplina.html', context)


def projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    context = {
        'projeto': projeto
    }
    return render(request, 'curso/projetos.html', context)


def projetos_view(request):
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos
    }
    return render(request, 'curso/projetos.html', context)


def in_editors_curso(user):
    return user.groups.filter(name='editors_curso').exists()
