from django.urls import path

from . import views

app_name = 'curso'
urlpatterns = [
    path('', views.curso_view, name='curso'),
    # path('novo', views.novo_curso_view, name='novo_curso'),
    # path('<int:curso_id>/editar', views.edita_curso_view, name='edita_curso'),
    # path('<int:curso_id>/apagar', views.apaga_curso_view, name='apaga_curso'),

    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina'),
    # path('disciplina/nova', views.nova_disciplina_view, name='nova_disciplina'),
    # path('disciplina/<int:disciplina_id>/editar', views.edita_disciplina_view, name='edita_disciplina'),
    # path('disciplina/<int:disciplina_id>/apagar', views.apaga_disciplina_view, name='apaga_disciplina'),

    path('projeto/<int:projeto_id>/', views.projeto_view, name='projeto'),
    # path('projeto/novo', views.novo_projeto_view, name='novo_projeto'),
    # path('projeto/<int:projeto_id>/editar', views.edita_projeto_view, name='edita_projeto'),
    # path('projeto/<int:projeto_id>/apagar', views.apaga_projeto_view, name='apaga_projeto'),

    path('projetos/', views.projetos_view, name='projetos'),

    # path('linguagem_programacao/nova', views.nova_linguagem_programacao_view, name='nova_linguagem_programacao'),
    # path('linguagem_programacao/<int:linguagem_programacao_id>/editar', views.edita_linguagem_programacao_view,
    #      name='edita_linguagem_programacao'),
    # path('linguagem_programacao/<int:linguagem_programacao_id>/apagar', views.apaga_linguagem_programacao_view,
    #      name='apaga_linguagem_programacao'),
    #
    # path('docente/novo', views.novo_docente_view, name='novo_docente'),
    # path('docente/<int:docente_id>/editar', views.edita_docente_view, name='edita_docente'),
    # path('docente/<int:docente_id>/apagar', views.apaga_docente_view, name='apaga_docente'),
]
