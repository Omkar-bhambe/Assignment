# scripts/fetch_data.py

import requests
import sqlite3
from datetime import datetime
import time

API_KEY = 'cd5a7ecb4bd9d9993fd1dbd33a6ab4e5'
CITY = 'Pune'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
INTERVAL = 5  # Interval in seconds (1 hour)


def fetch_weather_data():
    """Fetch weather data from OpenWeatherMap API."""
    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'city': CITY,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return weather_data
    else:
        raise Exception(f"Error fetching data: {data.get('message', 'Unknown error')}")


def store_data(weather_data):
    """Store fetched weather data into the SQLite database."""
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            timestamp TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO weather (city, temperature, humidity, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (weather_data['city'], weather_data['temperature'], weather_data['humidity'], weather_data['wind_speed'],
          weather_data['timestamp']))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    while True:
        weather_data = fetch_weather_data()
        store_data(weather_data)
        print(f"Data fetched and stored at {weather_data['timestamp']}")
        time.sleep(INTERVAL)
