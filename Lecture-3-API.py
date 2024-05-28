import requests

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
API_KEY = 'your_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Function to fetch weather data for a given city
def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Check if the API call was successful
    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_data
    else:
        print(f"Error: {data['message']}")
        return None

# Example usage
city = 'London'
weather_info = fetch_weather(city)

if weather_info:
    print(f"Weather data for {city}:")
    print(weather_info)
else:
    print("Failed to retrieve weather data.")
