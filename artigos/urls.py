from django.urls import path

from . import views

app_name = 'artigos'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('artigo/<int:artigo_id>/', views.artigo_view, name='artigo'),
    path('autor/<int:autor_id>/', views.autor_view, name='autor'),

    # Artigos
    path('artigo/novo/', views.novo_artigo_view, name='novo_artigo'),
    path('artigo/<int:artigo_id>/editar/', views.edita_artigo_view, name='edita_artigo'),
    path('artigo/<int:artigo_id>/apagar/', views.apaga_artigo_view, name='apaga_artigo'),
    path('artigo/<int:artigo_id>/novo_rating/', views.novo_rating_view, name='novo_rating'),
    path('artigo/<int:artigo_id>/novo_comentario/', views.novo_comentario_view, name='novo_comentario'),

    # Comentários
    path('comentario/<int:comentario_id>/editar/', views.edita_comentario_view, name='edita_comentario'),
    path('comentario/<int:comentario_id>/apagar/', views.apaga_comentario_view, name='apaga_comentario'),

    # Ratings
    path('rating/<int:rating_id>/editar/', views.edita_rating_view, name='edita_rating'),
    path('rating/<int:rating_id>/apagar/', views.apaga_rating_view, name='apaga_rating'),
]
