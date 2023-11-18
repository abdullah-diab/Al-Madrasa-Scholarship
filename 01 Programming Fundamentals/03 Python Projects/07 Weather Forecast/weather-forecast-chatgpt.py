import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(api_key, city):
    """
    Get weather data from the OpenWeatherMap API for a specified city.

    Parameters:
    - api_key (str): OpenWeatherMap API key.
    - city (str): Name of the city for which weather data is requested.

    Returns:
    - dict: Weather data in JSON format.
    - None: In case of a connection error.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except requests.ConnectionError:
        messagebox.showerror("Error", "Failed to connect to the weather API.")
        return None

def update_weather():
    """
    Update the weather information displayed in the GUI based on the user-entered location.
    """
    city = location_entry.get()
    if not city:
        messagebox.showwarning("Warning", "Please enter a location.")
        return

    api_key = '32d1b1dfc17fcf9b156171f0473e34c4'

    weather_data = get_weather_data(api_key, city)
    if weather_data:
        temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed'] * 3.6} km/h")
        pressure_label.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")
        precipitation_label.config(text=f"Precipitation: {weather_data.get('rain', {}).get('1h', 0)} %")

# Create the main window
root = tk.Tk()
root.title("Weather Forecast")

# Create and place UI elements
location_label = tk.Label(root, text="Location:")
location_label.grid(row=0, column=0, padx=10, pady=10)

location_entry = tk.Entry(root)
location_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search", command=update_weather)
search_button.grid(row=0, column=2, padx=10, pady=10)

temperature_label = tk.Label(root, text="Temperature:")
temperature_label.grid(row=1, column=0, padx=10, pady=10)

humidity_label = tk.Label(root, text="Humidity:")
humidity_label.grid(row=2, column=0, padx=10, pady=10)

wind_speed_label = tk.Label(root, text="Wind Speed:")
wind_speed_label.grid(row=3, column=0, padx=10, pady=10)

pressure_label = tk.Label(root, text="Pressure:")
pressure_label.grid(row=4, column=0, padx=10, pady=10)

precipitation_label = tk.Label(root, text="Precipitation:")
precipitation_label.grid(row=5, column=0, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
