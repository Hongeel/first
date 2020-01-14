from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def index(request): #Собственно функция общения с api
    appid = '24cdb9b2884a4a14a8aa6d35d9cd5ed9' # апи кей
    url = 'https://api.weatherbit.io/v2.0/current?city={},RU&key=' + appid # url запроса

    city = 'Москва' # город по умолчанию, в запросе встает в {}
    if(request.method == 'POST'): # ловушка на POST запрос, если в форме выбрать город и отправить запрос, то этот запрос будет пойман данным условием и переменная city будет переназначена
        city = request.POST.get('city')
    res = requests.get(url.format(city)).json()

    city_info = { # берем из ответа API Json нужные нам данные
        'city': city,
        'temp': res['data'][0]['temp'],
        'app_temp': res['data'][0]['app_temp']
    }

    context = {'info': city_info} # собираем данные в одну переменную в виде списка

    return render(request, 'weather/index.html', context) # возвращаем получившиеся в функции данные в память сервера. 
    # в дальнейшем вызываем эти данные в html файле командами {{ info.city}}, {{ info.temp }} и тд.