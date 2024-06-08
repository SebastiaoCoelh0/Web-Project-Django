import json

from bandas.models import *

Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

with open('bandas/json/bandas.json', 'r') as file:
    bandas = json.load(file)
    for banda, info in bandas.items():
        Banda.objects.create(
            nome=banda,
            descricao=info.get('descricao'),
            lancamento_primeiro_album=info.get('lancamento_primeiro_album'),
            banda_ativa=info.get('banda_ativa')
        )
print('bandas OK!')
with open('bandas/json/albuns.json', 'r') as file:
    albuns = json.load(file)
    for banda_nome, albums_data in albuns.items():

        banda = Banda.objects.get(nome=banda_nome)

        for album_data in albums_data:

            album = Album.objects.create(
                banda=banda,
                titulo=album_data['titulo'],
                lancamento=album_data['lancamento']
            )

            for musica_data in album_data['musicas']:
                Musica.objects.create(
                    album=album,
                    titulo=musica_data['titulo'],
                    duracao=musica_data['duracao'],
                    link_spotify=musica_data.get('link_spotify', None)
                )

print('albuns OK!')
