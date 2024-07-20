from django.urls import path

from . import views

app_name = 'bandas'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('banda/<int:banda_id>/', views.banda_view, name='banda'),
    path('banda/novo', views.nova_banda_view, name="nova_banda"),
    path('banda/<int:banda_id>/editar', views.edita_banda_view, name="edita_banda"),
    path('banda/<int:banda_id>/apagar', views.apaga_banda_view, name="apaga_banda"),

    path('album/<int:album_id>/', views.albuns_view, name='album'),
    path('banda/<int:banda_id>/novo_album', views.novo_album_view, name="novo_album"),
    path('album/<int:album_id>/editar', views.edita_album_view, name="edita_album"),
    path('album/<int:album_id>/apagar', views.apaga_album_view, name="apaga_album"),
    path('musicas/<int:musica_id>/', views.musica_view, name='musica'),

    path('musica/<int:album_id>/nova_musica', views.nova_musica_view, name="nova_musica"),
    path('musica/<int:musica_id>/editar', views.edita_musica_view, name="edita_musica"),
    path('musica/<int:musica_id>/apagar', views.apaga_musica_view, name="apaga_musica"),

]
