from django.urls import path

from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    path('sem_permissao/', views.sem_permissao_view, name='sem_permissao')
]
