from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    # Get the city name from the form POST request; if not provided, use 'paris' by default
    city = request.POST.get('city', 'paris')

    # OpenWeatherMap API URL (fetches weather data)
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8725e0e43104c5b14b0807b163e3f7ce'
    PARAMS = {'units': 'metric'}  # Fetch temperature in Celsius

    # Google Custom Search API for fetching city images
    API_KEY = 'AIzaSyDmMzc9Z3x0XGPp0WqNDYLzhyJAVC_ytjM'
    SEARCH_ENGINE_ID = 'e5813a7765ecd46ac'
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    # Default fallback image
    image_url = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

    try:
        # Fetch image data from Google Custom Search API
        image_data = requests.get(city_url).json()
        search_items = image_data.get("items")
        if search_items:
            image_url = search_items[0]['link']
    except Exception:
        pass  # If image API fails, we already have a fallback image

    try:
        # Fetch weather data
        weather_data = requests.get(url, params=PARAMS).json()

        # If API returns an error (like "city not found"), handle it
        if weather_data.get('cod') != 200:
            raise KeyError("City not found in weather API")

        # Extract weather details
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.date.today()

        # Send weather data to template
        return render(
            request,
            'home.html',  # ✅ Always use home.html
            {
                'description': description,
                'icon': icon,
                'temp': temp,
                'day': day,
                'city': city,
                'exception_occurred': False,
                'image_url': image_url
            }
        )

    except KeyError:
        # Handle invalid city gracefully
        exception_occurred = True
        messages.error(request, f"Sorry, weather data for '{city}' is not available.")
        day = datetime.date.today()

        # Fallback weather data (for Paris)
        return render(
            request,
            'home.html',  # ✅ FIXED: Use home.html instead of weatherapp/home.html
            {
                'description': 'clear sky',
                'icon': '01d',
                'temp': 25,
                'day': day,
                'city': 'paris',
                'exception_occurred': exception_occurred,
                'image_url': image_url
            }
        )
