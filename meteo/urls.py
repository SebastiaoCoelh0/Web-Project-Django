from django.urls import path

from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('lisboa/', views.lisboa_view, name='weather_lisboa'),
    path('weather/', views.previsao_view, name='weather_previsao'),
    path('api/', views.api_view, name='api'),
    path('api/avisos-meteorologicos/', views.avisos_meteorologicos_view, name='avisos-meteorologicos'),
    path('api/informacao-sismicidade/<int:idArea>/', views.informacao_sismicidade_view, name='informacao-sismicidade'),
    path('api/observacao-meteorologica/', views.observacao_meteorologica_view, name='observacao-meteorologica'),
]