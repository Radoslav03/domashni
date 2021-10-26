from django.shortcuts import render
import requests

def home(request):
    url = 'https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Cvehicle%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north'
    a = requests.get(url).json()
    # нищо не се подразбира под дефиницията 'a' - можеше да е нещо като data или response

    # data е много общопонятно име за това, което искам да върнем като лист от речници
    data = []
    # бих предложил името да е по-насочено към предмета на информация - например train_datalist

    for i in a['data']:
        train = {}
        train['time'] = i['attributes']['departure_time']
        # Това не работи - показва None в резултат
        # departure_time на влака се намира чрез schedule_id в included

        id = i['relationships']['trip']['data']['id']
        # отново не се подразбира каква информация съдържа това id
        for y in a['included']:
            if y['id'] == id:
                train['destination'] = y['attributes']['headsign']

        if i['relationships']['vehicle']['data'] is None:
            train['vehicle'] = 'None'
        # Този if е безсмислен, както и полето за id на влака

        else:
            for y in a['included']:
                if y['id'] == i['relationships']['vehicle']['data']['id']:
                    train['vehicle'] = y['attributes']['label']

        # for циклите са супер - кратки и на място

        train['track'] = 'TDB' # безполезно и ненужно

        train['status'] = i['attributes']['status']
        data.append(train)


    return render(request, 'home.html',{'data': data})



