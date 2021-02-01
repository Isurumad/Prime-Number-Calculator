from tkinter import *

root = Tk()
e=Entry(root,width = 35, borderwidth=5)
e.grid(row=0, column=0,columnspan=3, padx = 10, pady = 10)

def onClick(text):
    current = e.get()
    e.delete(0,END)
    e.insert(0,text)

button = Button(root, text="click", command=lambda:onClick(1))
button.grid(row=1,column=1)

root.mainloop()