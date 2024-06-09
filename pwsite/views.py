# Create your views here.

from datetime import datetime

from django.shortcuts import render


def index_view(request):
    return render(request, "pwsite/index.html")


def interesses_view(request):
    current_date = datetime.now()  # Obter a data atual
    context = {'current_date': current_date}
    return render(request, "pwsite/interesses.html", context)


def sobre_view(request):
    return render(request, "pwsite/sobre.html")
