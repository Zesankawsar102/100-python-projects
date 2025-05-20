import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry.get())
        unit = combo.get()

        if unit == "Meters to Feet":
            result = value * 3.28084
        elif unit == "Feet to Meters":
            result = value / 3.28084
        elif unit == "Kilograms to Pounds":
            result = value * 2.20462
        elif unit == "Pounds to Kilograms":
            result = value / 2.20462
        elif unit == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
        else:
            result = "Invalid unit"

        output_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        output_label.config(text="Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x250")

tk.Label(root, text="Enter value:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

tk.Label(root, text="Select conversion:", font=("Arial", 12)).pack(pady=5)
combo = ttk.Combobox(root, values=[
    "Meters to Feet",
    "Feet to Meters",
    "Kilograms to Pounds",
    "Pounds to Kilograms",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius"
], font=("Arial", 12))
combo.pack(pady=5)
combo.set("Meters to Feet")

tk.Button(root, text="Convert", command=convert, font=("Arial", 12)).pack(pady=10)
output_label = tk.Label(root, text="", font=("Arial", 14))
output_label.pack(pady=5)

root.mainloop()
