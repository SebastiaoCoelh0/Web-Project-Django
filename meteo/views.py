import requests
from django.shortcuts import render


def index(request):
    return render(request, 'meteo/index.html')


def lisboa(request):
    url_previsao = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'  # URL para previsão de Lisboa
    url_classes = 'https://api.ipma.pt/open-data/weather-type-classe.json'  # URL para classes de tempo

    response_previsao = requests.get(url_previsao)
    response_classes = requests.get(url_classes)

    print(f"Status code previsão: {response_previsao.status_code}")
    print(f"Status code classes: {response_classes.status_code}")

    if response_previsao.status_code == 200 and response_classes.status_code == 200:
        previsao = response_previsao.json()
        classes = response_classes.json()

        print(f"Resposta previsão: {previsao}")
        print(f"Resposta classes: {classes}")

        previsao_hoje = previsao['data'][0]
        id_weather_type = previsao_hoje['idWeatherType']
        descricao = next(
            (item['descWeatherTypePT'] for item in classes['data'] if item['idWeatherType'] == id_weather_type), None)
        icon = f"/static/meteo/w_ic_d_{previsao_hoje['idWeatherType']:02d}anim.svg"

        context = {
            'cidade': 'Lisboa',
            'temp_min': previsao_hoje['tMin'],
            'temp_max': previsao_hoje['tMax'],
            'data': previsao_hoje['forecastDate'],
            'descricao': descricao,
            'icon': icon
        }

        return render(request, 'meteo/lisboa.html', context)
    else:
        print("Erro ao consultar a API do IPMA")
        return render(request, 'meteo/error.html', {'message': 'Erro ao consultar a API do IPMA'})


def previsao(request):
    url_cidades = 'https://api.ipma.pt/open-data/distrits-islands.json'

    response_cidades = requests.get(url_cidades)

    if response_cidades.status_code == 200:
        cidades = response_cidades.json()
        cidades_list = cidades['data']

        if request.method == 'POST':
            cidade_id = request.POST.get('cidade')
            url_previsao = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
            response_previsao = requests.get(url_previsao)

            if response_previsao.status_code == 200:
                previsao = response_previsao.json()
                previsoes = previsao['data']
                context = {'cidades': cidades_list, 'previsoes': previsoes}
                return render(request, 'meteo/previsao.html', context)
        else:
            context = {'cidades': cidades_list}
            return render(request, 'meteo/previsao.html', context)
    else:
        return render(request, 'meteo/error.html', {'message': 'Erro ao consultar a API do IPMA'})
