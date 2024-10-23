import requests
import time
from datetime import datetime
from flask import Flask, jsonify, render_template, request
import sqlite3
import threading

app = Flask(__name__)

# Constants
API_KEY = "ab672d5049a426b7c0da994ae1d6e834"  # Replace with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
FETCH_INTERVAL = 300  # Fetch every 5 minutes
ALERT_THRESHOLD = 35  # Example threshold for temperature

# Database setup (SQLite)
DATABASE = 'weather_data.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
        city TEXT, 
        temp REAL, 
        feels_like REAL, 
        condition TEXT, 
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS alerts (
        city TEXT, 
        alert_message TEXT, 
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def fetch_weather(city):
    try:
        url = BASE_URL.format(city, API_KEY)
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            condition = data['weather'][0]['main']
            return {
                'city': city,
                'temp': temp,
                'feels_like': feels_like,
                'condition': condition
            }
        else:
            return None
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")
        return None

def save_weather_to_db(city, temp, feels_like, condition):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather_data (city, temp, feels_like, condition) VALUES (?, ?, ?, ?)",
                   (city, temp, feels_like, condition))
    conn.commit()
    conn.close()

def check_alerts(city, temp):
    if temp > ALERT_THRESHOLD:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        alert_message = f"Alert: Temperature in {city} exceeds {ALERT_THRESHOLD}°C"
        cursor.execute("INSERT INTO alerts (city, alert_message) VALUES (?, ?)", (city, alert_message))
        conn.commit()
        conn.close()
        print(alert_message)

def process_weather():
    while True:
        for city in CITIES:
            weather_data = fetch_weather(city)
            if weather_data:
                save_weather_to_db(
                    weather_data['city'], 
                    weather_data['temp'], 
                    weather_data['feels_like'], 
                    weather_data['condition']
                )
                check_alerts(weather_data['city'], weather_data['temp'])
        time.sleep(FETCH_INTERVAL)

@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT city, temp, feels_like, condition, timestamp FROM weather_data ORDER BY timestamp DESC LIMIT 6")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/search', methods=['POST'])
def search():
    city = request.form.get('city')
    weather_data = fetch_weather(city)
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/alerts')
def alerts():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT city, alert_message, timestamp FROM alerts ORDER BY timestamp DESC LIMIT 10")
    alerts = cursor.fetchall()
    conn.close()
    return jsonify(alerts)

if __name__ == '__main__':
    init_db()
    # Start the weather fetching process in a separate thread
    threading.Thread(target=process_weather, daemon=True).start()
    app.run(debug=True)
