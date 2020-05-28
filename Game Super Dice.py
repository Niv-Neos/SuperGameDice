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
main.configure(background="gray10")
main.clipboard_get

number_i = tk.IntVar()
number_ii = tk.IntVar()
hold_i = 0

### Rollers
def Roll_Dice(quanity, sides):
       steps = 0
       a = 0
       while steps < quanity:
              a = a + rd.randint(1,sides)
              steps = steps + 1
       while steps == quanity:
              mod = number_ii.get()
              a = a + mod
              number_i.set(a)
              log.config(state="normal")
              log.insert(tk.INSERT, "["+str(a)+"]")
              log.config(state="disabled")
              if hold_i is 0:
                  number_ii.set(0)
              return a

def Clear_Log():
        log.config(state="normal")
        log.delete('1.0', tk.END)
        log.config(state="disabled")

def Modifier(num):
        get = number_ii.get()
        b = num + get
        number_ii.set(b)
        return b

def Modifier_Hold(state):
        trigger = state
        if trigger is 0:
            hold_i = 0
            Mod_Hold_Text()
            return hold_i
        elif trigger is 1:
            hold_i = 1
            Mod_Hold_Text()
            return hold_i

def Mod_Hold_Text():
        while hold_i is 1:
            return "Modifier Hold: ON"
        while hold_i is 0:
            return "Modifier Hold: OFF"
            
### Dices
d2b = tk.Button(main, text = ("d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,2), fg = "red3", bg = "gray3").grid(row=1,column=2,ipadx=30,ipady=5)
d2b2 = tk.Button(main, text = ("2d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,2), fg = "red3", bg = "gray3").grid(row=1,column=3,ipadx=30,ipady=5)
d2b3 = tk.Button(main, text = ("3d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,2), fg = "red3", bg = "gray3").grid(row=1,column=4,ipadx=30,ipady=5)
d2b4 = tk.Button(main, text = ("4d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,2), fg = "red3", bg = "gray3").grid(row=1,column=5,ipadx=30,ipady=5)
d2b5 = tk.Button(main, text = ("5d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,2), fg = "red3", bg = "gray3").grid(row=1,column=6,ipadx=30,ipady=5)
d2b6 = tk.Button(main, text = ("6d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,2), fg = "red3", bg = "gray3").grid(row=1,column=7,ipadx=30,ipady=5)

d4b = tk.Button(main, text = ("d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,4), fg = "orange", bg = "gray3").grid(row=2,column=2,ipadx=30,ipady=5)
d4b2 = tk.Button(main, text = ("2d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,4), fg = "orange", bg = "gray3").grid(row=2,column=3,ipadx=30,ipady=5)
d4b3 = tk.Button(main, text = ("3d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,4), fg = "orange", bg = "gray3").grid(row=2,column=4,ipadx=30,ipady=5)
d4b4 = tk.Button(main, text = ("4d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,4), fg = "orange", bg = "gray3").grid(row=2,column=5,ipadx=30,ipady=5)
d4b5 = tk.Button(main, text = ("5d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,4), fg = "orange", bg = "gray3").grid(row=2,column=6,ipadx=30,ipady=5)
d4b6 = tk.Button(main, text = ("6d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,4), fg = "orange", bg = "gray3").grid(row=2,column=7,ipadx=30,ipady=5)

d6b = tk.Button(main, text = ("d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,6), fg = "yellow3", bg = "gray3").grid(row=3,column=2,ipadx=30,ipady=5)
d6b2 = tk.Button(main, text = ("2d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,6), fg = "yellow3", bg = "gray3").grid(row=3,column=3,ipadx=30,ipady=5)
d6b3 = tk.Button(main, text = ("3d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,6), fg = "yellow3", bg = "gray3").grid(row=3,column=4,ipadx=30,ipady=5)
d6b4 = tk.Button(main, text = ("4d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,6), fg = "yellow3", bg = "gray3").grid(row=3,column=5,ipadx=30,ipady=5)
d6b5 = tk.Button(main, text = ("5d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,6), fg = "yellow3", bg = "gray3").grid(row=3,column=6,ipadx=30,ipady=5)
d6b6 = tk.Button(main, text = ("6d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,6), fg = "yellow3", bg = "gray3").grid(row=3,column=7,ipadx=30,ipady=5)

d8b = tk.Button(main, text = ("d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=2,ipadx=30,ipady=5)
d8b2 = tk.Button(main, text = ("2d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=3,ipadx=30,ipady=5)
d8b3 = tk.Button(main, text = ("3d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=4,ipadx=30,ipady=5)
d8b4 = tk.Button(main, text = ("4d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=5,ipadx=30,ipady=5)
d8b5 = tk.Button(main, text = ("5d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=6,ipadx=30,ipady=5)
d8b6 = tk.Button(main, text = ("6d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,8), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=7,ipadx=30,ipady=5)

d10b = tk.Button(main, text = ("d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,10), fg = "green3", bg = "gray3").grid(row=5,column=2,ipadx=30,ipady=5)
d10b2 = tk.Button(main, text = ("2d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,10), fg = "green3", bg = "gray3").grid(row=5,column=3,ipadx=30,ipady=5)
d10b3 = tk.Button(main, text = ("3d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,10), fg = "green3", bg = "gray3").grid(row=5,column=4,ipadx=30,ipady=5)
d10b4 = tk.Button(main, text = ("4d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,10), fg = "green3", bg = "gray3").grid(row=5,column=5,ipadx=30,ipady=5)
d10b5 = tk.Button(main, text = ("5d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,10), fg = "green3", bg = "gray3").grid(row=5,column=6,ipadx=30,ipady=5)
d10b6 = tk.Button(main, text = ("6d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,10), fg = "green3", bg = "gray3").grid(row=5,column=7,ipadx=30,ipady=5)

d12b = tk.Button(main, text = ("d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,12), fg = "cyan3", bg = "gray3").grid(row=6,column=2,ipadx=30,ipady=5)
d12b2 = tk.Button(main, text = ("2d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,12), fg = "cyan3", bg = "gray3").grid(row=6,column=3,ipadx=30,ipady=5)
d12b3 = tk.Button(main, text = ("3d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,12), fg = "cyan3", bg = "gray3").grid(row=6,column=4,ipadx=30,ipady=5)
d12b4 = tk.Button(main, text = ("4d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,12), fg = "cyan3", bg = "gray3").grid(row=6,column=5,ipadx=30,ipady=5)
d12b5 = tk.Button(main, text = ("5d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,12), fg = "cyan3", bg = "gray3").grid(row=6,column=6,ipadx=30,ipady=5)
d12b6 = tk.Button(main, text = ("6d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,12), fg = "cyan3", bg = "gray3").grid(row=6,column=7,ipadx=30,ipady=5)

d20b = tk.Button(main, text = ("d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,20), fg = "blue violet", bg = "gray3").grid(row=7,column=2,ipadx=30,ipady=5)
d20b2 = tk.Button(main, text = ("2d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,20), fg = "blue violet", bg = "gray3").grid(row=7,column=3,ipadx=30,ipady=5)
d20b3 = tk.Button(main, text = ("3d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,20), fg = "blue violet", bg = "gray3").grid(row=7,column=4,ipadx=30,ipady=5)
d20b4 = tk.Button(main, text = ("4d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,20), fg = "blue violet", bg = "gray3").grid(row=7,column=5,ipadx=30,ipady=5)
d20b5 = tk.Button(main, text = ("5d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,20), fg = "blue violet", bg = "gray3").grid(row=7,column=6,ipadx=30,ipady=5)
d20b6 = tk.Button(main, text = ("6d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,20), fg = "blue violet", bg = "gray3").grid(row=7,column=7,ipadx=30,ipady=5)

clear_button = tk.Button(main, text = ("Clear Log"), font = (cf.Base_Font),
            command = lambda : Clear_Log(), fg = "red4", bg = "brown1").grid(row=1,column=1,ipadx=30,ipady=5)

### Modifier Addition
plus_1 = tk.Button(main, text = ("+1  "), font = (cf.Base_Font),
            command = lambda : Modifier(1), fg = "gray1", bg = "CadetBlue1").grid(row=9,column=2,ipadx=30,ipady=5)
plus_2 = tk.Button(main, text = ("+2  "), font = (cf.Base_Font),
            command = lambda : Modifier(2), fg = "gray1", bg = "CadetBlue1").grid(row=10,column=2,ipadx=30,ipady=5)
plus_5 = tk.Button(main, text = ("+5  "), font = (cf.Base_Font),
            command = lambda : Modifier(5), fg = "gray1", bg = "CadetBlue1").grid(row=11,column=2,ipadx=30,ipady=5)
plus_10 = tk.Button(main, text = ("+10 "), font = (cf.Base_Font),
            command = lambda : Modifier(10), fg = "gray1", bg = "CadetBlue1").grid(row=12,column=2,ipadx=30,ipady=5)

minus_1 = tk.Button(main, text = ("-1  "), font = (cf.Base_Font),
            command = lambda : Modifier(-1), fg = "gray1", bg = "IndianRed1").grid(row=9,column=3,ipadx=30,ipady=5)
minus_2 = tk.Button(main, text = ("-2  "), font = (cf.Base_Font),
            command = lambda : Modifier(-2), fg = "gray1", bg = "IndianRed1").grid(row=10,column=3,ipadx=30,ipady=5)
minus_5 = tk.Button(main, text = ("-5  "), font = (cf.Base_Font),
            command = lambda : Modifier(-5), fg = "gray1", bg = "IndianRed1").grid(row=11,column=3,ipadx=30,ipady=5)
minus_10 = tk.Button(main, text = ("-10 "), font = (cf.Base_Font),
            command = lambda : Modifier(-10), fg = "gray1", bg = "IndianRed1").grid(row=12,column=3,ipadx=30,ipady=5)

hold_on = tk.Button(main, text = ("Modifier Stick"), font = (cf.Base_Font),
            command = lambda : Modifier_Hold(1), fg = "gray1", bg = "CadetBlue3").grid(row=13,column=2,ipady=5)
hold_off = tk.Button(main, text = ("Modifier Clear"), font = (cf.Base_Font),
            command = lambda : Modifier_Hold(0), fg = "gray1", bg = "IndianRed3").grid(row=13,column=3,ipady=5)


### Numbers and Processe
counter = tk.Label(main, textvariable = number_i, font = (cf.Counter_Font),
              fg = "gray99", bg = "gray3").grid(row=0,column=8,ipadx=100)

modifier = tk.Label(main, textvariable = number_ii, font = (cf.Modifier_Font),
              fg = "gray99", bg = "Darkorchid4").grid(row=9,column=1,ipadx=150)
modifier_toggle = tk.Label(main, text = Mod_Hold_Text(), font = (cf.Modifier_Font),
              fg = "gray99", bg = "Darkorchid4").grid(row=10,column=1,ipadx=0)

log = tk.Text(main, height=7, width=18, bg = "dark slate gray", fg = "SeaGreen1")
log.grid(row=0,column=1,ipadx=100)
log.config(state="disabled")

main.mainloop()
