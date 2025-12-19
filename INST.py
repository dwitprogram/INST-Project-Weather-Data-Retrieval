"""
Name: Dwight Guevara
Date: 12/10/2025
Project: Weather Data Retrieval
"""
import requests
import pandas as pd

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
def get_weekly_avg_temp(city):
    """
    
    """
    formed_url= f"http://api.weatherapi.com/v1/history.json?key={API_Key}&q={city}" #base URL for weekly weather data
    response=requests.get(formed_url)
    if response.status_code !=200:
        print("Error: Unable to retrieve data")
        return None
    data = response.json()
    return {
        "city": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "avg_temp_f": data["forecast"]["forecastday"][0]["day"]["avgtemp_f"]
    }        
def get_hottest_coldest_days(city):
    """
    
    """
    formed_url= f"http://api.weatherapi.com/v1/history.json?key={API_Key}&q={city}" #base URL for weekly weather data
    response=requests.get(formed_url)
    if response.status_code !=200:
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
print("2. Weekly average temperature for a specific city")
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
    get_weekly_avg_temp(city)
elif choice == "3":
    get_hottest_coldest_days(city)




