import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3


def load_latest_data():
    """Load the latest weather data for visualization."""
    conn = sqlite3.connect('weather_data.db')
    query = '''
        SELECT * FROM weather
        ORDER BY timestamp DESC
        LIMIT 1000
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(df.head())  # Print the first few rows to check timestamp format
    return df


def plot_data(df):
    """Generate and save plots for weather data."""
    plt.figure(figsize=(10, 10))

    # Temperature Histogram
    plt.subplot(2, 2, 1)
    sns.histplot(df['temperature'], bins=20, kde=True, color='blue')
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')

    # Convert timestamps to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')  # Use errors='coerce' to handle parsing issues

    # Drop rows where timestamp could not be parsed
    df = df.dropna(subset=['timestamp'])

    # Extract hour from timestamp and update DataFrame
    df.loc[:, 'hour'] = df['timestamp'].dt.hour

    # Humidity Bar Chart
    plt.subplot(2, 2, 2)
    avg_humidity_per_hour = df.groupby('hour')['humidity'].mean().reset_index()
    sns.barplot(data=df, x='hour', y='humidity', color='orange')
    plt.title('Average Hourly Humidity Trends')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Humidity (%)')

    # Wind Speed Pie Chart
    plt.subplot(2, 2, 3)
    wind_speed_counts = df['wind_speed'].value_counts()
    plt.pie(wind_speed_counts, labels=wind_speed_counts.index, autopct='%1.1f%%',
            colors=plt.cm.Paired(range(len(wind_speed_counts))))
    plt.title('Wind Speed Distribution')

    plt.tight_layout()
    plt.savefig('weather_trends.png')
    plt.show()


if __name__ == '__main__':
    df = load_latest_data()
    plot_data(df)
