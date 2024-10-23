# src/config.py

API_KEY = "ab672d5049a426b7c0da994ae1d6e834"  # Replace with your actual API Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
METROS = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
COUNTRY_CODE = "IN"
CHECK_INTERVAL = 300  # Interval to call API (in seconds, 5 mins)

# Thresholds
TEMP_THRESHOLD = 35  # Degrees Celsius
ALERT_THRESHOLD = 2  # Breach threshold for consecutive updates
