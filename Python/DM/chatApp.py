from tkinter import *
from tkinter import scrolledtext

#SendButton Function
def SendFunc():
    UserInput = InputText.get("1.0",END).strip()
    DisplayText.config(state=NORMAL)
    DisplayText.insert(END,"You: "+ UserInput + "\n")
    DisplayText.insert(END,"Bot: "+ "Hi, Welcome to the Chat App!" + "\n")
    DisplayText.config(state=DISABLED)
    InputText.delete("1.0", END)



root = Tk()
root.title("Chat APP")

AppHeader = Label(root,text="Chat APP", font =("italy",50),bg="Lightblue")
AppHeader.pack(fill=X, expand=True)

DisplayText = scrolledtext.ScrolledText(root,state=DISABLED,wrap=WORD)
DisplayText.pack(fill=BOTH,expand=TRUE)

InputText= scrolledtext.ScrolledText(root, height=5, wrap = WORD)
InputText.pack(fill=X, padx=5, pady = 5)

SendButton = Button(root, text="Send", font=("italy",12,"bold"),command=SendFunc, bg="lightgreen", fg="red")
SendButton.pack(fill=X, padx=5,pady=5)

root.mainloop()