import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry_value.get())
        conversion_type = combo_conversion.get()

        if conversion_type == "Rupees to Dollars":
            result = value * 0.012  
            result_label.config(text=f"Result: ${result:.2f}")
        elif conversion_type == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            result_label.config(text=f"Result: {result:.2f} °F")
        elif conversion_type == "Inches to Feet":
            result = value / 12
            result_label.config(text=f"Result: {result:.2f} ft")
        else:
            result_label.config(text="Please select a conversion type.")
    except ValueError:
        result_label.config(text="Invalid input. Enter a number.")


root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x250")
root.resizable(False, False)


title_label = tk.Label(root, text="Unit Converter", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

entry_value = tk.Entry(root, font=("Helvetica", 12))
entry_value.pack(pady=5)

combo_conversion = ttk.Combobox(root, state="readonly", font=("Helvetica", 12))
combo_conversion['values'] = ("Rupees to Dollars", "Celsius to Fahrenheit", "Inches to Feet")
combo_conversion.set("Select conversion")
combo_conversion.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert, font=("Helvetica", 12))
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Result will appear here", font=("Helvetica", 12))
result_label.pack(pady=10)


root.mainloop()
