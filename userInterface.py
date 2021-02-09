from tkinter import *
from fractions import Fraction as frac
from main import mainFunc, countPrime, nthPrime, eularPiFunction, awFunction

root = Tk()
root.title("Prime Number Calculator")
root.geometry("498x550")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
Label(root, text="Insert Number : ").grid(row=0, column=5, columnspan=2, sticky=W)

# output = Text(root,width=30)
# output.grid(row=1,column=6, columnspan=5, rowspan=10)

scrollbar = Scrollbar(root, orient="vertical")

output = Listbox(root, width=40, height=22, yscrollcommand=scrollbar.set)
output.grid(row=1, column=6, rowspan=10)
scrollbar.config(command=output.yview)
scrollbar.grid(row=1, column=7, rowspan=10, sticky=N + S)


# scrollbar = Scrollbar(root)
# scrollbar.grid(row=1,column=11,rowspan=10,columnspan=5)
# output.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=output.yview)

def button_click(number):
    current = e.get()
    output.delete(0, END)
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_option_1():
    global number
    number = e.get()
    label_num = Label(root, text=number)
    label_num.grid(row=0, column=6)
    output.delete(0, END)
    count, list = countPrime(number)
    output.insert(END, ("NUMBER OF PRIMES : " + str(count) + "\n"))
    for i in list:
        output.insert(END, ( "  " + str(i) + "\n"))


def button_option_2():
    global number
    number = e.get()
    label_num = Label(root, text=number)
    label_num.grid(row=0, column=6)
    output.delete(0, END)
    results = mainFunc(number)
    for result in results:
        output.insert(END, "  " + result)


def button_option_3():
    global number
    global math
    output.delete(0, END)
    number = e.get()
    Label(root, text=number).grid(row=0, column=6)
    result = nthPrime(number)
    output.insert(END, ( "  " + str(number) + "(st/nd/th) PRIME NUMBER : \n" + str(result) + "\n"))

def button_option_4():
    output.delete(0, END)
    number = e.get()
    Label(root, text=number).grid(row=0, column=6)
    results = eularPiFunction(number)
    output.insert(END, ("No of relatively pr's : "+ str(len(results))))
    for result in results:
        output.insert(END, "  " + str(result))


def button_option_5():
    output.delete(0, END)
    number = e.get()
    Label(root, text=number).grid(row=0, column=6)
    sum = awFunction(number)
    output.insert(END, ("Resiprocal Sum : " + str(sum)))
    output.insert(END, ("As a fraction : " + str(frac(str(sum)).limit_denominator(100))))


label_option = Label(root, text="Choose Option").grid(row=6, column=1, columnspan=3, pady=20)
button_1 = Button(root, text="1", padx=20, pady=8, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=20, pady=8, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=20, pady=8, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=20, pady=8, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=20, pady=8, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=20, pady=8, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=20, pady=8, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=20, pady=8, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=20, pady=8, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=20, pady=8, command=lambda: button_click(0))
button_clear = Button(root, text="clear", padx=46, pady=8, command=button_clear)

button_0.grid(row=5, column=1)

button_option_1 = Button(root, text="Number of Primes", padx=45, pady=8, command=button_option_1)
button_option_2 = Button(root, text="Check Prime", padx=60, pady=8, command=button_option_2)
button_option_3 = Button(root, text="nth Prime", padx=68, pady=8, command=button_option_3)
button_option_4 = Button(root, text="Eular Function", padx=56, pady=8, command=button_option_4)
button_option_5 = Button(root, text="AW", padx=84, pady=8, command=button_option_5)

button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)

button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)

button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)

button_clear.grid(row=5, column=2, columnspan=2)

button_option_1.grid(row=8, column=1, columnspan=3)
button_option_2.grid(row=9, column=1, columnspan=3)
button_option_3.grid(row=10, column=1, columnspan=3)
button_option_4.grid(row=11, column=1, columnspan=3)
button_option_5.grid(row=12, column=1, columnspan=3)

root.mainloop()
