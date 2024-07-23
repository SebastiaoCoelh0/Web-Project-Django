from django.urls import path

from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('lisboa/', views.lisboa_view, name='weather_lisboa'),
    path('weather/', views.previsao_view, name='weather_previsao'),
    path('api/', views.api_view, name='api'),
]
