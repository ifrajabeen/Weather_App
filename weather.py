import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

load_dotenv()

def get_current_weather(city="Karachi"):
    api_key = os.getenv("API_KEY")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    data = requests.get(request_url).json()

    
    if str(data.get('cod')) == "200":
        # Convert API timestamp to Pakistan Time (UTC+5)
        utc_dt = datetime.fromtimestamp(data['dt'], tz=timezone.utc)
        pk_time = utc_dt + timedelta(hours=5) 
        
        data['date'] = pk_time.strftime('%a, %b %d')
        data['time'] = pk_time.strftime('%I:%M %p')
        
    return data

def get_weather_forecast(city="Karachi"):
    api_key = os.getenv("API_KEY")
    request_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    data = requests.get(request_url).json()

    forecast_list = []
    seen_dates = []
    
    # Get Today's date in Pakistan to filter it out from forecast
    pk_today = (datetime.now(timezone.utc) + timedelta(hours=5)).strftime('%Y-%m-%d')

    if str(data.get('cod')) == "200":
        for item in data['list']:
            date_str = item['dt_txt'].split(' ')[0]

            # Logic: Skip today because it's already in the 'Current' section
            # Only pick one entry per day for the next 5 days
            if date_str > pk_today and date_str not in seen_dates:
                date_obj = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')
                
                forecast_list.append({
                    "date": date_obj.strftime('%a, %b %d'),
                    "temp": f"{item['main']['temp']:.1f}",
                    "description": item['weather'][0]['description'].capitalize(),
                    "icon": item['weather'][0]['icon']
                })
                seen_dates.append(date_str)

            if len(forecast_list) == 5:
                break
                
    return forecast_list
def get_hourly_forecast(city="Karachi"):
    api_key = os.getenv("API_KEY")
    request_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    data = requests.get(request_url).json()
    hourly_list = []
    if str(data.get('cod')) == "200":
        for item in data['list'][:8]:
          dt_obj = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')

          hourly_list.append({
              "time": dt_obj.strftime('%I %p'),
              "temp": f"{item['main']['temp']:.1f}",
              "icon": item['weather'][0]['icon'],
              "condition": item['weather'][0]['main']
          })
    return hourly_list
def get_air_quality(lat, lon):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    
    response = requests.get(url).json()
    
    if "list" in response:
        aqi_value = response["list"][0]["main"]["aqi"]
        # AQI levels mapping
        aqi_desc = {
            1: "Good 😊",
            2: "Fair 😐",
            3: "Moderate 😷",
            4: "Poor 🤢",
            5: "Very Poor 🚨"
        }
        return aqi_desc.get(aqi_value, "Unknown")
    return "N/A"
if __name__ == "__main__":
    city = input("\nPlease enter a city name: ")
    if not bool(city.strip()):
        city = "Karachi"
    print("\n---- Current Weather ----")
    print(get_current_weather(city))
    print("\n---- 5-Day Forecast ----")
    print(get_weather_forecast(city))