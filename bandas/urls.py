from django.urls import path

from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('banda/<int:banda_id>/', views.banda_view, name='banda'),
    path('banda/novo', views.nova_banda_view, name="nova_banda"),
    path('banda/<int:banda_id>/apaga', views.apaga_banda_view, name="apaga_banda"),
    path('banda/<int:banda_id>/novo_album', views.novo_album_view, name="novo_album"),
    path('albuns/<int:album_id>/', views.albuns_view, name='album'),
    path('musicas/<int:musica_id>/', views.musica_view, name='musica'),
]
