import requests
import datetime as dt
import sqlite3

# Configuration
API_KEY = 'INSERT THE API KEY'  # insert your own API key for privacy concerns i haven't inserted my own API KEY 
CITY = 'Maharashtra'  # insert the name of the place you desire
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'


def fetch_weather_data(url):
    """Fetch data from the OpenWeather API."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def extract_weather_info(data):
    """Extract relevant weather information from the API response."""
    if not data:
        return {}

    try:
        temp_in_celsius = data['main']['temp']
        temp_feels_like = data['main']['feels_like']
        temp_max = data['main']['temp_max']
        wind_speed = data['wind'].get('speed', 'N/A')
        wind_gust = data['wind'].get('gust', 'N/A')
        humidity = data['main']['humidity']
        sunrise = dt.datetime.fromtimestamp(data['sys']['sunrise'] + data['timezone'], tz=dt.timezone.utc)
        sunset = dt.datetime.fromtimestamp(data['sys']['sunset'] + data['timezone'], tz=dt.timezone.utc)
        description = data['weather'][0]['description']
    except KeyError as e:
        print(f"Missing data in API response: {e}")
        return {}

    return {
        'temp_in_celsius': temp_in_celsius,
        'temp_feels_like': temp_feels_like,
        'temp_max': temp_max,
        'wind_speed': wind_speed,
        'wind_gust': wind_gust,
        'humidity': humidity,
        'sunrise': sunrise,
        'sunset': sunset,
        'description': description
    }


def store_weather_data(weather_info, city, db_name='weather_data.db'):
    """Store weather data in an SQLite database."""
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Create table if it does not exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT,
                temp_in_celsius REAL,
                temp_feels_like REAL,
                temp_max REAL,
                wind_speed REAL,
                wind_gust REAL,
                humidity INTEGER,
                sunrise TIMESTAMP,
                sunset TIMESTAMP,
                description TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Insert data into the table
        c.execute('''
            INSERT INTO weather_data (city, temp_in_celsius, temp_feels_like, temp_max, wind_speed, wind_gust, humidity, sunrise, sunset, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            city,
            weather_info.get('temp_in_celsius'),
            weather_info.get('temp_feels_like'),
            weather_info.get('temp_max'),
            weather_info.get('wind_speed'),
            weather_info.get('wind_gust'),
            weather_info.get('humidity'),
            weather_info.get('sunrise'),
            weather_info.get('sunset'),
            weather_info.get('description')
        ))

        # Commit the transaction and close the connection
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()


def main():
    """Main function to fetch, process, and store weather data."""

    data = fetch_weather_data(URL)
    weather_info = extract_weather_info(data)

    if weather_info:
        # Print the extracted data
        print(f"Temperature in {CITY} is {weather_info['temp_in_celsius']}°C")
        print(f"Feels like {weather_info['temp_feels_like']}°C")
        print(f"Maximum temperature for {CITY} today is {weather_info['temp_max']}°C")
        print(f"Wind speed for {CITY} is {weather_info['wind_speed']} m/s")
        print(f"Wind gust for {CITY} is {weather_info['wind_gust']} m/s")
        print(f"Humidity for {CITY} is {weather_info['humidity']}%")
        print(f"Sunrise in {CITY} is at {weather_info['sunrise']}")
        print(f"Sunset in {CITY} is at {weather_info['sunset']}")
        print(f"Current weather condition in {CITY} is {weather_info['description']}")

        # Store data in SQLite database
        store_weather_data(weather_info, CITY)
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    """main to run all the functions at once"""
    main()
