from django.shortcuts import render
import requests

# Create your views here.

from elsys.models import Car
from api.serializers import CarSerializer
from django.http import JsonResponse

def about(request):
    return render(request, 'about.html')

def cars_json(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many = True)
    return JsonResponse({'data': serializer.data }, safe=False)

def trains(request):
    url = 'https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Cvehicle%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north'
    a = requests.get(url).json()

    data = []
    for i in a['data']:
        train = {}
        train['time'] = i['attributes']['departure_time']

        id = i['relationships']['trip']['data']['id']
        for y in a['included']:
            if y['id'] == id:
                train['destination'] = y['attributes']['headsign']

        if i['relationships']['vehicle']['data'] is None:
            train['vehicle'] = 'None'
        else:
            for y in a['included']:
                if y['id'] == i['relationships']['vehicle']['data']['id']:
                    train['vehicle'] = y['attributes']['label']

        train['track'] = 'TDB'

        train['status'] = i['attributes']['status']
        data.append(train)


    return render(request, 'trains.html', {'data': data})

