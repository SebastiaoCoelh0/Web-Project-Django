# forms.py

from django import forms

from .models import Artigo, Comentario, Rating


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'
        exclude = ['autor', 'data_publicacao', 'media_ratings']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        exclude = ['utilizador', 'artigo', 'data_comentario']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
        exclude = ['utilizador', 'artigo']
