"""Metric Converter Project #"""
import tkinter as tk
from tkinter import ttk, END

# Define window
root = tk.Tk()
root.title("Metric Helper")
root.iconbitmap("ruler.ico")
root.resizable(0, 0)

# Define fonts & colors
field_font = ("Cambria", 10)
bg_color = "#C75C5C"
button_color = "#F5CF87"
root.config(bg=bg_color)


# Define functions
def convert():
    """Convert from 1 metric prefix to another"""
    metric_values = {
        "femto": 10 ** -15,
        "pico": 10 ** -12,
        "nano": 10 ** -9,
        "micro": 10 ** -6,
        "milli": 10 ** -3,
        "centi": 10 ** -2,
        "deci": 10 ** -1,
        "meter": 10 ** 0,
        "deca": 10 ** 1,
        "hecto": 10 ** 2,
        "kilo": 10 ** 3,
        "mega": 10 ** 6,
        "giga": 10 ** 9,
        "tera": 10 * 12,
        "peta": 10 ** 15
    }

    # Clear the output field
    output_field.delete(0, END)

    # Get all user information
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    # Convert to base (meter) first
    meter = start_value * metric_values[start_prefix]

    # Convert to the new metric value
    end_value = meter / metric_values[end_prefix]

    # Update output field with answer
    output_field.insert(0, str(end_value))


# Define layout

# Create the input and output entry fields
input_field = tk.Entry(root, width=20, font=field_font, borderwidth=3)
output_field = tk.Entry(root, width=20, font=field_font, borderwidth=3)
equal_label = tk.Label(root, text="=", font=field_font, bg=bg_color)

input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)

input_field.insert(0, "Enter your quantity")

# Combo box for metric values
metric_list = ["femto", "pico", "nano", "micro", "milli", "centi", "deci", "meter", "deca", "hecto",
               "kilo", "mega", "giga", "tera", "peta"]
input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify="center")
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify="center")
to_label = tk.Label(root, text="to", font=field_font, bg=bg_color)

input_combobox.set("meter")
output_combobox.set("meter")

input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

# Create a conversion button
convert_button = tk.Button(root, text="Convert", font=field_font, bg=button_color, command=convert)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

# Run the root window
root.mainloop()
