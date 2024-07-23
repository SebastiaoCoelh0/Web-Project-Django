# portfolio/views.py

import requests
from django.shortcuts import render


def landing_page_view(request):
    weather_icon = get_weather_icon()
    context = {'weather_icon': weather_icon}
    return render(request, 'portfolio/landing_page.html', context)

def videos_view(request):
    return render(request, 'portfolio/videos.html')

def get_weather_icon():
    # ID para Lisboa ou qualquer cidade que desejar
    city_id = 1110600
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json"
    response = requests.get(url)
    data = response.json()
    if 'data' in data and len(data['data']) > 0:
        today_weather = data['data'][0]
        weather_type = today_weather['idWeatherType']
        if weather_type < 10:
            return f"/static/meteo/w_ic_d_0{weather_type}anim.svg"
        else:
            return f"/static/meteo/w_ic_d_{weather_type}anim.svg"
    return "/static/meteo/w_ic_d_00anim.svg"  # Default icon
