import tkinter as tk
from tkinter import messagebox

def press(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
    except:
        messagebox.showerror("Error", "Invalid expression")
        clear()

# Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Display
display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill="x", padx=10, pady=10)

# Buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        if char == '=':
            btn = tk.Button(row_frame, text=char, font=("Arial", 36),
                            command=calculate)
        else:
            btn = tk.Button(row_frame, text=char, font=("Arial", 36),
                            command=lambda c=char: press(c))
        btn.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 36),
                      bg="red", fg="white", command=clear)
clear_btn.pack(fill="x", padx=10, pady=10)

# Run
root.mainloop()
