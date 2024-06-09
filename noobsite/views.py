# Create your views here.
from django.http import HttpResponse


def index_view1(request):
    return HttpResponse("Olá noob esta é a pagina web mais básica do mundo!")


def index_view2(request):
    return HttpResponse("Ficha 6 é fixe")


def index_view3(request):
    return HttpResponse("Hello World!")
