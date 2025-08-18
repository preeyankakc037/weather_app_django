from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    
    else: 
        city='kathmandu'

    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8725e0e43104c5b14b0807b163e3f7ce' 
    PARAMS = {'units': 'metrics'}
   # This will convert temp in cesius and farenhit 
    return render (request, 'home.html')

