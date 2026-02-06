from flask import Flask, render_template, request
# Import mein get_air_quality add kiya
from weather import get_current_weather, get_weather_forecast, get_hourly_forecast, get_air_quality
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Empty string check
    if not city or not city.strip():
        city = "Karachi"

    weather_data = get_current_weather(city)
    forecast_data = get_weather_forecast(city)
    hourly_data = get_hourly_forecast(city)

    # Check if API returned an error
    if str(weather_data.get('cod')) != "200":
        return render_template("city-not-found.html")

    # --- AQI Integration (lat/lon coordinates backend se hi nikal liye) ---
    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']
    aqi_status = get_air_quality(lat, lon)

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        date=weather_data.get('date'),
        time=weather_data.get('time'),
        icon=weather_data["weather"][0]["icon"],
        forecast=forecast_data,
        hourly=hourly_data,
        humidity=weather_data['main']['humidity'],
        wind_speed=weather_data['wind']['speed'],
        condition=weather_data["weather"][0]["main"].lower(),
        aqi=aqi_status  # Ye template mein AQI pass kar raha hai
    )

if __name__ == "__main__":
    print("Server starting on http://localhost:8000")
    serve(app, host="0.0.0.0", port=8000)