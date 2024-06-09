from django.urls import path

from . import views

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('pastel_de_nata/', views.pastel_de_nata_view, name='pastel_de_nata'),
    path('bacalhau_a_bras/', views.bacalhau_a_bras_view, name='bacalhau_a_bras'),
]
