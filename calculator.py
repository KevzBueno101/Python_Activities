from tkinter import *
import tkinter.font as font

def add():
    try:
        result_value = float(enterOne.get()) + float(enterTwo.get())
        result.config(text="Result: " + str(result_value))
    except:
        result.config(text="Invalid input")

def sub():
    try:
        result_value = float(enterOne.get()) - float(enterTwo.get())
        result.config(text="Result: " + str(result_value))
    except:
        result.config(text="Invalid input")

def div():
    try:
        result_value = float(enterOne.get()) / float(enterTwo.get())
        result.config(text="Result: " + str(result_value))
    except:
        result.config(text="Invalid input")

def mul():
    try:
        result_value = float(enterOne.get()) * float(enterTwo.get())
        result.config(text="Result: " + str(result_value))
    except:
        result.config(text="Invalid input")

root = Tk()
root.title("Simple Calculator")

numOne = Label(root, text="Enter First Number:", font=("Serif", 12))
enterOne = Entry(root)
numTwo = Label(root, text="Enter Second Number:", font=("Serif", 12))
enterTwo = Entry(root)

add_btn = Button(root, text="Add", width=10, command=add)
sub_btn = Button(root, text="Sub", width=10, command=sub)
div_btn = Button(root, text="Div", width=10, command=div)
mul_btn = Button(root, text="Mul", width=10, command=mul)

result = Label(root, text="Result:", font=("Serif", 12))

numOne.grid(row=0, column=0)
enterOne.grid(row=0, column=1)
numTwo.grid(row=1, column=0)
enterTwo.grid(row=1, column=1)
add_btn.grid(row=2, column=0)
sub_btn.grid(row=2, column=1)
div_btn.grid(row=3, column=0)
mul_btn.grid(row=3, column=1)
result.grid(row=4, column=0, columnspan=2)

root.mainloop()