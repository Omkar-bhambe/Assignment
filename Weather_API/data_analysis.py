# scripts/analyze_data.py

import sqlite3
import pandas as pd

def get_latest_data():
    """Retrieve the latest weather data from the database."""
    conn = sqlite3.connect('weather_data.db')
    query = '''
        SELECT * FROM weather
        ORDER BY timestamp DESC
        LIMIT 100
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def calculate_statistics(df):
    """Calculate basic statistics for the weather data."""
    stats = {
        'average_temperature': df['temperature'].mean(),
        'average_humidity': df['humidity'].mean(),
        'average_wind_speed': df['wind_speed'].mean()
    }
    return stats

if __name__ == '__main__':
    df = get_latest_data()
    stats = calculate_statistics(df)
    print(f"Average Temperature: {stats['average_temperature']:.2f}°C")
    print(f"Average Humidity: {stats['average_humidity']:.2f}%")
    print(f"Average Wind Speed: {stats['average_wind_speed']:.2f} m/s")
