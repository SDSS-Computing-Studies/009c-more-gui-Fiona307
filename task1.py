#!python3

import tkinter as tk
from tkinter import*

win = tk.Tk()

import math

trianglepic = PhotoImage(file="triangle.png")
l1 = tk.Label(win, image=trianglepic)

a_e = tk.Entry(win, width=10)
b_e = tk.Entry(win, width=10)
c_e = tk.Entry(win, width=10)
h_e = tk.Entry(win, width=10)

output = StringVar()
instruction = "Enter in as much information about the\ntriangle shown and I will calculate the area"
output.set(instruction)
e1 = tk.Entry(win, textvariable=output)

def calculate():
    a = a_e.get()
    b = b_e.get()
    c = c_e.get()
    h = h_e.get()
    if h == None:
        s = (float(a)+float(b)+float(c))/2
        area = math.sqrt(s*(s-float(a))*(s-float(b))*(s-float(c)))
        answer = 
        e1.delete(0,END)
        e1.insert(0,answer)


b1 = tk.Button(win, text="Calculate!")


win.mainloop()