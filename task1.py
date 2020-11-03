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

instruction = "Enter in as much information about the\ntriangle shown and I will calculate the area"
e1 = tk.Entry(win, textvariable=instruction)


b1 = tk.Button(win, text="Calculate!")


win.mainloop()