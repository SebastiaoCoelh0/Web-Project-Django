# Create your views here.
from django.shortcuts import render

from .models import *


def index_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome'),
    }
    return render(request, "bandas/index.html", context)


def banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    context = {
        'banda': banda,
        'albuns': banda.album_set.all()
    }
    return render(request, "bandas/banda.html", context)


def albuns_view(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {
        'album': album,
        'musicas': album.musica_set.all()
    }
    return render(request, "bandas/album.html", context)
