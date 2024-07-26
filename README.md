# Weather Data Aggregator and Analyzer

## Project Overview

The Weather Data Aggregator and Analyzer is a Python application designed to fetch weather data from a public API, store it in a local SQLite database, and provide analysis and visualization of weather trends over time. This project uses the OpenWeatherMap API to gather weather information such as temperature, humidity, and wind speed.

## Features

- **Data Fetching**: Periodically fetches weather data for a specified city and stores it in a local database.
- **Data Storage**: Uses SQLite to store weather data with a schema designed for time-series data.
- **Data Analysis**: Provides basic statistical analysis, such as average temperature, humidity, and wind speed.
- **Data Visualization**: Uses Matplotlib and Seaborn to create visualizations for temperature distribution, hourly humidity trends, and wind speed distribution.

## Prerequisites

- Python 3.x
- pip (Python package manager)
- OpenWeatherMap API key (or another public weather API key)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/weather-data-analyzer.git
   cd weather-data-analyzer
2. Set Up a Virtual Environment
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt
   
4. Obtain API Key
   Sign up for an API key from OpenWeatherMap or a similar weather service.

5. Configure API Key
   Open scripts/fetch_data.py and replace 'your_api_key' with your actual API key

