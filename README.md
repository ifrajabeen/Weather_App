# 🌦️ Advanced Weather Dashboard with Real-Time AQI

A modern, responsive, and feature-rich weather application built using **Python (Flask)** and the **OpenWeatherMap API**. This dashboard provides deep insights into current weather conditions and air quality with a dynamic, living UI.

---

## ✨ Key Features

* **Real-Time Data:** Accurate temperature, "Feels Like" conditions, humidity, and wind speed.
* **Air Quality Index (AQI) 🍃:** Integrated pollution tracking to monitor environmental safety—essential for health awareness in urban areas.
* **Dynamic Backgrounds:** The UI theme intelligently adapts (Rainy, Sunny, Cloudy, etc.) based on the current weather condition using CSS-to-JS binding.
* **Comprehensive Forecasts:**
    * **Hourly Ribbon:** A detailed 24-hour outlook.
    * **5-Day Outlook:** Daily high/low temperatures and weather descriptions.
* **Robust Error Handling:** Custom-designed "City Not Found" experience to handle invalid searches gracefully.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask
* **Server:** Waitress (Production-ready WSGI)
* **Frontend:** HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6+)
* **Data Source:** OpenWeatherMap API

---

## 📂 Project Structure

```text
weather_app/
├── server.py           # Main Flask application and routing
├── weather.py          # API logic for Weather and AQI data
├── .env                # API Keys (Excluded from Git for security)
├── requirements.txt    # List of dependencies
├── static/
│   └── styles/
│       └── style.css   # Dynamic themes and layouts
└── templates/          # HTML pages (Index, Weather, Error)
```
## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ifrajabeen/Weather_App.git](https://github.com/ifrajabeen/Weather_App.git)
   cd Weather_App
2. **Install Dependencies:**
3. **API Configuration: Create a .env file in the root directory and add your API key:**
4. **Run the App:**

## ⚠️ Error Handling & Security
The project includes multi-layer validation to ensure a smooth user experience and data safety:

**Backend Check:** API response codes are verified to redirect users to a custom error page if a city isn't found.

**Input Validation:** A fallback mechanism is in place for empty or invalid searches to prevent app crashes.

**Security:** Use of .gitignore ensures that sensitive API keys (.env) and virtual environments (.venv) are never exposed to the public.

Developed by Ifra Jabeen
