from django.urls import path

from . import views

app_name = 'artigos'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('artigo/<int:artigo_id>/', views.artigo_view, name='artigo'),
    path('autor/<int:autor_id>/', views.autor_view, name='autor'),
]
