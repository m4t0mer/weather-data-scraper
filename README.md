# Weather Data Scraper

## Overview
This Python script scrapes real-time weather data from the OpenWeatherMap API, extracting comprehensive information for multiple cities. The scraper is designed for personal use, but the collected data can also be integrated into other applications that require weather information.

## Features
- Fetch current weather data for multiple cities with a single run
- Retrieve key weather metrics such as temperature, humidity, wind speed, weather condition, and more
- Save the scraped data to a CSV file for further analysis or storage
- Supports both MX Linux and Windows operating systems

## Prerequisites
- Python 3.7 or higher
- OpenWeatherMap API key (you can sign up for a free account to obtain the key)
- `dotenv` library for managing environment variables

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/m4t0mer/weather-data-scraper.git
   ```
2. Navigate to the project directory:
   ```
   cd weather-data-scraper
   ```
3. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the project root directory and add your OpenWeatherMap API key:
   ```
   OPENWEATHERMAP_API_KEY=YOUR_API_KEY_HERE
   ```

## Usage
To run the weather data scraper, execute the following command:
```
python src/scraper.py
```
The script will prompt you to enter a comma-separated list of city names. Once the data is fetched, you'll be asked if you want to save the data to a CSV file.

## Data Columns
The weather data scraper collects the following information for each city:
- City
- Country
- Latitude
- Longitude
- Current Temperature
- High Temperature
- Low Temperature
- Humidity
- Wind Speed
- Weather Condition
- Weather Description
- Sunrise Time
- Sunset Time
- Timestamp

## Future Improvements
In the future, i'd like to explore the integration of AI/Language Models (LLMs) to enhance the weather data scraper. This could include features such as:
- Generating personalized weather reports or forecasts based on the scraped data
- Integrating the scraper with other data sources to provide more comprehensive weather information

## Contributing
If you'd like to contribute to the development of the weather data scraper, feel free to submit issues, feature requests, or pull requests on the [GitHub repository](https://github.com/m4t0mer/weather-data-scraper).

## License
This project is licensed under the [MIT License](LICENSE).

