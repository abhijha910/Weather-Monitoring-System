import requests
from config import API_KEY, COUNTRY_CODE

def get_weather_data(city):
    """Fetch weather data for the given city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code} - {response.json().get('message')}")
        return None
