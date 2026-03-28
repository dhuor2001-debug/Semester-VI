import tkinter as tk
from tkinter import messagebox
from tkinter import Checkbutton
from tkinter import *
import csv
import os

# Create main window
root = tk.Tk()
root.title('Student Registration Form')
root.geometry('400x400')
root.configure(bg='#0000FF')

# Title Label
title_label = tk.Label(root, text='Student Registration Form',
                       font=('Arial', 16, 'bold'), bg='#0000FF', fg='white')
title_label.pack(pady=10)

# Name
name_label = tk.Label(root, text='Name:', bg='#0000FF', fg='white')
name_label.pack(anchor=tk.W, padx=20)
name_entry = tk.Entry(root, width=30)
name_entry.pack(padx=20, pady=5)

# Roll
roll_label = tk.Label(root, text='Roll No:', bg='#0000FF', fg='white')
roll_label.pack(anchor=tk.W, padx=20)
roll_entry = tk.Entry(root, width=30)
roll_entry.pack(padx=20, pady=5)
#Branch-Label
branch_lebel = tk.Label(root,text="select Branch")
branch_lebel.pack()

#Branch
choices = ['physics','chemistry','CS','Math' ]
dropdown = tk.Combobox(root,value=choices)
dropdown.pack()

# Email
email_label = tk.Label(root, text='Email ID:', bg='#0000FF', fg='white')
email_label.pack(anchor=tk.W, padx=20)
email_entry = tk.Entry(root, width=30)
email_entry.pack(padx=20, pady=5)

# Address
address_label = tk.Label(root, text='Address:', bg='#0000FF', fg='white')
address_label.pack(anchor=tk.W, padx=20)
address_entry = tk.Text(root, width=30, height=2)
address_entry.pack(padx=20, pady=5)

# Submit Function
def submit_form():
    name = name_entry.get()
    roll = roll_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END).strip()

    if name == "" or roll == "" or email == "" or address == "":
        messagebox.showwarning("Error", "All fields are required!")
    else:
        file_exists = os.path.isfile("data.csv")

        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)

            # Write header only once
            if not file_exists:
                writer.writerow(["Name", "Roll No", "Email", "Address"])

            # Write data row
            writer.writerow([name, roll, email, address])

        messagebox.showinfo("Success", "Student Registered Successfully!")

        # Clear fields after submission
        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete("1.0", tk.END)

#Consent
agree_value = tk.IntVar()
checkbox = tk.Checkbutton(root,text="Do you agree",value=agree_value)
checkbox.pack()

# Submit Button
submit_button = tk.Button(root, text='Submit', command=submit_form)
submit_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text='Exit', command=root.quit)
exit_button.pack()

root.mainloop()
