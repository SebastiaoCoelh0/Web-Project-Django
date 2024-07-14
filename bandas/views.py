# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from .forms import BandaForm, AlbumForm
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


def musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    context = {
        'album': musica.album,
        'musica': musica
    }
    return render(request, "bandas/musica.html", context)


def in_editors_bandas(user):
    return user.groups.filter(name='editors_bandas').exists()


@login_required
@user_passes_test(in_editors_bandas)
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:index')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)


@login_required
@user_passes_test(in_editors_bandas)
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('banda', banda_id=banda.id)
    else:
        form = BandaForm(instance=banda)

    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/edita_banda.html', context)


@login_required
@user_passes_test(in_editors_bandas)
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:index')


@login_required
@user_passes_test(in_editors_bandas)
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    form = AlbumForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('banda', banda_id=banda.id)

    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/novo_album.html', context)


@login_required
@user_passes_test(in_editors_bandas)
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('banda', banda_id=album.id)
    else:
        form = BandaForm(instance=album)

    context = {'form': form, 'album': album}
    return render(request, 'bandas/edita_album.html', context)


@login_required
@user_passes_test(in_editors_bandas)
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandas')
