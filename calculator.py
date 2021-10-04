#! /usr/bin/env/ python

"""This is a calculator, simple is that"""

from tkinter import *
#from tkinter import messagebox
import parser

window = Tk()
window.title("My Calculator")
window.geometry("210x180")

position = 0   # initial position of the number input

#def helloCallBack():
#  messagebox.showinfo( "Hello Python", "Hello World")

def numbutton(click): # get user input
    global position
    resetposition()
    display.insert(position, click)

def negativebutton(): # convert current str to negative
    neg = display.get()
    clearallbutton()
    display.insert(0, "-(" + neg + ")")

def percentagebutton(): # convert percentage to float 
    global position
    try: 
        num = float(display.get())   # must be float or int
    except Exception:
        clearallbutton()
        display.insert(0, "ERROR")
    else:
        clearallbutton()
        display.insert(0, num/100)

def calculate():
    formula = display.get()
    try:
        code = parser.expr(formula).compile()
        result = eval(code)
        clearallbutton()
        display.insert(0, result)
    except Exception:
        clearallbutton()
        display.insert(0, "ERROR")

def clearallbutton():
    display.delete(0,END)

def resetposition():
    global position
    position = len(display.get())


display = Entry(window, justify=RIGHT, width=16) # main display 
display.grid(row=0, columnspan=4)

Button(window, text="AC", command=lambda: clearallbutton()).grid(row=2, column=0)
Button(window, text="+/-", command=lambda: negativebutton()).grid(row=2, column=1)
Button(window, text="%", command=lambda: percentagebutton()).grid(row=2, column=2)
Button(window, text="/", command=lambda: numbutton("/")).grid(row=2, column=3)
Button(window, text="7", command=lambda: numbutton(7)).grid(row=3, column=0)
Button(window, text="8", command=lambda: numbutton(8)).grid(row=3, column=1)
Button(window, text="9", command=lambda: numbutton(9)).grid(row=3, column=2)
Button(window, text="X", command=lambda: numbutton("*")).grid(row=3, column=3)
Button(window, text="4", command=lambda: numbutton(4)).grid(row=4, column=0)
Button(window, text="5", command=lambda: numbutton(5)).grid(row=4, column=1)
Button(window, text="6", command=lambda: numbutton(6)).grid(row=4, column=2)
Button(window, text="-", command=lambda: numbutton("-")).grid(row=4, column=3)
Button(window, text="1", command=lambda: numbutton(1)).grid(row=5, column=0)
Button(window, text="2", command=lambda: numbutton(2)).grid(row=5, column=1)
Button(window, text="3", command=lambda: numbutton(3)).grid(row=5, column=2)
Button(window, text="+", command=lambda: numbutton("+")).grid(row=5, column=3)
Button(window, text="0", command=lambda: numbutton(0)).grid(row=6, column=0, columnspan=2)
Button(window, text=".", command=lambda: numbutton(".")).grid(row=6, column=2)
Button(window, text="=", command=lambda: calculate()).grid(row=6, column=3)

window.mainloop()   # infinite loop