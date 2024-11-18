import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
api_key = ""
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" 

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    main = data ['main']
    weather = data['weather'][0]['description']
    temperature = main['temp']
    humidity = main['humidity']
    wind_speed = data['wind']['speed']
    # fire?

    result = f"Weather: {weather.capitalize()}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
    weather_label.config(text=result)
else:
    messagebox.showerror("Error", "City not found")

app = tk.Tk()
app.title("Weather")

tk.Label(app, text="Enter City:").pack()
city_entry = tk.Entry(app)
city_entry.pack()

tk.Button(app, text="Get Weather", command=get_weather).pack()
weather_label = tk.Label(app, text="")
weather_label.pack()

app.mainloop()

