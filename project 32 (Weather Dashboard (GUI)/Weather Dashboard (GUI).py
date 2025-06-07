import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY_HERE"  # Replace with your real API key
    base_url = "your url"

    try:
        params = {"q": city, "appid": api_key, "units": "metric"}
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text="❌ City not found.")
            return

        temp = data['main']['temp']
        condition = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        result = (
            f"📍 {city.title()}\n"
            f"🌤 Condition: {condition}\n"
            f"🌡 Temperature: {temp}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind: {wind} m/s"
        )
        result_label.config(text=result)
    except Exception as e:
        result_label.config(text="⚠️ Error retrieving weather data.")

# GUI Setup
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="🌦 Enter City Name:", font=("Arial", 14)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify=tk.LEFT)
result_label.pack(pady=20)

root.mainloop()
