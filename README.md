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
    git clone https://github.com/Omkar-bhambe/Weathe_API.git
    cd Weather_API
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
- `requirements.txt` : Comprises all the modules and libraries required for the seamless execution of the program

## Dependencies

- `requests`: For making HTTP requests to the OpenWeather API
- `matplotlib`: For creating visualizations
- `pandas`: For data manipulation and analysis
- `seaborn` : Used for data mamipulation, analysis and visualisation

## An Overview of how it will looks like 

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Output/Visualization%20sheet.png" width="700">

### Temperature over time plot 

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Output/Temperature%20Over%20Time.png" width = "500">

### Feels like Temperature over time plot 

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Weather_API/Output/Feels Like Temp Over Time.png" width = "500">

### Wind Speed distribution(frequency vs wind speed plot)

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Output/Wind%20Speed%20Distribution.png" width = "500">

### Wind Pie Plot

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Output/Wind%20speed%20%20pie%20plot.png" width = "500">

### Humidity Distribution

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Output/Humidity%20Distribution.png" width = "500">

### Wind Gust Distribution 

<img src = "https://github.com/Omkar-bhambe/Assignment/blob/main/Output/Wind%20Gust%20Distribution.png" width = "500">

For the visualization i took Maharashtra into the consideration as far as the locations concerns you can use any other state or city you desire to analyze and visualize your data using these program

#### Steps to Execute the Program :- 

1. Step 1 :- First run the file fetch_data.py before that check weather all the modules and libraries are installed you can use any interpreter for execution of the code.
   
2. Step 2 :- After fetching the data from API (Use your own API key Instructions to generate are mentioned above) the data get automatically store into schema generated via the queries passed in the code due to the implementation of the sqlite3.
   
3. Step 3 :- Run visualize.py file once fetch_data.py is completely executed these file will analyze the data fetched from the API by accessing it throught the schema weather_data.db and then visualize it into graphs as shown in above images.
   
4. Once this procces is completed a pop up sheet opens on the user interface and showcases all the plots in one sheet if user is using IDE while if they are jupyter notebook or google colab the result will be seen on the interpreter itself.

## Contact

For any questions or feedback, please open an issue on the GitHub repository or contact me at `bhambeomkar@gmail.com `.

Happy coding and stay informed about the weather!


