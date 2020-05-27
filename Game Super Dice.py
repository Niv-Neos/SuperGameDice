import math as mt
import numpy as np
import os
import config as cf
import random as rd

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

RESOLUTION = cf.Resolution

main = tk.Tk()
main.geometry(RESOLUTION)
main.title("Game Super Dice")
main.configure(background="gray40")
main.clipboard_get

number_i = tk.IntVar()

### Rollers
def Roll_d6(quanity, sides):
       steps = 0
       a = 0
       while steps < quanity:
              a = a + rd.randint(1,sides)
              steps = steps + 1
       while steps == quanity:
              number_i.set(a)
              return a

### Dices
d2b = tk.Button(main, text = ("d2  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(1,2), fg = "red3", bg = "gray3").grid(row=1,column=2,ipadx=30,ipady=5)
d2b2 = tk.Button(main, text = ("2d2  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(2,2), fg = "red3", bg = "gray3").grid(row=1,column=3,ipadx=30,ipady=5)
d2b3 = tk.Button(main, text = ("3d2  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(3,2), fg = "red3", bg = "gray3").grid(row=1,column=4,ipadx=30,ipady=5)
d2b4 = tk.Button(main, text = ("4d2  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(4,2), fg = "red3", bg = "gray3").grid(row=1,column=5,ipadx=30,ipady=5)
d2b5 = tk.Button(main, text = ("5d2  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(5,2), fg = "red3", bg = "gray3").grid(row=1,column=6,ipadx=30,ipady=5)
d2b6 = tk.Button(main, text = ("6d2  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(6,2), fg = "red3", bg = "gray3").grid(row=1,column=7,ipadx=30,ipady=5)
       
d4b = tk.Button(main, text = ("d4  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(1,4), fg = "orange", bg = "gray3").grid(row=2,column=2,ipadx=30,ipady=5)
d4b2 = tk.Button(main, text = ("2d4  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(2,4), fg = "orange", bg = "gray3").grid(row=2,column=3,ipadx=30,ipady=5)
d4b3 = tk.Button(main, text = ("3d4  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(3,4), fg = "orange", bg = "gray3").grid(row=2,column=4,ipadx=30,ipady=5)
d4b4 = tk.Button(main, text = ("4d4  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(4,4), fg = "orange", bg = "gray3").grid(row=2,column=5,ipadx=30,ipady=5)
d4b5 = tk.Button(main, text = ("5d4  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(5,4), fg = "orange", bg = "gray3").grid(row=2,column=6,ipadx=30,ipady=5)
d4b6 = tk.Button(main, text = ("6d4  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(6,4), fg = "orange", bg = "gray3").grid(row=2,column=7,ipadx=30,ipady=5)
       
d6b = tk.Button(main, text = ("d6  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(1,6), fg = "yellow3", bg = "gray3").grid(row=3,column=2,ipadx=30,ipady=5)
d6b2 = tk.Button(main, text = ("2d6  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(2,6), fg = "yellow3", bg = "gray3").grid(row=3,column=3,ipadx=30,ipady=5)
d6b3 = tk.Button(main, text = ("3d6  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(3,6), fg = "yellow3", bg = "gray3").grid(row=3,column=4,ipadx=30,ipady=5)
d6b4 = tk.Button(main, text = ("4d6  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(4,6), fg = "yellow3", bg = "gray3").grid(row=3,column=5,ipadx=30,ipady=5)
d6b5 = tk.Button(main, text = ("5d6  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(5,6), fg = "yellow3", bg = "gray3").grid(row=3,column=6,ipadx=30,ipady=5)
d6b6 = tk.Button(main, text = ("6d6  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(6,6), fg = "yellow3", bg = "gray3").grid(row=3,column=7,ipadx=30,ipady=5)

d8b = tk.Button(main, text = ("d8  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(1,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=2,ipadx=30,ipady=5)
d8b2 = tk.Button(main, text = ("2d8  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(2,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=3,ipadx=30,ipady=5)
d8b3 = tk.Button(main, text = ("3d8  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(3,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=4,ipadx=30,ipady=5)
d8b4 = tk.Button(main, text = ("4d8  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(4,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=5,ipadx=30,ipady=5)
d8b5 = tk.Button(main, text = ("5d8  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(5,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=6,ipadx=30,ipady=5)
d8b6 = tk.Button(main, text = ("6d8  "), font = ("kimberly_BI"),
            command = lambda : Roll_d6(6,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=7,ipadx=30,ipady=5)

d10b = tk.Button(main, text = ("d10"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(1,10), fg = "green3", bg = "gray3").grid(row=5,column=2,ipadx=30,ipady=5)
d10b2 = tk.Button(main, text = ("2d10"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(2,10), fg = "green3", bg = "gray3").grid(row=5,column=3,ipadx=30,ipady=5)
d10b3 = tk.Button(main, text = ("3d10"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(3,10), fg = "green3", bg = "gray3").grid(row=5,column=4,ipadx=30,ipady=5)
d10b4 = tk.Button(main, text = ("4d10"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(4,10), fg = "green3", bg = "gray3").grid(row=5,column=5,ipadx=30,ipady=5)
d10b5 = tk.Button(main, text = ("5d10"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(5,10), fg = "green3", bg = "gray3").grid(row=5,column=6,ipadx=30,ipady=5)
d10b6 = tk.Button(main, text = ("6d10"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(6,10), fg = "green3", bg = "gray3").grid(row=5,column=7,ipadx=30,ipady=5)

d12b = tk.Button(main, text = ("d12"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(1,12), fg = "cyan3", bg = "gray3").grid(row=6,column=2,ipadx=30,ipady=5)
d12b2 = tk.Button(main, text = ("2d12"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(2,12), fg = "cyan3", bg = "gray3").grid(row=6,column=3,ipadx=30,ipady=5)
d12b3 = tk.Button(main, text = ("3d12"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(3,12), fg = "cyan3", bg = "gray3").grid(row=6,column=4,ipadx=30,ipady=5)
d12b4 = tk.Button(main, text = ("4d12"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(4,12), fg = "cyan3", bg = "gray3").grid(row=6,column=5,ipadx=30,ipady=5)
d12b5 = tk.Button(main, text = ("5d12"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(5,12), fg = "cyan3", bg = "gray3").grid(row=6,column=6,ipadx=30,ipady=5)
d12b6 = tk.Button(main, text = ("6d12"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(6,12), fg = "cyan3", bg = "gray3").grid(row=6,column=7,ipadx=30,ipady=5)

d20b = tk.Button(main, text = ("d20"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(1,20), fg = "blue violet", bg = "gray3").grid(row=7,column=2,ipadx=30,ipady=5)
d20b2 = tk.Button(main, text = ("2d20"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(2,20), fg = "blue violet", bg = "gray3").grid(row=7,column=3,ipadx=30,ipady=5)
d20b3 = tk.Button(main, text = ("3d20"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(3,20), fg = "blue violet", bg = "gray3").grid(row=7,column=4,ipadx=30,ipady=5)
d20b4 = tk.Button(main, text = ("4d20"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(4,20), fg = "blue violet", bg = "gray3").grid(row=7,column=5,ipadx=30,ipady=5)
d20b5 = tk.Button(main, text = ("5d20"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(5,20), fg = "blue violet", bg = "gray3").grid(row=7,column=6,ipadx=30,ipady=5)
d20b6 = tk.Button(main, text = ("6d20"), font = ("kimberly_BI"),
            command = lambda : Roll_d6(6,20), fg = "blue violet", bg = "gray3").grid(row=7,column=7,ipadx=30,ipady=5)

### Numbers and Processe
counter = tk.Label(main, textvariable = number_i, font = ("kimberly_BI 72"),
              fg = "gray99", bg = "gray3").grid(row=0,column=8,ipadx=100)

log = tk.Text(main, height=7, width=18, bg = "dark slate gray", fg = "SeaGreen1").grid(row=0,column=1,ipadx=100)

main.mainloop()
