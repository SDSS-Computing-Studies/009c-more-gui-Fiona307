#!python3

import tkinter as tk
from tkinter import*

win = tk.Tk()

import math

trianglepic = PhotoImage(name="task1.png")
l1 = tk.Label(win, image=trianglepic)
a_e = tk.Entry(win, width=10)
b_e = tk.Entry(win, width=10)
c_e = tk.Entry(win, width=10)
h_e = tk.Entry(win, width=10)

win.mainloop()