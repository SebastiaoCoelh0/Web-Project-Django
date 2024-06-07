# Register your models here.
from django.contrib import admin
from .models import Banda, Album, Musica

admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Musica)

