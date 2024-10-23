# src/main.py
import time
import pandas as pd
from weather_data import get_weather_data
from data_processing import process_weather_data, daily_summary
from alerting import check_thresholds
from visualization import plot_weather_summary
from config import METROS, CHECK_INTERVAL

def main():
    all_data = []
    
    while True:
        weather_data = [get_weather_data(city) for city in METROS]
        processed_df = process_weather_data(weather_data)
        
        if not processed_df.empty:
            all_data.append(processed_df)
            daily_df = pd.concat(all_data)
            
            # Calculate daily summary
            summary = daily_summary(daily_df)
            print(summary)
            
            # Check thresholds for alerts
            check_thresholds(summary)
            
            # Visualize the summary
            plot_weather_summary(summary)
        
        time.sleep(CHECK_INTERVAL)  # Wait for the next interval

if __name__ == "__main__":
    city = "Delhi"  # Replace with any city of your choice
    weather_data = get_weather_data(city)
    print(weather_data)  # This will print the weather data for Delhi
