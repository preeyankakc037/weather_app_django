from django.shortcuts import render
import requests
import datetime

# Home view function that handles weather request
def home(request):
    # Check if user has submitted a city name via POST form
    if 'city' in request.POST:
        city = request.POST['city']   # take user input city
    else: 
        city = 'kathmandu'            # default city if no input given

    # Base URL of OpenWeatherMap API
    url = 'https://api.openweathermap.org/data/2.5/weather'

    # Parameters to be sent with the API request
    PARAMS = {
        'q': city,                                  # city name
        'appid': '8725e0e43104c5b14b0807b163e3f7ce', # your API key
        'units': 'metric'                            # return temp in Celsius
    }

    # Sending GET request to the weather API
    # requests.get() fetches the data, .json() converts response into Python dictionary
    data = requests.get(url, params=PARAMS).json()

    # Extract useful information from API response
    description = data['weather'][0]['description']  # weather condition (e.g., "clear sky")
    icon = data['weather'][0]['icon']               # icon ID for weather condition
    temp = data['main']['temp']                     # current temperature
    day = datetime.date.today()                     # current date

    # Send data to the template (home.html) for rendering
    return render(request, 'home.html', {
        'description': description, 
        'icon': icon, 
        'temp': temp, 
        'day': day,
        'city': city
    })
