import requests

def get_weather(api_key, city, country_code=""):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f"{city},{country_code}",
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        main_info = weather_data['main']
        weather_info = weather_data['weather'][0]
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Description: {weather_info['description']}")
        print(f"Temperature: {main_info['temp']}°C")
        print(f"Humidity: {main_info['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    
    api_key = 'YOUR_API_KEY'
    city_name = input("Enter the city name: ")
    country_code = input("Enter the country code (optional, press Enter to skip): ")

    weather_data = get_weather(api_key, city_name, country_code)
    display_weather(weather_data)
