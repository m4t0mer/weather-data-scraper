import requests
import csv
from datetime import datetime
import os
import sys
from dotenv import load_dotenv

class WeatherScraper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city):
        """
        Fetch weather data for a given city from OpenWeatherMap API
        
        :param city: Name of the city
        :return: Dictionary with weather information
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Using Celsius
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            return {
                'city': data['name'],
                'country': data['sys']['country'],
                'latitude': data['coord']['lat'],
                'longitude': data['coord']['lon'],
                'temperature_current': data['main']['temp'],
                'temperature_high': data['main']['temp_max'],
                'temperature_low': data['main']['temp_min'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'weather_condition': data['weather'][0]['main'],
                'weather_description': data['weather'][0]['description'],
                'sunrise_time': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
                'sunset_time': datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        except requests.RequestException as e:
            print(f"Error fetching weather data for {city}: {e}")
            return None

    def save_to_csv(self, data, filename='weather_data.csv'):
        """
        Save scraped data to a CSV file
        
        :param data: List of dictionaries with weather data
        :param filename: Output CSV filename
        """
        if not data:
            print("No data to save.")
            return

        # Ensure output directory exists
        os.makedirs('output', exist_ok=True)
        filepath = os.path.join('output', filename)

        keys = data[0].keys()
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Data saved to {filepath}")

def get_api_key():
    """
    Retrieve OpenWeatherMap API key from .env file
    
    :return: API key or None if not set
    """
    # Load environment variables from .env file
    load_dotenv()
    
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        print("Error: OPENWEATHERMAP_API_KEY not found in .env file.")
        sys.exit(1)
    return api_key

def main():
    # Get API key from .env file
    API_KEY = get_api_key()
    
    # city input with multiple city support
    scraper = WeatherScraper(API_KEY)
    weather_data = []
    
    print("Weather Data Scraper")
    print("Enter city names (comma-separated) or 'quit' to exit.")
    
    while True:
        try:
            cities_input = input("Enter cities: ").strip()
            
            if cities_input.lower() == 'quit':
                print("Exiting the weather scraper.")
                break
            
            # Split cities by comma and strip whitespace
            cities = [city.strip() for city in cities_input.split(',') if city.strip()]
            
            if not cities:
                print("No cities entered. Please try again.")
                continue
            
            # Fetch weather data for each city
            for city in cities:
                city_weather = scraper.get_weather_data(city)
                
                if city_weather:
                    weather_data.append(city_weather)
                    print(f"\n--- Weather Information for {city} ---")
                    for key, value in city_weather.items():
                        print(f"{key.replace('_', ' ').title()}: {value}")
            
            if weather_data:
                save_choice = input("\nDo you want to save the collected data to a CSV file? (yes/no): ").lower()
                if save_choice in ['yes', 'y']:
                    # Use timestamp in filename to make it unique
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    scraper.save_to_csv(weather_data, f'weather_data_{timestamp}.csv')
                
                # Reset weather_data for next batch of cities
                weather_data = []
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
    
    
