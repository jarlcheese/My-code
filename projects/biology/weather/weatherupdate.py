import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    # Retrieve the city name from the entry widget
    city = city_entry.get()
    
    # Check if the city field is empty
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    # Replace with your OpenWeatherMap API key
    api_key = "5fc22da694b748459e849a77dfa34fc4"
    
    # Build the URL for the API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Send a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the JSON response
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']
        temperature = main['temp']
        humidity = main['humidity']
        wind_speed = data['wind']['speed']
        
        # Prepare the result string
        result = (
            f"Weather: {weather.capitalize()}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        
        #(advisory = generate_weather_advisory(temperature, wind_speed, weather)
        ####if advisory:
            # += f"\n\nAdvisory: {advisory}"

        # Update the weather_label with the fetched data
        weather_label.config(text=result)
        
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found. Please enter a valid city name.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    #def generate_weather_advisory(temperature, wind_speed, weather):
     ##   """
        #Generate a weather advisory based on temperature, wind speed, and weather conditions
       # """
       # advisory = ""

       # if temperature >= 35:
       #     advisory += "It's extremely hot. Stay hydrated and avoid outside activities"
       # elif temperature <= 0:
       #     advisory += "It's freezing outside. Dress warmly and avoid prolonged exposure."

        #if wind_speed >= 20:
         #   if advisory:
          #      advisory += " Also, "
        #advisory += "High wind speeds detected. Secure loose objects and be cautious."

    # Weather condition-based advisory
    #if "rain" in weather.lower() or "shower" in weather.lower():
     #   if advisory:
      #      advisory += " Additionally, "
       # advisory += "Carry an umbrella. Roads might be slippery."
    #elif "snow" in weather.lower():
     #   if advisory:
      #      advisory += " Also, "
       # advisory += "Snowfall expected. Drive carefully."

    #return advisory if advisory else "No significant advisories."

# Create the main Tkinter window
app = tk.Tk()
app.title("Weather App")

# Set window size
app.geometry("500x500")

# Add label for city input
tk.Label(app, text="Enter City:", font=("Arial", 12)).pack(pady=10)

# Create an entry widget for the user to type the city name
city_entry = tk.Entry(app, font=("Arial", 12))
city_entry.pack(pady=5)

# Create a button to trigger the weather fetch
tk.Button(app, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

# Create a label to display the weather information
weather_label = tk.Label(app, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=20)

# Start the Tkinter event loop
app.mainloop()
