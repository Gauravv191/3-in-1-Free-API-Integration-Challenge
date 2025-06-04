import asyncio
import aiohttp
from utils import fetch_weather, fetch_news, fetch_joke


async def main():
    city = input("Enter your city name: ").strip()
    async with aiohttp.ClientSession() as session:
        weather, news, joke = await asyncio.gather(
            fetch_weather(session, city),
            fetch_news(session, city),
            fetch_joke(session)
        )
    print(f"🌤 Weather in {city}: {weather}")
    print(f"📰 Top News: {news}")
    print(f"😂 Joke of the Day: {joke}")

if __name__ == "__main__":
    asyncio.run(main())
