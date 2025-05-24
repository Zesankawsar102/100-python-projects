import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city.")
        return

    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text="City not found.")
            return

        weather = data['weather'][0]['description'].title()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        result = (
            f"📍 {city.title()}\n"
            f"🌤 Weather: {weather}\n"
            f"🌡 Temp: {temp}°C\n"
            f"🤗 Feels Like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind: {wind} m/s"
        )

        result_label.config(text=result)

    except Exception as e:
        result_label.config(text="Error retrieving data.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter City:", font=("Arial", 14)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify=tk.LEFT)
result_label.pack(pady=20)

root.mainloop()
