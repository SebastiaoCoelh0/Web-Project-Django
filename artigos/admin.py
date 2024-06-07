# Register your models here.
from django.contrib import admin
from .models import Utilizador, Artigo, Comentario, Rating

admin.site.register(Utilizador)
admin.site.register(Artigo)
admin.site.register(Comentario)
admin.site.register(Rating)
