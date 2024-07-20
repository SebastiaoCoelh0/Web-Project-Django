from django import forms  # formulários Django

from .models import Banda, Album, Musica


class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'
        labels = {
            'descricao': 'Descrição',
            'lancamento': 'Lançamento do primeiro álbum'
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        exclude = ['banda']
        labels = {
            'titulo': 'Título',
            'lancamento': 'Lançamento do álbum'
        }
        widgets = {
            'lancamento': forms.DateInput(attrs={'type': 'date'})
        }


class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        exclude = ['album']
        labels = {
            'titulo': 'Título',
            'duracao': 'Duração'
        }
        help_texts = {
            'duracao': 'Formato min:seg ex: 05:33'
        }
