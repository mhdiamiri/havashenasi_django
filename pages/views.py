from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


def index(request):
    city = ''
    text = ''
    if 'city_name' in request.GET:
        city = request.GET['city_name']
        text = getinfo(city)
    
    context = {
        "result" : text,

    }

    return render(request, 'index.html', context=context)

def getinfo(city_name):
    text = ''
    response = requests.get('https://api.codebazan.ir/weather/?city=%s'%(city_name))
    ok = (response.json()["result"]['استان'] != 'null')

    if ok:
        keys = ["result", "فردا", "شنبه", "یک شنبه", "دوشنبه", "سه شنبه", "چهار شنبه", "پنج شنبه", "آدینه"]
        for key in keys:
            try:
                res = response.json()[key]
                if key != 'result' : text += (key+':'+'\n')
            except:
                break
            for title in res:
                text += str(title)+": "+str(res[title])+"\n"
            text += '\n'
        return text
    else:
        return 'پیدا نشد!'    
