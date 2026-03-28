from tkinter import *
from tkinter import ttk
root = Tk()
root.title('hi')

branch_lebel = ttk.Label(root,text="select Branch")
branch_lebel.pack()

choices = ['physics','chemistry','CS','Math' ]
dropdown = ttk.Combobox(root,value=choices)
dropdown.pack()

checkbox = ttk.Checkbutton(root,text="Do you agree")
checkbox.pack()



root.mainloop()