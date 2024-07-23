import requests
from django.shortcuts import render
from django.http import JsonResponse

def obter_nome_cidade(cidade_id):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cidades_response = requests.get(cidades_url)

    if cidades_response.status_code != 200:
        return "Nome da cidade não disponível"

    dic_cidades = cidades_response.json()
    cidades_data = dic_cidades.get('data', [])

    for cidade in cidades_data:
        if cidade.get('globalIdLocal') == cidade_id:
            return cidade.get('local')

    return "Nome da cidade não disponível"

def listar_cidades(request):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cidades_response = requests.get(cidades_url)
    if cidades_response.status_code == 200:
        dic_cidades = cidades_response.json()
        cidades_data = dic_cidades.get('data', [])
        cidades = [{"nome": cidade.get('local'), "id": cidade.get('globalIdLocal')} for cidade in cidades_data]
        return JsonResponse({"cidades": cidades})
    else:
        return JsonResponse({"error": "Erro ao consultar a API do IPMA"}, status=500)

def previsao_hojeAPI(request, cidade_id):
    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    previsao_response = requests.get(previsao_url)
    if previsao_response.status_code == 200:
        dic_previsao = previsao_response.json()
        previsao_hoje = dic_previsao['data'][0]
    else:
        return JsonResponse({"error": "Erro ao consultar a API do IPMA"}, status=500)

    weather_types_response = requests.get(weather_types_url)
    if weather_types_response.status_code == 200:
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])
        weather_types = {item['idWeatherType']: item for item in weather_types_list}
        weather_description = weather_types.get(previsao_hoje['idWeatherType'], {}).get('descWeatherTypePT', 'Descrição não disponível')
    else:
        weather_description = 'Descrição não disponível'

    resposta = {
        "cidade": obter_nome_cidade(cidade_id),
        "data": previsao_hoje.get('forecastDate', 'N/A'),
        "min_temp": previsao_hoje.get('tMin', 'N/A'),
        "max_temp": previsao_hoje.get('tMax', 'N/A'),
        "descricaoTempo": weather_description,
        "precipitacao": previsao_hoje.get('precipitaProb', 'N/A'),
        "icon_url": f"https://www.ipma.pt/bin/images/weather-symbols/w_ic_d_{previsao_hoje['idWeatherType']:02d}anim.svg"
    }

    return JsonResponse(resposta)

def previsao_proximos_5_diasAPI(request, cidade_id):
    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    previsao_response = requests.get(previsao_url)
    if previsao_response.status_code == 200:
        dic_previsao = previsao_response.json()
        previsoes = dic_previsao['data'][:5]
    else:
        return JsonResponse({"error": "Erro ao consultar a API do IPMA"}, status=500)

    weather_types_response = requests.get(weather_types_url)
    if weather_types_response.status_code == 200:
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])
        weather_types = {item['idWeatherType']: item for item in weather_types_list}
    else:
        weather_types = {}

    previsao_proximos_5_dias = []
    for previsao in previsoes:
        weather_description = weather_types.get(previsao['idWeatherType'], {}).get('descWeatherTypePT', 'Descrição não disponível')
        previsao_proximos_5_dias.append({
            "data": previsao.get('forecastDate', 'N/A'),
            "min_temp": previsao.get('tMin', 'N/A'),
            "max_temp": previsao.get('tMax', 'N/A'),
            "descricaoTempo": weather_description,
            "precipitacao": previsao.get('precipitaProb', 'N/A'),
            "icon_url": f"https://www.ipma.pt/bin/images/weather-symbols/w_ic_d_{previsao['idWeatherType']:02d}anim.svg"
        })

    resposta = {
        "cidade": obter_nome_cidade(cidade_id),
        "previsoes": previsao_proximos_5_dias
    }

    return JsonResponse(resposta)

def lisboa(request):
    previsaoLisboa_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    previsao_response = requests.get(previsaoLisboa_url)
    if previsao_response.status_code == 200:
        dic_previsao = previsao_response.json()
        previsao_hoje = dic_previsao['data'][0]
    else:
        previsao_hoje = {}

    weather_types_response = requests.get(weather_types_url)
    if weather_types_response.status_code == 200:
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])
        weather_types = {item['idWeatherType']: item for item in weather_types_list}
    else:
        weather_types = {}

    city_name = "Lisboa"
    min_temp = previsao_hoje.get('tMin', 'N/A')
    max_temp = previsao_hoje.get('tMax', 'N/A')
    dataDeHoje = previsao_hoje.get('forecastDate', 'N/A')
    weather_type_id = previsao_hoje.get('idWeatherType', 'N/A')
    weather_description = weather_types.get(weather_type_id, {}).get('descWeatherTypePT', 'N/A')
    icon_filename = f"w_ic_d_{weather_type_id:02d}anim.svg"
    icon_url = f"/static/meteo/{icon_filename}"

    context = {
        'cidade': city_name,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'dataDeHoje': dataDeHoje,
        'descricaoTempo': weather_description,
        'icon_url': icon_url,
    }

    return render(request, 'meteo/lisboa.html', context)

def previsao_proximos_5_dias(request):
    cidade_id = 1110600
    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    previsao_response = requests.get(previsao_url)
    if previsao_response.status_code == 200:
        previsao_data = previsao_response.json()['data'][:5]
    else:
        previsao_data = []

    weather_types_response = requests.get(weather_types_url)
    if (weather_types_response.status_code == 200):
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])
        weather_types = {item['idWeatherType']: item for item in weather_types_list}
    else:
        weather_types = {}

    proximos_5_dias = []
    for dia in previsao_data:
        data = dia.get('forecastDate', 'N/A')
        min_temp = dia.get('tMin', 'N/A')
        max_temp = dia.get('tMax', 'N/A')
        weather_type_id = dia.get('idWeatherType', 'N/A')
        weather_description = weather_types.get(weather_type_id, {}).get('descWeatherTypePT', 'N/A')
        icon_filename = f"w_ic_d_{weather_type_id:02d}anim.svg"
        icon_url = f"https://www.ipma.pt/bin/images/weather-symbols/{icon_filename}"

        proximos_5_dias.append({
            'data': data,
            'min_temp': min_temp,
            'max_temp': max_temp,
            'descricaoTempo': weather_description,
            'icon_url': icon_url
        })

    context = {
        'cidade': 'Lisboa',
        'previsao_proximos_5_dias': proximos_5_dias
    }

    return render(request, 'meteo/previsao.html', context)

def index_view(request):
    return render(request, 'meteo/index.html')

def api_documentation(request):
    return render(request, 'meteo/api_documentation.html')
