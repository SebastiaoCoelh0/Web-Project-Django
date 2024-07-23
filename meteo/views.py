from datetime import datetime

import requests
from django.http import JsonResponse
from django.shortcuts import render


def get_weather_data(global_id_local):
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json"
    response = requests.get(url)
    return response.json()


def get_city_list():
    url = "https://api.ipma.pt/open-data/distrits-islands.json"
    response = requests.get(url)
    return response.json()


def get_wind_details():
    url = "https://api.ipma.pt/open-data/wind-speed-daily-classe.json"
    response = requests.get(url)
    return response.json()


def get_weather_type_classes():
    url = "https://api.ipma.pt/open-data/weather-type-classe.json"
    response = requests.get(url)
    return response.json()


def index_view(request):
    cities_data = get_city_list()
    cities = cities_data['data']
    context = {'cities': cities}
    return render(request, 'meteo/index.html', context)


def previsao_view(request):
    city_id = request.GET.get('city_id')
    if not city_id:
        return render(request, 'meteo/previsao.html', {'error': 'No city selected.'})

    days = []
    types = {}
    wind_details = {}
    wind_data_raw = get_wind_details()
    wind_data = wind_data_raw['data']
    weather_data_raw = get_weather_data(city_id)
    weather_data = weather_data_raw['data']
    weather_types_raw = get_weather_type_classes()
    weather_types = weather_types_raw['data']

    for wind_type in wind_data:
        wind_details[wind_type['classWindSpeed']] = wind_type['descClassWindSpeedDailyEN']
    for weather_type in weather_types:
        types[weather_type['idWeatherType']] = weather_type['descWeatherTypeEN']
    for day in weather_data:
        day['weatherType'] = types[day['idWeatherType']]
        day['windSpeed'] = wind_details[str(day['classWindSpeed'])]
        if day['idWeatherType'] < 10:
            day['image'] = f"/static/meteo/w_ic_d_0{day['idWeatherType']}anim.svg"
        else:
            day['image'] = f"/static/meteo/w_ic_d_{day['idWeatherType']}anim.svg"
        # print(day['image'])
        day['forecastDate'] = datetime.strptime(day['forecastDate'], '%Y-%m-%d')
        days.append(day)

    context = {
        'city': search_for_city_name(city_id),
        'days': days,
    }
    return render(request, 'meteo/previsao.html', context)


def search_for_city_name(city_id):
    cities_data = get_city_list()
    cities = cities_data['data']

    for city in cities:
        if int(city['globalIdLocal']) == int(city_id):
            return city['local']
    return 'Cidade não encontrada'


def lisboa_view(request):
    city_id = 1110600  # ID para Lisboa
    weather_data_raw = get_weather_data(city_id)
    weather_types_raw = get_weather_type_classes()

    if 'data' in weather_data_raw and len(weather_data_raw['data']) > 0:
        today_weather = weather_data_raw['data'][0]  # Obter a previsão de hoje
        weather_types = {item['idWeatherType']: item for item in weather_types_raw['data']}
        today_weather['weatherType'] = weather_types[today_weather['idWeatherType']]['descWeatherTypePT']
        if today_weather['idWeatherType'] < 10:
            today_weather['image'] = f"/static/meteo/w_ic_d_0{today_weather['idWeatherType']}anim.svg"
        else:
            today_weather['image'] = f"/static/meteo/w_ic_d_{today_weather['idWeatherType']}anim.svg"
        # print(today_weather['image'])
        today_weather['forecastDate'] = datetime.strptime(today_weather['forecastDate'], '%Y-%m-%d').strftime(
            '%Y-%m-%d')
    else:
        today_weather = {}

    context = {
        'city': 'Lisboa',
        'weather': today_weather,
    }
    return render(request, 'meteo/lisboa.html', context)


def api_view(request):
    return render(request, 'meteo/api.html')


def avisos_meteorologicos_view(request):
    url = "https://api.ipma.pt/open-data/forecast/warnings/warnings_www.json"
    response = requests.get(url)
    data = response.json()
    filtered_data = [
        {
            "text": item["text"],
            "awarenessTypeName": item["awarenessTypeName"],
            "idAreaAviso": item["idAreaAviso"],
            "startTime": item["startTime"],
            "awarenessLevelID": item["awarenessLevelID"],
            "endTime": item["endTime"]
        }
        for item in data
        if item["awarenessLevelID"] in ["yellow", "orange", "red"]
    ]
    return JsonResponse(filtered_data)

def informacao_sismicidade_view(request, idArea):
    url = f"https://api.ipma.pt/open-data/observation/seismic/{idArea}.json"
    response = requests.get(url)
    data = response.json()
    filtered_data = [
        {
            "time": item["time"],
            "local": item["local"],
            "lat": item["lat"],
            "lon": item["lon"],
            "magnitud": item["magnitud"],
            "magType": item["magType"],
            "degree": item["degree"],
            "dataUpdate": item["dataUpdate"],
            "obsRegion": item["obsRegion"],
            "depth": item["depth"]
        }
        for item in data["data"]
    ]
    return JsonResponse(filtered_data)

def observacao_meteorologica_view(request):
    url = "https://api.ipma.pt/open-data/observation/meteorology/stations/observations.json"
    response = requests.get(url)
    data = response.json()
    filtered_data = []
    for date_time, stations in data.items():
        for station_id, measurements in stations.items():
            filtered_data.append({
                "dateTime": date_time,
                "stationId": station_id,
                **measurements
            })
    return JsonResponse(filtered_data)