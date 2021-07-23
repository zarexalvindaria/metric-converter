#Metric Helper Project
import tkinter as tk
from tkinter import StringVar

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
input_field = tk.Entry(root, width=20, font=field_font)
output_field = tk.Entry(root, width=20, font=field_font)
equal_label = tk.Label(root, text="=", font=field_font, bg=bg_color)

input_field.grid(row=0, column=0)
equal_label.grid(row=0, column=1)
output_field.grid(row=0, column=2)

input_field.insert(0, "Enter your quantity")

#Create dropdowns for metric values
metric_list = ["femto", "pico", "nano", "micro", "milli", "centi", "deci", "base value", "deca", "hecto"
               "kilo", "mega", "giga", "tera", "peta"]
input_choice = StringVar()
output_choice = StringVar()
input_dropdown = tk.OptionMenu(root, input_choice, *metric_list)
output_dropdown = tk.OptionMenu(root, output_choice, *metric_list)
to_label = tk.Label(root, text="to", font=field_font, bg=bg_color)

input_dropdown.grid(row=1, column=0)
to_label.grid(row=1, column=1)
output_dropdown.grid(row=1, column=2)

#Run the root window
root.mainloop()

