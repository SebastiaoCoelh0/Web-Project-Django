from django.urls import path

from . import views

app_name = 'curso'
urlpatterns = [
    path('', views.curso_view, name='curso'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina'),
    path('projeto/<int:projeto_id>/', views.projeto_view, name='projeto'),
    path('projetos/', views.projetos_view, name='projetos'),
]
