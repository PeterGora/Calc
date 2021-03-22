from tkinter import *
import re


base = Tk()
base.geometry("380x380+400+150")
base.resizable(width=0, height=0)
base.title("Calculator")
base.configure(bg="#2a2f33")


def calculate():
    get_all = entered.get(1.0, END)
    value = get_all
    value = re.sub(u"\u00F7", '/', value)
    value = re.sub("x", '*', value)
    value = re.sub(u"%", '/100', value)
    answer = eval(value)
    entered.delete(1.0, END)
    entered.insert(1.0, answer)

def buttons(text):
    entered.insert(END, text)

def clear():
    entered.delete(1.0, END)

entered =  Text(base, width=30, height=1.5, bg="#ffffff", bd=10, font="5")
entered.place(x=33, y=10)

def all_buttons():
    button_nine = Button(base, width=8, text="9", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("9"))
    button_nine.place(x=190, y=100)
    button_eight = Button(base, width=8, text="8", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("8"))
    button_eight.place(x=100, y=100)
    button_seven = Button(base, width=8, text="7", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("7"))
    button_seven.place(x=10, y=100)
    button_six = Button(base, width=8, text="6", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("6"))
    button_six.place(x=190, y=150)
    button_five = Button(base, width=8, text="5", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("5"))
    button_five.place(x=100, y=150)
    button_four = Button(base, width=8, text="4", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("4"))
    button_four.place(x=10, y=150)
    button_three = Button(base, width=8, text="3", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("3"))
    button_three.place(x=190, y=200)
    button_two = Button(base, width=8, text="2", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("2"))
    button_two.place(x=100, y=200)
    button_one = Button(base, width=8, text="1", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("1"))
    button_one.place(x=10, y=200)
    button_zero = Button(base, width=8, text="0", bd=5, font="1", bg="#c8cfcd", command=lambda: buttons("0"))
    button_zero.place(x=100, y=250)
    button_dot = Button(base, width=8, text=".", bd=5, font="1", bg="#62a0d1", command=lambda: buttons("."))
    button_dot.place(x=10, y=250)
    button_plus = Button(base, width=8, text="+", bd=5, font="1", bg="#62a0d1", command=lambda: buttons("+"))
    button_plus.place(x=280, y=250)
    button_minus = Button(base, width=8, text="-", bd=5, font="1", bg="#62a0d1", command=lambda: buttons("-"))
    button_minus.place(x=280, y=200)
    button_divide = Button(base, width=8, text=u"\u00F7", bd=5, font="1", bg="#62a0d1", command=lambda: buttons(u"\u00F7"))
    button_divide.place(x=280, y=100)
    button_multiply = Button(base, width=8, text="x", bd=5, font="1", bg="#62a0d1", command=lambda: buttons("x"))
    button_multiply.place(x=280, y=150)
    button_percent = Button(base, width=8, text="%", bd=5, font="1", bg="#62a0d1", command=lambda: buttons("%"))
    button_percent.place(x=190, y=250)
    button_clear = Button(base, width=8, text=u"\u232B", bd=5, font="1", bg="#cc1839", command=clear)
    button_clear.place(x=190, y=300)
    button_calculate = Button(base, width=8, text="=", bd=5, font="1", bg="#62a0d1", command=calculate)
    button_calculate.place(x=280, y=300)

all_buttons()

base.mainloop()
