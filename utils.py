import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API = os.getenv("WEATHER_API")
NEWS_API = os.getenv("NEWS_API")

async def fetch_json(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            return await response.json()
    except Exception as e:
        return {"error": str(e)}

async def fetch_weather(session, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric"
    data = await fetch_json(session, url)
    if "error" in data:
        return f"Weather fetch error: {data['error']}"
    main = data.get("main", {})
    weather = data.get("weather", [{}])[0]
    temp = main.get("temp")
    desc = weather.get("description", "No description")
    if temp is not None:
        return f"{temp}°C, {desc}"
    return "Weather data unavailable"

async def fetch_news(session, city):
    url = f"https://newsapi.org/v2/everything?q={city}&apiKey={NEWS_API}"
    data = await fetch_json(session, url)
    if "error" in data:
        return f"News fetch error: {data['error']}"
    articles = data.get("articles", [])
    if articles:
        return articles[0].get("title", "No title available")
    return "No news articles found for this city."

async def fetch_joke(session):
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    data = await fetch_json(session, url)
    if data.get("error") is True:
        return "Joke fetch error"
    return data.get("joke", "No joke today 😅")
