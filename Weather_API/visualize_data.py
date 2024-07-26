import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
DB_NAME = 'weather_data.db'

def load_data_from_db(db_name):

    """Load data from SQLite database into a pandas DataFrame."""
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query('SELECT * FROM weather_data', conn)
    conn.close()
    return df

def preprocess_data(df):

    """Preprocess the DataFrame by converting 'date' to datetime format."""

    df['date'] = pd.to_datetime(df['date'])
    return df

def plot_temperature_over_time(ax, df):

    """Plot temperature data over time."""
    ax.plot(df['date'], df['temp_in_celsius'], marker='o', color='blue', label='Current Temperature')
    ax.plot(df['date'], df['temp_max'], marker='o', color='red', label='Maximum Temperature')
    if 'temp_min' in df.columns:
        ax.plot(df['date'], df['temp_min'], marker='o', color='green', label='Minimum Temperature')
    ax.set_title('Temperature Over Time', fontsize=12)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Temperature (°C)', fontsize=12)
    ax.legend()
    ax.tick_params(axis='x', rotation=45)

def plot_feels_like_temperature(ax, df):

    """Plot 'feels like' temperature over time."""
    ax.plot(df['date'], df['temp_feels_like'], marker='o', color='orange')
    ax.set_title('Feels Like Temperature Over Time', fontsize=12)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Feels Like Temperature (°C)', fontsize=12)
    ax.tick_params(axis='x', rotation=45)

def plot_wind_speed_distribution(ax, df):
    """Plot wind speed distribution."""
    sns.histplot(df['wind_speed'].astype(float), kde=True, bins=20, ax=ax)
    ax.set_title('Wind Speed Distribution', fontsize=12)
    ax.set_xlabel('Wind Speed (m/s)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)

def plot_humidity_distribution(ax, df):

    """Plot humidity distribution using scatter and line plot."""
    ax.scatter(df.index, df['humidity'], alpha=0.5, color='purple', edgecolor='w', label='Humidity')
    ax.plot(df.index, df['humidity'], color='black', linestyle='--', linewidth=1, label='Trend Line')
    ax.set_title('Humidity Distribution', fontsize=12)
    ax.set_xlabel('Index', fontsize=12)
    ax.set_ylabel('Humidity (%)', fontsize=12)
    ax.legend()

def plot_wind_gust_distribution(ax, df):

    """Plot wind gust distribution if applicable."""
    if df['wind_gust'].notna().any():
        sns.histplot(df['wind_gust'].astype(float), kde=True, bins=20, ax=ax)
        ax.set_title('Wind Gust Distribution', fontsize=12)
        ax.set_xlabel('Wind Gust (m/s)', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
    else:
        ax.axis('off')

def plot_wind_speed_pie_chart(ax, df):

    """Plot pie chart for wind speed distribution."""
    bins = [2, 5, 10, 20]
    bin_labels = ['2-5 m/s', '5-10 m/s', '10-20 m/s']
    df['wind_speed_category'] = pd.cut(df['wind_speed'].astype(float), bins=bins, labels=bin_labels, include_lowest=True)
    wind_speed_counts = df['wind_speed_category'].value_counts()
    ax.pie(wind_speed_counts, labels=wind_speed_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set2"), wedgeprops=dict(width=0.4))
    ax.set_title('Wind Speed Distribution (Pie Chart)', fontsize=12)

def main():

    """Main function to load, process, and visualize weather data."""
    # Load and preprocess data
    df = load_data_from_db(DB_NAME)
    df = preprocess_data(df)

    # Print basic information
    print(df.head())
    print(df.describe())

    # Set the style for seaborn
    sns.set(style="whitegrid")

    # Create a figure with subplots
    fig, axes = plt.subplots(3, 2, figsize=(16, 14), gridspec_kw={'hspace': 1.0, 'wspace': 0.4})

    # Plot data
    plot_temperature_over_time(axes[0, 0], df)
    plot_feels_like_temperature(axes[0, 1], df)
    plot_wind_speed_distribution(axes[1, 0], df)
    plot_humidity_distribution(axes[1, 1], df)
    plot_wind_gust_distribution(axes[2, 0], df)
    plot_wind_speed_pie_chart(axes[2, 1], df)

    # Adjust plot layout
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
