import tkinter as tk
import math

# Create the main window
window = tk.Tk()
window.title("Best Calculator")
window.geometry("400x600")

# Set up a variable to hold the input/output text
display_var = tk.StringVar()

# Display frame
display = tk.Entry(window, textvar=display_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4)

# Basic operations
def button_click(value):
    current = display_var.get()
    display_var.set(current + str(value))

def button_clear():
    display_var.set("")

def button_equal():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

def button_backspace():
    current = display_var.get()
    display_var.set(current[:-1])

# Advanced operations
def button_sqrt():
    try:
        current = float(display_var.get())
        display_var.set(math.sqrt(current))
    except Exception as e:
        display_var.set("Error")

def button_square():
    try:
        current = float(display_var.get())
        display_var.set(current ** 2)
    except Exception as e:
        display_var.set("Error")

# Create number buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

# Create operation buttons
operations = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 2), ('←', 5, 0),
    ('√', 5, 1), ('x²', 5, 2)
]

# Add buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, font=("Arial", 18), width=4, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

for (text, row, col) in operations:
    if text == "=":
        button = tk.Button(window, text=text, font=("Arial", 18), width=4, height=2, command=button_equal)
    elif text == "C":
        button = tk.Button(window, text=text, font=("Arial", 18), width=4, height=2, command=button_clear)
    elif text == "←":
        button = tk.Button(window, text=text, font=("Arial", 18), width=4, height=2, command=button_backspace)
    elif text == "√":
        button = tk.Button(window, text=text, font=("Arial", 18), width=4, height=2, command=button_sqrt)
    elif text == "x²":
        button = tk.Button(window, text=text, font=("Arial", 18), width=4, height=2, command=button_square)
    else:
        button = tk.Button(window, text=text, font=("Arial", 18), width=4, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Start the GUI loop
window.mainloop()

def button_sin():
    try:
        current = float(display_var.get())
        display_var.set(math.sin(math.radians(current)))  # Convert to radians
    except Exception as e:
        display_var.set("Error")

def button_cos():
    try:
        current = float(display_var.get())
        display_var.set(math.cos(math.radians(current)))  # Convert to radians
    except Exception as e:
        display_var.set("Error")
