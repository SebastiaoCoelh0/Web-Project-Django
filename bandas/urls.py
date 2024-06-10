from django.urls import path

from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('banda/<int:banda_id>/', views.banda_view, name='banda'),
    path('albuns/<int:album_id>/', views.albuns_view, name='album'),
]
