# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import BandaForm, AlbumForm, MusicaForm
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
def nova_banda_view(request):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:index')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)


@login_required
def edita_banda_view(request, banda_id):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda', banda_id=banda.id)
    else:
        form = BandaForm(instance=banda)

    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/edita_banda.html', context)


@login_required
def apaga_banda_view(request, banda_id):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:index')


@login_required
def novo_album_view(request, banda_id):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    banda = Banda.objects.get(id=banda_id)
    form = AlbumForm(request.POST or None, request.FILES)
    if form.is_valid():
        album = form.save(commit=False)
        album.banda = banda
        album.save()
        return redirect('bandas:banda', banda_id=banda.id)

    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/novo_album.html', context)


@login_required
def edita_album_view(request, album_id):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    album = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:album', album_id=album.id)
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album': album}
    return render(request, 'bandas/edita_album.html', context)


@login_required
def apaga_album_view(request, album_id):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    album = Album.objects.get(id=album_id)
    banda = album.banda
    album.delete()
    return redirect('bandas:banda', banda_id=banda.id)


@login_required
def nova_musica_view(request, album_id):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    album = Album.objects.get(id=album_id)
    form = MusicaForm(request.POST or None, request.FILES)
    if form.is_valid():
        musica = form.save(commit=False)
        musica.album = album
        musica.save()
        return redirect('bandas:album', album_id=album.id)

    context = {'form': form, 'album': album}
    return render(request, 'bandas/nova_musica.html', context)


@login_required
def edita_musica_view(request, musica_id):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    musica = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:musica', album_id=musica.id)
    else:
        form = MusicaForm(instance=musica)

    context = {'form': form, 'musica': musica}
    return render(request, 'bandas/edita_musica.html', context)


@login_required
def apaga_musica_view(request, musica_id):
    if not in_editors_bandas(request.user):
        return redirect('autenticacao:sem_permissao')
    musica = Musica.objects.get(id=musica_id)
    album = musica.album
    musica.delete()
    return redirect('bandas:album', album_id=album.id)
