"""
Mini Python Project: Combined Data from 3 Public APIs

APIs integrated:
- OpenWeatherMap (Weather) - requires free API key from https://openweathermap.org/api
- Quotable (Inspirational quotes) - no API key needed
- Official Joke API (Random jokes) - no API key needed

Output: CLI mini dashboard showing current weather for a specified city, a motivational quote, and a random joke.

Instructions:
1. Get a free API key from OpenWeatherMap and paste it in the API_KEY variable below.
2. Run this script with Python 3.
3. Enter your city name when prompted.
"""

import requests

def get_weather(city, api_key):
    """Fetch current weather for city from OpenWeatherMap."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        return (weather_desc, temp, feels_like, humidity)
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_quote():
    """Fetch a random inspirational quote from ZenQuotes API."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data[0]["q"], data[0]["a"]
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return None, None


def get_joke():
    """Fetch a random joke from Official Joke API."""
    url = "https://official-joke-api.appspot.com/jokes/random"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["setup"], data["punchline"]
    except Exception as e:
        print(f"Error fetching joke: {e}")
        return None, None

def main():
    API_KEY = "Your_Whether_API_Key"  # Replace with your key
    print("Welcome to the Mini API Dashboard!")
    city = input("Enter the city name for weather report: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    weather = get_weather(city, API_KEY)
    if weather is None:
        print("Failed to get weather data. Please check city name or API key.")
    else:
        weather_desc, temp, feels_like, humidity = weather
        print(f"\nWeather in {city.capitalize()}:")
        print(f"  Condition: {weather_desc}")
        print(f"  Temperature: {temp} °C (feels like {feels_like} °C)")
        print(f"  Humidity: {humidity}%")

    quote, author = get_quote()
    if quote:
        print(f"\nInspirational Quote:\n  \"{quote}\" — {author}")
    else:
        print("\nCould not fetch inspirational quote.")

    setup, punchline = get_joke()
    if setup:
        print(f"\nHere's a joke for you:\n  {setup}\n  {punchline}")
    else:
        print("\nCould not fetch a joke.")

if __name__ == "__main__":
    main()
