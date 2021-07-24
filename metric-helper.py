#Metric Helper Project
import tkinter as tk
from tkinter import StringVar, ttk

# Define window
root = tk.Tk()
root.title("Metric Helper")
root.iconbitmap("ruler.ico")
root.resizable(0,0)

#Define fonts & colors
field_font = ("Cambria", 10)
bg_color = "#C75C5C"
button_color = "#F5CF87"
root.config(bg = bg_color)

#Defne functions


#Define layout


#Create the input and output entry fields
input_field = tk.Entry(root, width=20, font=field_font, borderwidth=3)
output_field = tk.Entry(root, width=20, font=field_font, borderwidth=3)
equal_label = tk.Label(root, text="=", font=field_font, bg=bg_color)

input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)

input_field.insert(0, "Enter your quantity")

#Combo box for metric values
metric_list = ["femto", "pico", "nano", "micro", "milli", "centi", "deci", "base value", "deca", "hecto"
               "kilo", "mega", "giga", "tera", "peta"]
input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify="center")
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify="center")
to_label = tk.Label(root, text="to", font=field_font, bg=bg_color)

input_combobox.set("base value")
output_combobox.set("base value")

input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

#Create a conversion button
convert_button = tk.Button(root, text="Convert", font=field_font, bg=button_color)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

#Run the root window
root.mainloop()

