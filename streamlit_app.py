import streamlit as st
import asyncio
import aiohttp
from utils import fetch_weather, fetch_news, fetch_joke

st.title("🧩 Daily Dashboard")

city = st.text_input("Enter your city")

if city:
    async def main():
        async with aiohttp.ClientSession() as session:
            weather, news, joke = await asyncio.gather(
                fetch_weather(session, city),
                fetch_news(session, city),
                fetch_joke(session)
            )
            st.subheader("🌤 Weather")
            st.write(weather)

            st.subheader("📰 News")
            st.write(news)

            st.subheader("😂 Joke")
            st.write(joke)

    asyncio.run(main())
