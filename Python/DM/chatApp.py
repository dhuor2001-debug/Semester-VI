from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("Chat APP")

AppHeader = Label(root,text="Chat APP", font =("italy",50),bg="Lightblue")
AppHeader.pack(fill=X, expand=True)

DisplayText = scrolledtext.ScrolledText(root,state=DISABLED,wrap=WORD)
DisplayText.pack(fill=BOTH,expand=TRUE)

InputText= scrolledtext.ScrolledText(root, height=5, wrap = WORD)
InputText.pack(fill=X, padx=5, pady = 5)

root.mainloop()