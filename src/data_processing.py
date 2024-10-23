# src/data_processing.py
import pandas as pd
from datetime import datetime

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(weather_data):
    """Convert temperatures from Kelvin to Celsius and return a structured dataframe."""
    processed_data = []
    
    for city_data in weather_data:
        if city_data:
            city = city_data["name"]
            temp = kelvin_to_celsius(city_data["main"]["temp"])
            feels_like = kelvin_to_celsius(city_data["main"]["feels_like"])
            main = city_data["weather"][0]["main"]
            timestamp = datetime.utcfromtimestamp(city_data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
            
            processed_data.append([city, temp, feels_like, main, timestamp])
    
    df = pd.DataFrame(processed_data, columns=["City", "Temperature", "Feels Like", "Main", "Timestamp"])
    return df

def daily_summary(df):
    """Generate daily summary including average, max, min, and dominant condition."""
    summary = df.groupby("City").agg(
        avg_temp=("Temperature", "mean"),
        max_temp=("Temperature", "max"),
        min_temp=("Temperature", "min"),
        dominant_condition=("Main", lambda x: x.mode()[0])
    ).reset_index()

    return summary
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15 if kelvin else None
