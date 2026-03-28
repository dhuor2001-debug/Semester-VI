import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        operator = entry_op.get()

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = a / b
        else:
            messagebox.showerror("Error", "Incorrect operator")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers")

# Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Widgets
tk.Label(root, text="First Number").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Second Number").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Operator (+ - * /)").pack()
entry_op = tk.Entry(root)
entry_op.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run app
root.mainloop()
