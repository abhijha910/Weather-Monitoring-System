# Weather Monitoring System

## Overview
The Weather Monitoring System is a real-time data processing system that retrieves and analyzes weather data from the OpenWeatherMap API. It provides summarized insights and alerts based on configurable thresholds.

## Functionality Overview

### Weather Data Retrieval
The system continuously calls the OpenWeatherMap API to fetch weather data for specific cities (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad). The fetched data includes temperature, weather condition, and more.

### Rollups and Aggregates
Daily weather summary: The system calculates daily aggregates for each city, including:
- Average temperature
- Maximum and minimum temperature
- Dominant weather condition (based on most frequent occurrence)

**Storage:** Daily summaries are stored in the database for future analysis.

### Alerting System
The user can set configurable thresholds (e.g., alert if the temperature exceeds 35°C). Alerts are triggered when the thresholds are breached and are displayed on the console (or through email, if configured).

### Visualizations
The system provides visualizations of daily weather summaries, historical trends, and alerts using libraries like Matplotlib.

## Features
- Real-time weather data retrieval for major metros in India.
- Daily weather summary with average, maximum, and minimum temperatures.
- Alerting system for extreme weather conditions.
- Visualizations of weather data trends.

## Search Functionality

### Example Searches

1. **Searching for Delhi:**
   - **Input**: `Delhi`
   - **Output**: `Delhi: 25.30°C, Clear`
   - ![Delhi Search Result](Project Snapshots/Search%20City%20Delhi.png)  <!-- Correctly formatted for spaces in file name -->

2. **Searching for Kolkata:**
   - **Input**: `Kolkata`
   - **Output**: `Kolkata: 28.75°C, Clouds`
   - ![Kolkata Search Result](Project Snapshots/Search%20Valid%20City%20Kolkata.png)  <!-- Correctly formatted for spaces in file name -->

3. **Searching for a Non-Existent City:**
   - **Input**: `NotACity`
   - **Output**: `City not found`
   - ![City Not Found](Project Snapshots/Search%20Wrong%20City.png)  <!-- Correctly formatted for spaces in file name -->


## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/weather_monitoring_system.git

2. Navigate to the project directory:

   ```bash
    cd weather_monitoring_system

3. Create and activate a virtual environment:

   ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    
4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    
5. Configure your API keys in config.py.
   
   ## Run the application:

    ```bash
    python src/main.py

## Authors
Abhyanand Jha - abhyanandlsc@gmail.com
