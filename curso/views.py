# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CursoForm, DisciplinaForm, ProjetoForm, DocenteForm, LinguagemProgramacaoForm
from .models import Curso, Disciplina, Projeto, LinguagemProgramacao, Docente


def curso_view(request):
    cursos = Curso.objects.all()

    cursos_disciplinas = []

    for curso in cursos:
        disciplinas_por_ano = {}
        for disciplina in curso.disciplinas.all():
            ano = disciplina.ano
            semestre = disciplina.semestre
            if ano not in disciplinas_por_ano:
                disciplinas_por_ano[ano] = {'1º Semestre': [], '2º Semestre': [], 'Anual': []}
            disciplinas_por_ano[ano][semestre].append(disciplina)

        cursos_disciplinas.append({
            'curso': curso,
            'disciplinas_por_ano': disciplinas_por_ano
        })

    context = {
        'cursos_disciplinas': cursos_disciplinas,
    }
    return render(request, 'curso/index.html', context)


def disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    projetos = Projeto.objects.filter(disciplina=disciplina)
    context = {
        'disciplina': disciplina,
        # 'projetos': projetos
    }
    return render(request, 'curso/disciplina.html', context)


def linguagens_programacao_view(request):
    lp = LinguagemProgramacao.objects.all()
    context = {
        'linguagens_programacao': lp,
    }
    return render(request, 'curso/linguagens_programacao.html', context)


def projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
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


def docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    context = {
        'docente': docente,
        'disciplinas': docente.disciplinas.all()
    }
    return render(request, 'curso/docente.html', context)


def in_editors_cursos(user):
    return user.groups.filter(name='editors_curso').exists()


@login_required
def novo_curso_view(request):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')

    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)


@login_required
def edita_curso_view(request, curso_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    curso = Curso.objects.get(id=curso_id)

    if request.POST:
        form = CursoForm(request.POST or None, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:curso', curso_id=curso_id)
    else:
        form = CursoForm(instance=curso)

    context = {'form': form, 'curso': curso}
    return render(request, 'curso/edita_curso.html', context)


@login_required
def apaga_curso_view(request, curso_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('curso:curso')


@login_required
def nova_disciplina_view(request):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:curso')

    context = {'form': form}
    return render(request, 'curso/nova_disciplina.html', context)


@login_required
def edita_disciplina_view(request, disciplina_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    disciplina = Disciplina.objects.get(id=disciplina_id)

    if request.POST:
        form = DisciplinaForm(request.POST or None, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina', disciplina_id=disciplina.id)
    else:
        form = DisciplinaForm(instance=disciplina)

    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'curso/edita_disciplina.html', context)


@login_required
def apaga_disciplina_view(request, disciplina_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('curso:curso')


@login_required
def novo_projeto_view(request):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('curso:projetos')

    context = {'form': form}
    return render(request, 'curso/novo_projeto.html', context)


@login_required
def edita_projeto_view(request, projeto_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    projeto = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:projeto', projeto_id=projeto.id)
    else:
        form = ProjetoForm(instance=projeto)

    context = {'form': form, 'projeto': projeto}
    return render(request, 'curso/edita_projeto.html', context)


@login_required
def apaga_projeto_view(request, projeto_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('curso:projetos')


@login_required
def nova_linguagem_programacao_view(request):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    form = LinguagemProgramacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:curso')

    context = {'form': form}
    return render(request, 'curso/nova_linguagem_programacao.html', context)


@login_required
def edita_linguagem_programacao_view(request, linguagem_programacao_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    linguagem_programacao = LinguagemProgramacao.objects.get(id=linguagem_programacao_id)

    if request.POST:
        form = LinguagemProgramacaoForm(request.POST or None, instance=linguagem_programacao)
        if form.is_valid():
            form.save()
            return redirect('curso:curso')
    else:
        form = LinguagemProgramacaoForm(instance=linguagem_programacao)

    context = {'form': form, 'linguagem_programacao': linguagem_programacao}
    return render(request, 'curso/edita_linguagem_programacao.html', context)


@login_required
def apaga_linguagem_programacao_view(request, linguagem_programacao_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    linguagem_programacao = LinguagemProgramacao.objects.get(id=linguagem_programacao_id)
    linguagem_programacao.delete()
    return redirect('curso:curso')


@login_required
def novo_docente_view(request):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    form = DocenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:curso')

    context = {'form': form}
    return render(request, 'curso/novo_docente.html', context)


@login_required
def edita_docente_view(request, docente_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    docente = Docente.objects.get(id=docente_id)

    if request.POST:
        form = DocenteForm(request.POST or None, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('curso:curso')
    else:
        form = DocenteForm(instance=docente)

    context = {'form': form, 'docente': docente}
    return render(request, 'curso/edita_docente.html', context)


@login_required
def apaga_docente_view(request, docente_id):
    if not in_editors_cursos(request.user):
        return redirect('autenticacao:sem_permissao')
    docente = Docente.objects.get(id=docente_id)
    docente.delete()
    return redirect('curso:curso')
