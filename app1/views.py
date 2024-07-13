from django.shortcuts import render

# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt
from decouple import config

@csrf_exempt
def weather_forecast(request):
    place = None
    if request.method == "POST":
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        print(latitude,longitude)
        api_key = config('weather_api_key')
        print(api_key)
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        print(data)
        if data.get('name'):
            # temperature = data['main']['temp']
            place = data['name']
            # print("temperature",temperature)
            print("place",place)
            
    return render(request, 'weather_forecast.html',{'place':place})