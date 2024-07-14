# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Artigo, Utilizador, Comentario


def index_view(request):
    artigos = Artigo.objects.all().order_by('data_publicacao')
    context = {
        'artigos': artigos
    }
    return render(request, 'artigos/index.html', context)


def artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo).order_by('data_comentario')
    context = {
        'artigo': artigo,
        'comentarios': comentarios
    }
    return render(request, 'artigos/artigo.html', context)


def autor_view(request, autor_id):
    autor = get_object_or_404(Utilizador, id=autor_id)
    artigos = Artigo.objects.filter(autor=autor).order_by('data_publicacao')
    context = {
        'autor': autor,
        'artigos': artigos
    }
    return render(request, 'artigos/autor.html', context)


def in_editors_artigos(user):
    return user.groups.filter(name='editors_artigos').exists()
