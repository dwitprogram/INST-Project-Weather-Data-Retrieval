"""
Name: Dwight Guevara
Date: 12/10/2025
Project: Weather Data Retrieval
"""
import requests
import pandas as pd

API_Key= '752fd0accb0e4626b2362921251912' #API key provided by weatherapi.com
url= f"http://api.weatherapi.com/v1" #base URL for the weather API
city=input("Enter the name of the city: ") #user input for the city name
formed_url= f"{url}/current.json?key={API_Key}&q={city}" #formed URL with the city name and API key
def get_weather_data(city):
    """
    Takes API key and city name as input and returns the current weather data for the specified city.
    
    :param city: User input for the city name.
    :return: Current weather data for the specified city.
    """
    response=requests.get(f"{formed_url}")
    
    if response.status_code== 200:
        data = response.json()
        weather = {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "temp_f": data["current"]["temp_f"],
            "humidity": data["current"]["humidity"],
            "condition": data["current"]["condition"]["text"]
            }
        return weather
weather_data = get_weather_data(city)
if weather_data:
    df = pd.DataFrame([weather_data])
    print(df)
