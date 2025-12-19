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
    Calls Api to get current weather data for a specific city
    
    Args:
        city (str): The name of the city for which to retrieve the current weather data.
    Returns:
        pandas.Dataframe: Dataframe containing the current weather data for the specified city.
    """
    formed_url= f"http://api.weatherapi.com/v1/current.json?key={API_Key}&q={city}" #base URL for current weather data
    response=requests.get(formed_url) #make API call to get current weather data
    if response.status_code !=200: #check if API call was successful
        print(response.status_code) # Print the status code if the API call failed
        print("Error: Unable to retrieve data") # Print an error message if the API call failed
        return None # Return None if the API call failed
    data = response.json() # Parse the JSON response/ bridges the Json data into a dictionary
    current_weather={ # Create a dictionary with the relevant weather data
        "city": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "temp_f": data["current"]["temp_f"],
        "humidity": data["current"]["humidity"],
        "condition": data["current"]["condition"]["text"]
    }
    df=pd.DataFrame([current_weather])# Convert the dictionary to a pandas dataframe
    return df # Return the dataframe containing the current weather data
def get_last_7_days(city):
    """
    Calls Api to get weather data for the last 7 days for a specific city.
    Args:
        city (str): The name of the city for which to retrieve the current weather data.
    Returns:
        pandas.Dataframe: Dataframe containing the weather data for the last 7 days for the specified city.
    """
    end_date = date.today() - timedelta(days=1) # Get the current date minus one day ()
    start_date = end_date - timedelta(days=6) # Get the date 7 days ago from the current date
    formed_url= f"http://api.weatherapi.com/v1/history.json?key={API_Key}&q={city}&dt={start_date.isoformat()}&end_dt={end_date.isoformat()}" #base URL for weekly weather data
    response=requests.get(formed_url) #make API call to get last 7 days of weather data
    if response.status_code !=200: #check if API call was successful
        print(response.status_code) # Print the status code if the API call failed
        print("Error: Unable to retrieve data") # Print an error message if the API call failed
        return None # Return None if the API call failed
    data = response.json()# Parse the JSON response/ bridges the Json data into a dictionary
    rows = [] # Create a list to store the weather data for each day
    for day in data["forecast"]["forecastday"]: # Loop through the weather data for each day
        rows.append({ # Create a dictionary with the relevant weather data for each day
            "date": day["date"],
            "max_temp": day["day"]["maxtemp_f"],
            "min_temp": day["day"]["mintemp_f"],
            "avg_temp": day["day"]["avgtemp_f"]
        })
    df=pd.DataFrame(rows) # Convert the list of dictionaries to a pandas dataframe
    return df # Return the dataframe containing the weather data for the last 7 days
    
def get_hottest_coldest_days(city):
    """
    Calls Api to get the hottest and coldest days for the last 7 days for a specific city.
    Args:
        city (str): The name of the city for which to retrieve the current weather data.
    Returns:
        pandas.Dataframe: Dataframe containing the hottest and coldest days for the last 7 days for the specified city.
    """
    end_date = date.today() - timedelta(days=1) # Get the current date minus one day for consistency purposes
    start_date = end_date - timedelta(days=6) # Get the date 7 days ago from the current date
    formed_url= f"http://api.weatherapi.com/v1/history.json?key={API_Key}&q={city}&dt={start_date.isoformat()}&end_dt={end_date.isoformat()}" #base URL for weekly weather data
    response=requests.get(formed_url) #make API call to get last 7 days of weather data
    if response.status_code !=200: #check if API call was successful
        print(response.status_code) # Print the status code if the API call failed
        print("Error: Unable to retrieve data") # Print an error message if the API call failed
        return None # Return None if the API call failed
    data = response.json() # Parse the JSON response/ bridges the Json data into a dictionary
    minmax_weather={"city": data["location"]["name"], # Create a dictionary with the relevant weather data
    "region": data["location"]["region"],
    "country": data["location"]["country"],
    "hottest_day": data["forecast"]["forecastday"][0]["day"]["maxtemp_f"],
    "coldest_day": data["forecast"]["forecastday"][0]["day"]["mintemp_f"]}
    df=pd.DataFrame([minmax_weather]) # Convert the dictionary to a pandas dataframe
    return df # Return the dataframe containing the weather data for the last 7 days with the hottest and coldest days
        
print("Welcome to the weather data retrieval program!") # Welcome message
print("This program retrieves weather data via API calls")
print("Please choose a choice from the following options:") # Options for the user to choose from
print("1. Retrieve current weather data for a specific city")
print("2. Retrieve last 7 days of weather data for a specific city")
print("3. Hottest and coldest days for a specific city")
choice=input("Enter your choice (1, 2, or 3): ") #user input for the choice
city=input("Enter the name of the city: ") #user input for the city name

while choice not in ["1", "2", "3"]:
    print("Invalid choice. Please enter 1, 2, or 3")
    choice=input("Enter your choice (1, 2, or 3): ") #user input for the choice1+
if choice == "1": # Retrieve current weather data for a specific city
    result=get_current_weather(city) # Call the function to get the current weather data
    if result is not None and not result.empty: # Check if the result is not None and not empty
        print(result)
elif choice == "2": # Retrieve last 7 days of weather data for a specific city
    result=get_last_7_days(city) # Call the function to get the last 7 days of weather data
    if result is not None and not result.empty: # Check if the result is not None and not empty
        print(result)
elif choice == "3": # Retrieve hottest and coldest days for a specific city
    result=get_hottest_coldest_days(city) # Call the function to get the hottest and coldest days
    if result is not None and not result.empty: # Check if the result is not None and not empty
        print(result)
        
