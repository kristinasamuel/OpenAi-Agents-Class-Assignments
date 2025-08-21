#  create a weather tool to fetch the real time weather updates
import requests
import os
from agents import function_tool

# Load API Key from environment variable
API_KEY = os.getenv("WEATHER_API_KEY")

@function_tool
def get_weather(city: str) -> str:
    print("<<<<<< Weather Tool Call >>>>>.")
    # use try except for better error handling
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Return formatted string
        return f"Weather in {city}: {data['current']['temp_c']}°C, {data['current']['condition']['text']}"

    except Exception as e:
        return f"Error while fetching weather data: {e}"

        # Return formatted string
        return f"Weather in {city}: {data['current']['temp_c']}°C, {data['current']['condition']['text']}"

    except Exception as e:
        return f"Error while fetching weather data: {e}"
