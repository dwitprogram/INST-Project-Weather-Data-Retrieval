"""
Name: Dwight Guevara
Date: 12/10/2025
Project: Weather Data Retrieval
"""
import requests
import pandas as pd
from datetime import date, timedelta # Used for date manipulation to get last 7 days of current date

API_Key= '752fd0accb0e4626b2362921251912' #API key provided by weatherapi.com

url= f"http://api.weatherapi.com/v1" #base URL for the weather API
def get_current_weather(city):
    """
    
    """
    formed_url= f"http://api.weatherapi.com/v1/current.json?key={API_Key}&q={city}" #base URL for current weather data
    response=requests.get(formed_url)
    if response.status_code !=200:
        print("Error: Unable to retrieve data")
        return None
    data = response.json()
    return {
        "city": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "temp_f": data["current"]["temp_f"],
        "humidity": data["current"]["humidity"],
        "condition": data["current"]["condition"]["text"]
    }
def get_last_7_days(city):
    """
    
    """
    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=6)
    formed_url= f"http://api.weatherapi.com/v1/history.json?key={API_Key}&q={city}&dt={start_date.isoformat()}&end_dt={end_date.isoformat()}" #base URL for weekly weather data
    response=requests.get(formed_url)
    if response.status_code !=200:
        print(response.status_code)
        print("Error: Unable to retrieve data")
        return None
    data = response.json()
    rows = []
    for day in data["forecast"]["forecastday"]:
        rows.append({
            "date": day["date"],
            "max_temp": day["day"]["maxtemp_f"],
            "min_temp": day["day"]["mintemp_f"],
            "avg_temp": day["day"]["avgtemp_f"]
        })
    df=pd.DataFrame(rows)
    return df
    
def get_hottest_coldest_days(city):
    """
    
    """
    formed_url= f"http://api.weatherapi.com/v1/history.json?key={API_Key}&q={city}" #base URL for weekly weather data
    response=requests.get(formed_url)
    if response.status_code !=200:
        print(response.status_code)
        print("Error: Unable to retrieve data")
        return None
    data = response.json()
    return {
        "city": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "hottest_day": data["forecast"]["forecastday"][0]["day"]["maxtemp_f"],
        "coldest_day": data["forecast"]["forecastday"][0]["day"]["mintemp_f"]
    }
print("Welcome to the weather data retrieval program!") # Welcome message
print("This program retrieves weather data via API calls")
print("Please choose a choice from the following options:")
print("1. Retrieve current weather data for a specific city")
print("2. Retrieve last 7 days of weather data for a specific city")
print("3. Hottest and coldest days for a specific city")
choice=input("Enter your choice (1, 2, or 3): ") #user input for the choice

city=input("Enter the name of the city: ") #user input for the city name

while choice not in ["1", "2", "3"]:
    print("Invalid choice. Please enter 1, 2, or 3")
    choice=input("Enter your choice (1, 2, or 3): ") #user input for the choice1+
if choice == "1":
    result=get_current_weather(city)
    if result:
        df=pd.DataFrame([result])
        print(df)
elif choice == "2":
    result=get_last_7_days(city)
    if result is not None and not result.empty:
        print(result)
elif choice == "3":
    get_hottest_coldest_days(city)




