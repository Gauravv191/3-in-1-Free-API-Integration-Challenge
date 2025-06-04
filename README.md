# 🧩 Daily Dashboard

A simple Python-based dashboard that fetches and displays:
- 🌤 Weather for your city
- 📰 Latest news related to your city
- 😂 A random joke to lighten your day

Built using:
- `aiohttp` for asynchronous API requests
- `dotenv` for secure API key management
- `Streamlit` for a simple interactive UI

---

## 📦 Features

- Integrates **3 Public APIs**:
  - OpenWeatherMap (Weather)
  - NewsAPI (News)
  - JokeAPI (Random joke)
- Asynchronous API calls using `asyncio` + `aiohttp`
- Simple CLI or Streamlit UI
- .env support to keep your API keys secure
- Graceful error handling and data fallback

---

## 🚀 Installation

```bash
git clone https://github.com/Bhumesh2001/Daily_Dashboard.git
cd daily-dashboard
pip install -r requirements.txt

🔐 Environment Variables
Create a .env file in the project root:

WEATHER_API=your_openweathermap_api_key
NEWS_API=your_newsapi_key

You can register and get free API keys from:
https://openweathermap.org/api
https://newsapi.org/

🛠 Run the Project
🌐 Streamlit UI
streamlit run streamlit_app.py

🖥 CLI
python dashboard.py

🧪 Example Output (CLI)
🌤 Weather: 32°C, clear sky
📰 News: India, US agree to enhance defense ties in Indo-Pacific
😂 Joke: Why don't skeletons fight each other? They don't have the guts.

🧠 APIs Used
OpenWeatherMap
Docs: https://openweathermap.org/current

NewsAPI
Docs: https://newsapi.org/docs/endpoints/everything

JokeAPI
Docs: https://jokeapi.dev

✅ Bonus Features

Parallel API fetching using asyncio.gather
Custom error fallback messages
Easily extendable (add more API widgets in the UI)

📁 Project Structure
daily-dashboard/
│
├── dashboard.py        # Streamlit interface
├── streamlit_app.py       # CLI interface
├── utils.py               # API fetching logic
├── .env                   # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md

🙋‍♂️ Author
Bhumesh Kewat
🔗 LinkedIn(https://www.linkedin.com/in/bhumesh-kewat-backend-developer/)
