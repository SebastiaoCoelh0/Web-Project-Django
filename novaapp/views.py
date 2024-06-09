# Create your views here.
from django.shortcuts import render


def index_view(request):
    return render(request, 'novaapp/index.html')


def pastel_de_nata_view(request):
    return render(request, 'novaapp/pastel_de_nata.html')


def bacalhau_a_bras_view(request):
    return render(request, 'novaapp/bacalhau_a_bras.html')
