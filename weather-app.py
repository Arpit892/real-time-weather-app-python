import requests 

try:
    city_name = input("enter city name: ")
    api_key = "your-api-key"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    weather_data = requests.get(api_url)


    data = weather_data.json()
    weather = data.get('weather', [{}])[0].get('main', '')
    description = data.get('weather', [{}])[0].get('description', '')
    temp = data.get('main', {}).get('temp', '')
    feels_like = data.get('main', {}).get('feels_like', '')
    humidity = data.get('main', {}).get('humidity', '')
    wind = data.get('wind', {}).get('speed', '')
except Exception as e:
    city_name = "unknown"
    weather = "NA"
    description = "NA"
    temp = "NA"
    feels_like = "NA"
    humidity = "NA"
    wind = "NA"

print(f"\n🌍 Weather in {city_name.capitalize()}:")
print(f"🌡️ Temperature: {temp}°C (feels like {feels_like}°C)")
print(f"☁️ condition: {description}")
print(f"💧 humidity: {humidity}%")
print(f"🍃 wind_speed: {wind}m/s")