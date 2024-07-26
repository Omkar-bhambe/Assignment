# Weather API Analyzer

## Overview

Welcome to the Weather API Analyzer project! This Python-based application allows you to fetch, analyze, and visualize weather data for any city using the OpenWeather API. With this tool, you can get real-time weather information and generate insightful visualizations to better understand weather patterns and trends.

## Features

- **Real-time Weather Data**: Retrieve current weather data, including temperature, humidity, and weather conditions.
- **Data Analysis**: Analyze weather metrics such as temperature fluctuations, humidity levels, and more.
- **Data Visualization**: Generate charts and graphs to visualize weather trends and comparisons.
- **City Search**: Easily switch between cities to get localized weather information.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- An OpenWeather API key (sign up at [OpenWeather](https://home.openweathermap.org/users/sign_up) if you don’t have one)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/weather-api-analyzer.git
    cd weather-api-analyzer
    ```

2. **Install Dependencies**

    You can use `pip` to install the required packages. It’s recommended to use a virtual environment.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Set Up Your API Key**

    Create a `.env` file in the root directory of the project and add your OpenWeather API key:

    ```env
    OPENWEATHER_API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Application**

    ```bash
    python main.py
    ```

2. **Interactive Commands**

    After running the application, follow the prompts to enter a place name. The application will fetch the latest weather data for the specified place and display visualizations.

    **Example**

    ```bash
    Enter place name: London
    ```

    The application will provide a real-time weather report for London and display graphs such as temperature trends over time.

## Code Structure

- `featch_data.py`: Handles API requests and responses including schema creation and data storing.
- `visualization.py`: Generates charts and visualizations.
- `ouput`: Holds the screenshots of the ploted charts generated 

## Dependencies

- `requests`: For making HTTP requests to the OpenWeather API
- `matplotlib`: For creating visualizations
- `pandas`: For data manipulation and analysis
- `seaborn` : Used for data mamipulation, analysis and visualisation


## Contact

For any questions or feedback, please open an issue on the GitHub repository or contact me at `bhambeomkar@gmail.com `.

Happy coding and stay informed about the weather!

## An Overview of how it will looks like 

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Weather_API/Output/Screenshot%202024-07-27%20003713.png" width="500" height = "500">

### Temperature over time plot 

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Weather_API/Output/Screenshot%202024-07-27%20003235.png" width = "350" height = "350">

### Feels like Temperature over time plot 

<img src = ""

