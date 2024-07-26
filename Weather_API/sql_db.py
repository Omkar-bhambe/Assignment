import sqlite3

class WeatherDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS weather_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature REAL NOT NULL,
                    humidity REAL NOT NULL,
                    wind_speed REAL NOT NULL,
                    timestamp TEXT NOT NULL
                );
            ''')

    def insert_data(self, temperature, humidity, wind_speed, timestamp):
        with self.conn:
            self.conn.execute('''
                INSERT INTO weather_data (temperature, humidity, wind_speed, timestamp)
                VALUES (?, ?, ?, ?);
            ''', (temperature, humidity, wind_speed, timestamp))

    def fetch_data_range(self, start_date, end_date):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT temperature, humidity, wind_speed, timestamp
                FROM weather_data
                WHERE timestamp BETWEEN ? AND ?;
            ''', (start_date, end_date))
            return cursor.fetchall()
