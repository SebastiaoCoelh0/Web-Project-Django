# Create your views here.
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ArtigoForm, ComentarioForm, RatingForm
from .models import Artigo, Utilizador, Comentario, Rating


def index_view(request):
    artigos = Artigo.objects.all().order_by('data_publicacao')
    context = {
        'artigos': artigos
    }
    return render(request, 'artigos/index.html', context)


def artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo).order_by('data_comentario')

    context = {
        'artigo': artigo,
        'comentarios': comentarios
    }
    return render(request, 'artigos/artigo.html', context)


def autor_view(request, autor_id):
    autor = Utilizador.objects.get(id=autor_id)
    artigos = Artigo.objects.filter(autor=autor).order_by('data_publicacao')
    comentarios = Comentario.objects.filter(utilizador=Utilizador.objects.get(id=autor_id))
    context = {
        'autor': autor,
        'artigos': artigos,
        'comentarios': comentarios
    }
    return render(request, 'artigos/autor.html', context)


def in_editors_artigos(user):
    if user.groups.filter(name='editors_artigos').exists():
        utilizador, created = Utilizador.objects.get_or_create(user=user, defaults={'username': user.username})
        if created:
            utilizador.save()
        return True
    return False


@login_required
def novo_artigo_view(request):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = Utilizador.objects.get(user=request.user)  # Associar o artigo ao usuário
            artigo.data_publicacao = datetime.now()
            artigo.save()
            return redirect('artigos:artigo', artigo_id=artigo.id)
    else:
        form = ArtigoForm()
    return render(request, 'artigos/novo_artigo.html', {'form': form})


@login_required
def edita_artigo_view(request, artigo_id):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    artigo = Artigo.objects.get(id=artigo_id)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo', artigo_id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/edita_artigo.html', {'form': form, 'artigo': artigo})


@login_required
def apaga_artigo_view(request, artigo_id):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('artigos:index')


# Comentários
@login_required
def novo_comentario_view(request, artigo_id):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    artigo = Artigo.objects.get(id=artigo_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.utilizador.user = request.user  # Associar o comentário ao utilizador
            comentario.data_criacao = datetime.now()
            comentario.save()
            return redirect('artigos:artigo', artigo_id=artigo.id)
    else:
        form = ComentarioForm()
    return render(request, 'artigos/novo_comentario.html', {'form': form, 'artigo': artigo})


@login_required
def edita_comentario_view(request, comentario_id):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    comentario = Comentario.objects.get(id=comentario_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo', artigo_id=comentario.artigo.id)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'artigos/edita_comentario.html', {'form': form, 'comentario': comentario})


@login_required
def apaga_comentario_view(request, comentario_id):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()
    return redirect('artigos:artigo', artigo_id=comentario.artigo.id)


# Ratings
@login_required
def novo_rating_view(request, artigo_id):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    artigo = Artigo.objects.get(id=artigo_id)
    utilizador = Utilizador.objects.get(user=request.user)

    # Verifica se o utilizador já tem um rating para este artigo
    rating_existente = Rating.objects.filter(artigo=artigo, utilizador=utilizador).first()
    if rating_existente:
        return redirect('artigos:edita_rating', rating_id=rating_existente.id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.artigo = artigo
            rating.utilizador = utilizador
            rating.save()

            artigo.atualizar_media_rating()
            artigo.save()
            return redirect('artigos:artigo', artigo_id=artigo.id)
    else:
        form = RatingForm()
    return render(request, 'artigos/novo_rating.html', {'form': form, 'artigo': artigo})


@login_required
def edita_rating_view(request, rating_id):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    rating = Rating.objects.get(id=rating_id)
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            artigo = rating.artigo
            artigo.atualizar_media_rating()
            artigo.save()
            return redirect('artigos:artigo', artigo_id=rating.artigo.id)
    else:
        form = RatingForm(instance=rating)
    return render(request, 'artigos/edita_rating.html', {'form': form, 'rating': rating})


@login_required
def apaga_rating_view(request, rating_id):
    if not in_editors_artigos(request.user):
        return redirect('autenticacao:sem_permissao')
    rating = Rating.objects.get(id=rating_id)
    artigo = rating.artigo
    artigo.atualizar_media_rating()
    artigo.save()
    rating.delete()
    return redirect('artigos:artigo', artigo_id=rating.artigo.id)
