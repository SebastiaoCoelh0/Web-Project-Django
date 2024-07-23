from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('lisboa/', views.lisboa, name='lisboa'),
    path('previsao', views.previsao_proximos_5_dias, name='previsao'),
    path('api/cidades/', views.listar_cidades, name='listar_cidades'),
    path('api/previsao_hoje/<int:cidade_id>/', views.previsao_hojeAPI, name='previsao_hojeAPI'),
    path('api/previsao_proximos_5_dias/<int:cidade_id>/', views.previsao_proximos_5_diasAPI, name='previsao_proximos_5_diasAPI'),
    path('api/documentation/', views.api_documentation, name='api_documentation'),
]
