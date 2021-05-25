import math as mt
from tkinter.constants import S
import numpy as np
import os
import config as cf
import random as rd
import winsound as ws
#import graphics as gp

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

RESOLUTION = cf.Resolution
SCALE = cf.Scale

change_sfx_i = 'D:/Users/Frank/Desktop/Science/Python Projects/Game Super Dice/sounds/select_100-0.wav'
roll_sfx_i = 'D:/Users/Frank/Desktop/Science/Python Projects/Game Super Dice/sounds/select_100-5.wav'

main = tk.Tk()
main.geometry(RESOLUTION)
main.title("Game Super Dice")
main.configure(background="gray10")
main.clipboard_get

DATABASE = {
  'Wild Dice': ['Wild_Dice.png', None]
}

def g_get(name):
  if name in DATABASE:
    if DATABASE[name][1] is None:
      print('loading image:', name)
      DATABASE[name][1] = tk.PhotoImage(file=DATABASE[name][0])
    return DATABASE[name][1]
  return None

number_i = tk.IntVar()
number_ii = tk.IntVar()
number_iii = tk.IntVar()
number_iv = tk.IntVar()
number_v = tk.IntVar()
number_vi = tk.IntVar()

V_INDEX = [number_i,number_ii,number_iii,number_iv,number_v,number_vi]

### Rollers
def Roll_Dice(quanity, sides, special):
    steps = 0
    a = 0
    b = 0
    r = quanity
    t = number_v.get()
    while steps < quanity:
            roll = rd.randint(1,sides)
            if roll <= t and r > 0:
                roll = rd.randint(1,sides)
            a = a + roll
            steps = steps + 1
    while steps == quanity:
            mod = number_ii.get()
            wild_check = number_vi.get()
            a = a + mod
            if wild_check == 1:
                b = rd.randint(1,6)
                if b > a:
                    a = b
                    number_i.set(a)
            else:
                number_i.set(a)
            if special is 'percent':
                log.config(state="normal")
                log.insert(tk.INSERT, "["+str(a)+"%]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
            else:
                log.config(state="normal")
                log.insert(tk.INSERT, "["+str(a)+"]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
            if cf.Reset_After_Roll is True:
                number_ii.set(0)
                number_iii.set(0)
                number_iv.set(0)
                number_v.set(0)
                number_vi.set(0)
            return a
    while quanity == -1 and sides == -1:
            q = number_iii.get()
            s = number_iv.get()
            quanity == q
            sides = s
            if q <= 0 or s <= 0:
                log.config(state="normal")
                log.insert(tk.INSERT, "[No Negative Numbers]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
                if cf.Reset_After_Roll is True:
                    number_ii.set(0)
                    number_iii.set(0)
                    number_iv.set(0)
                    number_v.set(0)
                    number_vi.set(0)
                return a
            while steps < q and q > 0:
                a = a + rd.randint(1,sides)
                steps = steps + 1
                while steps == q:
                    mod = number_ii.get()
                    wild_check = number_vi.get()
                    a = a + mod
                    if wild_check == 1:
                        b = rd.randint(1,6)
                        if b > a:
                            a = b
                            number_i.set(a)
                    else:
                        number_i.set(a)
                    log.config(state="normal")
                    log.insert(tk.INSERT, "["+str(a)+"]")
                    log.config(state="disabled")
                    if cf.Sounds is True:
                        ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
                    if cf.Reset_After_Roll is True:
                        number_ii.set(0)
                        number_iii.set(0)
                        number_iv.set(0)
                        number_v.set(0)
                        number_vi.set(0)
                    return a

def Determined_Direction():
    steps = 0
    a = 0
    quanity = 1
    while steps < quanity:
            a = a + rd.randint(1,360)
            steps = steps + 1
    while steps == quanity:
            number_i.set(a)
            if cf.Direction_Output is 'Degrees':
                log.config(state="normal")
                log.insert(tk.INSERT, "["+str(a)+"]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
                return a
            elif cf.Direction_Output is 'Radians':
                b = (a*mt.pi)/180
                log.config(state="normal")
                log.insert(tk.INSERT, "["+str(round(b,1))+"]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
                return a
            elif cf.Direction_Output is 'Compass':
                compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
                b = (a/45)-1
                log.config(state="normal")
                log.insert(tk.INSERT, "["+compass[int(round(b,0))]+"]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
                return a
            elif cf.Direction_Output is 'Advance_Compass':
                compass = ["N", "NNE", "NE", "NEE", "E", "SEE", "SE", "SSE", "S", "SSW", "SW", "SWW", "W", "NWW", "NW", "NNW"]
                b = (a/22.5)-1
                log.config(state="normal")
                log.insert(tk.INSERT, "["+compass[int(round(b,0))]+"]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
                return a
            elif cf.Direction_Output is 'Simple_Compass':
                compass = ["N", "E", "S", "W"]
                b = (a/90)-1
                log.config(state="normal")
                log.insert(tk.INSERT, "["+compass[int(round(b,0))]+"]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)
                return a
            else:
                log.config(state="normal")
                log.insert(tk.INSERT, "[Error, you need the correct direction string. Check config]")
                log.config(state="disabled")
                if cf.Sounds is True:
                    ws.PlaySound('SystemExclamation', ws.SND_ASYNC)
                return a

def Clear_Log():
    log.config(state="normal")
    log.delete('1.0', tk.END)
    log.config(state="disabled")
    if cf.Sounds is True:
        ws.PlaySound(roll_sfx_i, ws.SND_ASYNC)

def Modifier(num):
    get = number_ii.get()
    b = num + get
    number_ii.set(b)
    if cf.Sounds is True:
        ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
    return b

def Set_Custom_Quanity(num):
    a = number_iii.get()
    if a < 0:
        q = 0
        number_iii.set(q)
        if cf.Sounds is True:
            ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
        return q
    else:
        q = num + a
        number_iii.set(q)
        if cf.Sounds is True:
            ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
        return q

def Set_Custom_Sides(num):
    a = number_iv.get()
    if a < 0:
        s = 0
        number_iv.set(s)
        if cf.Sounds is True:
            ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
        return s
    else:
        s = num + a
        number_iv.set(s)
        if cf.Sounds is True:
            ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
        return s

def Set_Reroll(num):
    a = number_v.get()
    if a < 0:
        r = 0
        number_v.set(r)
        if cf.Sounds is True:
            ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
        return r
    else:
        r = num + a
        number_v.set(r)
        if cf.Sounds is True:
            ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
        return r

def Reset(num, l):
    l[num].set(0)

def wild_change(num):
    if num == 0:
        number_vi.set(0)
        if cf.Sounds is True:
            ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
        return 0
    elif num == 1:
        number_vi.set(1)
        if cf.Sounds is True:
            ws.PlaySound(change_sfx_i, ws.SND_ASYNC)
        return 1
    else:
        print("This has to be 0 OFF or 1 ON")

def fifty_two_cards(jokers):
    suite = ["Spades", "Hearts", "Diamonds", "Clubs", "Joker"]
    r = rd.randint(1,13)
    if jokers is True:
        s = rd.randint(0,4)
    else:
        s = rd.randint(0,3)
    log.config(state="normal")
    if s == 4:
        log.insert(tk.INSERT, "["+suite[4]+"]")
    else:
        log.insert(tk.INSERT, "["+str(r)+" of "+suite[s]+"]")
    log.config(state="disabled")
    return r


### Dices
d2b = tk.Button(main, text = ("d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=2,ipadx=30*SCALE,ipady=5*SCALE)
d2b2 = tk.Button(main, text = ("2d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=3,ipadx=30*SCALE,ipady=5*SCALE)
d2b3 = tk.Button(main, text = ("3d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=4,ipadx=30*SCALE,ipady=5*SCALE)
d2b4 = tk.Button(main, text = ("4d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=5,ipadx=30*SCALE,ipady=5*SCALE)
d2b5 = tk.Button(main, text = ("5d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=6,ipadx=30*SCALE,ipady=5*SCALE)
d2b6 = tk.Button(main, text = ("6d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=7,ipadx=30*SCALE,ipady=5*SCALE)
d2b7 = tk.Button(main, text = ("7d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=8,ipadx=30*SCALE,ipady=5*SCALE)
d2b8 = tk.Button(main, text = ("8d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=9,ipadx=30*SCALE,ipady=5*SCALE)
d2b9 = tk.Button(main, text = ("9d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=10,ipadx=30*SCALE,ipady=5*SCALE)
d2b10 = tk.Button(main, text = ("10d2"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=11,ipadx=30*SCALE,ipady=5*SCALE)
d2b11 = tk.Button(main, text = ("11d2"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=12,ipadx=30*SCALE,ipady=5*SCALE)
d2b12 = tk.Button(main, text = ("12d2"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,2,'none'), fg = "red3", bg = "gray3").grid(row=1,column=13,ipadx=30*SCALE,ipady=5*SCALE)
                   

d4b = tk.Button(main, text = ("d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=2,ipadx=30*SCALE,ipady=5*SCALE)
d4b2 = tk.Button(main, text = ("2d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=3,ipadx=30*SCALE,ipady=5*SCALE)
d4b3 = tk.Button(main, text = ("3d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=4,ipadx=30*SCALE,ipady=5*SCALE)
d4b4 = tk.Button(main, text = ("4d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=5,ipadx=30*SCALE,ipady=5*SCALE)
d4b5 = tk.Button(main, text = ("5d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=6,ipadx=30*SCALE,ipady=5*SCALE)
d4b6 = tk.Button(main, text = ("6d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=7,ipadx=30*SCALE,ipady=5*SCALE)
d4b7 = tk.Button(main, text = ("7d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=8,ipadx=30*SCALE,ipady=5*SCALE)
d4b8 = tk.Button(main, text = ("8d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=9,ipadx=30*SCALE,ipady=5*SCALE)
d4b9 = tk.Button(main, text = ("9d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=10,ipadx=30*SCALE,ipady=5*SCALE)
d4b10 = tk.Button(main, text = ("10d4"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=11,ipadx=30*SCALE,ipady=5*SCALE)
d4b11 = tk.Button(main, text = ("11d4"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=12,ipadx=30*SCALE,ipady=5*SCALE)
d4b12 = tk.Button(main, text = ("12d4"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,4,'none'), fg = "orange", bg = "gray3").grid(row=2,column=13,ipadx=30*SCALE,ipady=5*SCALE)


d6b = tk.Button(main, text = ("d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=2,ipadx=30*SCALE,ipady=5*SCALE)
d6b2 = tk.Button(main, text = ("2d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=3,ipadx=30*SCALE,ipady=5*SCALE)
d6b3 = tk.Button(main, text = ("3d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=4,ipadx=30*SCALE,ipady=5*SCALE)
d6b4 = tk.Button(main, text = ("4d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=5,ipadx=30*SCALE,ipady=5*SCALE)
d6b5 = tk.Button(main, text = ("5d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=6,ipadx=30*SCALE,ipady=5*SCALE)
d6b6 = tk.Button(main, text = ("6d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=7,ipadx=30*SCALE,ipady=5*SCALE)
d6b7 = tk.Button(main, text = ("7d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=8,ipadx=30*SCALE,ipady=5*SCALE)
d6b8 = tk.Button(main, text = ("8d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=9,ipadx=30*SCALE,ipady=5*SCALE)
d6b9 = tk.Button(main, text = ("9d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=10,ipadx=30*SCALE,ipady=5*SCALE)
d6b10 = tk.Button(main, text = ("10d6"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=11,ipadx=30*SCALE,ipady=5*SCALE)
d6b11 = tk.Button(main, text = ("11d6"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=12,ipadx=30*SCALE,ipady=5*SCALE)
d6b12 = tk.Button(main, text = ("12d6"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,6,'none'), fg = "yellow3", bg = "gray3").grid(row=3,column=13,ipadx=30*SCALE,ipady=5*SCALE)

d8b = tk.Button(main, text = ("d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=2,ipadx=30*SCALE,ipady=5*SCALE)
d8b2 = tk.Button(main, text = ("2d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=3,ipadx=30*SCALE,ipady=5*SCALE)
d8b3 = tk.Button(main, text = ("3d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=4,ipadx=30*SCALE,ipady=5*SCALE)
d8b4 = tk.Button(main, text = ("4d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=5,ipadx=30*SCALE,ipady=5*SCALE)
d8b5 = tk.Button(main, text = ("5d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=6,ipadx=30*SCALE,ipady=5*SCALE)
d8b6 = tk.Button(main, text = ("6d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=7,ipadx=30*SCALE,ipady=5*SCALE)
d8b7 = tk.Button(main, text = ("7d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=8,ipadx=30*SCALE,ipady=5*SCALE)
d8b8 = tk.Button(main, text = ("8d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=9,ipadx=30*SCALE,ipady=5*SCALE)
d8b9 = tk.Button(main, text = ("9d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=10,ipadx=30*SCALE,ipady=5*SCALE)
d8b10 = tk.Button(main, text = ("10d8"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=11,ipadx=30*SCALE,ipady=5*SCALE)
d8b11 = tk.Button(main, text = ("11d8"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=12,ipadx=30*SCALE,ipady=5*SCALE)
d8b12 = tk.Button(main, text = ("12d8"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,8,'none'), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=13,ipadx=30*SCALE,ipady=5*SCALE)

d10b = tk.Button(main, text = ("d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=2,ipadx=30*SCALE,ipady=5*SCALE)
d10b2 = tk.Button(main, text = ("2d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=3,ipadx=30*SCALE,ipady=5*SCALE)
d10b3 = tk.Button(main, text = ("3d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=4,ipadx=30*SCALE,ipady=5*SCALE)
d10b4 = tk.Button(main, text = ("4d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=5,ipadx=30*SCALE,ipady=5*SCALE)
d10b5 = tk.Button(main, text = ("5d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=6,ipadx=30*SCALE,ipady=5*SCALE)
d10b6 = tk.Button(main, text = ("6d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=7,ipadx=30*SCALE,ipady=5*SCALE)
d10b7 = tk.Button(main, text = ("7d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=8,ipadx=30*SCALE,ipady=5*SCALE)
d10b8 = tk.Button(main, text = ("8d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=9,ipadx=30*SCALE,ipady=5*SCALE)
d10b9 = tk.Button(main, text = ("9d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=10,ipadx=30*SCALE,ipady=5*SCALE)
d10b10 = tk.Button(main, text = ("10d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=11,ipadx=30*SCALE,ipady=5*SCALE)
d10b11 = tk.Button(main, text = ("11d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=12,ipadx=30*SCALE,ipady=5*SCALE)
d10b12 = tk.Button(main, text = ("12d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,10,'none'), fg = "green3", bg = "gray3").grid(row=5,column=13,ipadx=30*SCALE,ipady=5*SCALE)

d12b = tk.Button(main, text = ("d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=2,ipadx=30*SCALE,ipady=5*SCALE)
d12b2 = tk.Button(main, text = ("2d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=3,ipadx=30*SCALE,ipady=5*SCALE)
d12b3 = tk.Button(main, text = ("3d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=4,ipadx=30*SCALE,ipady=5*SCALE)
d12b4 = tk.Button(main, text = ("4d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=5,ipadx=30*SCALE,ipady=5*SCALE)
d12b5 = tk.Button(main, text = ("5d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=6,ipadx=30*SCALE,ipady=5*SCALE)
d12b6 = tk.Button(main, text = ("6d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=7,ipadx=30*SCALE,ipady=5*SCALE)
d12b7 = tk.Button(main, text = ("7d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=8,ipadx=30*SCALE,ipady=5*SCALE)
d12b8 = tk.Button(main, text = ("8d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=9,ipadx=30*SCALE,ipady=5*SCALE)
d12b9 = tk.Button(main, text = ("9d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=10,ipadx=30*SCALE,ipady=5*SCALE)
d12b10 = tk.Button(main, text = ("10d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=11,ipadx=30*SCALE,ipady=5*SCALE)
d12b11 = tk.Button(main, text = ("11d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=12,ipadx=30*SCALE,ipady=5*SCALE)
d12b12 = tk.Button(main, text = ("12d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,12,'none'), fg = "cyan3", bg = "gray3").grid(row=6,column=13,ipadx=30*SCALE,ipady=5*SCALE)


d20b = tk.Button(main, text = ("d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=2,ipadx=30*SCALE,ipady=5*SCALE)
d20b2 = tk.Button(main, text = ("2d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=3,ipadx=30*SCALE,ipady=5*SCALE)
d20b3 = tk.Button(main, text = ("3d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=4,ipadx=30*SCALE,ipady=5*SCALE)
d20b4 = tk.Button(main, text = ("4d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=5,ipadx=30*SCALE,ipady=5*SCALE)
d20b5 = tk.Button(main, text = ("5d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=6,ipadx=30*SCALE,ipady=5*SCALE)
d20b6 = tk.Button(main, text = ("6d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=7,ipadx=30*SCALE,ipady=5*SCALE)
d20b7 = tk.Button(main, text = ("7d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=8,ipadx=30*SCALE,ipady=5*SCALE)
d20b8 = tk.Button(main, text = ("8d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=9,ipadx=30*SCALE,ipady=5*SCALE)
d20b9 = tk.Button(main, text = ("9d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=10,ipadx=30*SCALE,ipady=5*SCALE)
d20b10 = tk.Button(main, text = ("10d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=11,ipadx=30*SCALE,ipady=5*SCALE)
d20b11 = tk.Button(main, text = ("11d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=12,ipadx=30*SCALE,ipady=5*SCALE)
d20b12 = tk.Button(main, text = ("12d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,20,'none'), fg = "blue violet", bg = "gray3").grid(row=7,column=13,ipadx=30*SCALE,ipady=5*SCALE)

dc_p1 = tk.Button(main, text = ("Quanity +1"), font = (cf.Base_Font),
            command = lambda : Set_Custom_Quanity(1), fg = "gray99", bg = "gray3").grid(row=8,column=3,ipadx=11*SCALE,ipady=5*SCALE)
dc_p5 = tk.Button(main, text = ("Quanity +5"), font = (cf.Base_Font),
            command = lambda : Set_Custom_Quanity(5), fg = "gray99", bg = "gray3").grid(row=9,column=3,ipadx=11*SCALE,ipady=5*SCALE)
dc_m1 = tk.Button(main, text = ("Quanity -1"), font = (cf.Base_Font),
            command = lambda : Set_Custom_Quanity(-1), fg = "gray99", bg = "gray3").grid(row=10,column=3,ipadx=11*SCALE,ipady=5*SCALE)
dc_m5 = tk.Button(main, text = ("Quanity -5"), font = (cf.Base_Font),
            command = lambda : Set_Custom_Quanity(-5), fg = "gray99", bg = "gray3").grid(row=11,column=3,ipadx=11*SCALE,ipady=5*SCALE)

bc_p1 = tk.Button(main, text = ("Sides +1"), font = (cf.Base_Font),
            command = lambda : Set_Custom_Sides(1), fg = "gray99", bg = "gray3").grid(row=8,column=4,ipadx=17*SCALE,ipady=5*SCALE)
bc_p5 = tk.Button(main, text = ("Sides +5"), font = (cf.Base_Font),
            command = lambda : Set_Custom_Sides(5), fg = "gray99", bg = "gray3").grid(row=9,column=4,ipadx=17*SCALE,ipady=5*SCALE)
bc_m1 = tk.Button(main, text = ("Sides -1"), font = (cf.Base_Font),
            command = lambda : Set_Custom_Sides(-1), fg = "gray99", bg = "gray3").grid(row=10,column=4,ipadx=17*SCALE,ipady=5*SCALE)
bc_m5 = tk.Button(main, text = ("Sides -5"), font = (cf.Base_Font),
            command = lambda : Set_Custom_Sides(-5), fg = "gray99", bg = "gray3").grid(row=11,column=4,ipadx=17*SCALE,ipady=5*SCALE)

roll = tk.Button(main, text = ("Roll Custom"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(-1,-1,'none'), fg = "gray99", bg = "gray3").grid(row=8,column=2,ipadx=2*SCALE,ipady=5*SCALE)

fifty_two_cards_button_with_joker = tk.Button(main, text = ("52 Cards WJ"), font = (cf.Base_Font),
            command = lambda : fifty_two_cards(True), fg = "sky blue", bg = "gray3").grid(row=8,column=9,ipadx=39*SCALE,ipady=5*SCALE)

fifty_two_cards_button = tk.Button(main, text = ("52 Cards"), font = (cf.Base_Font),
            command = lambda : fifty_two_cards(False), fg = "sky blue", bg = "gray3").grid(row=9,column=9,ipadx=39*SCALE,ipady=5*SCALE)

wild_on = tk.Button(main, text = ("Wild On"), font = (cf.Base_Font),
            command = lambda : wild_change(1), fg = "yellow1", bg = "gray3").grid(row=8,column=8,ipadx=39*SCALE,ipady=5*SCALE)

wild_off = tk.Button(main, text = ("Wild Off"), font = (cf.Base_Font),
            command = lambda : wild_change(0), fg = "yellow4", bg = "gray3").grid(row=9,column=8,ipadx=39*SCALE,ipady=5*SCALE)
            
direction = tk.Button(main, text = ("┼"), font = (cf.Base_Font),
            command = lambda : Determined_Direction(), fg = "gray99", bg = "gray3").grid(row=8,column=7,ipadx=39*SCALE,ipady=5*SCALE)

percentage = tk.Button(main, text = ("%"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,100,'percent'), fg = "gray99", bg = "gray3").grid(row=8,column=6,ipadx=40*SCALE,ipady=5*SCALE)

reroll_plus = tk.Button(main, text = ("Reroll +1"), font = (cf.Base_Font),
            command = lambda : Set_Reroll(1), fg = "gray99", bg = "gray3").grid(row=9,column=6,ipadx=1*SCALE,ipady=5*SCALE)
            
reroll_minus = tk.Button(main, text = ("Reroll -1"), font = (cf.Base_Font),
            command = lambda : Set_Reroll(-1), fg = "gray99", bg = "gray3").grid(row=10,column=6,ipadx=1*SCALE,ipady=5*SCALE)

clear_button = tk.Button(main, text = ("Clear Log"), font = (cf.Base_Font),
            command = lambda : Clear_Log(), fg = "gray1", bg = "brown1").grid(row=1,column=1,ipadx=30*SCALE,ipady=5*SCALE)

### Modifier Addition
plus_1 = tk.Button(main, text = ("+1  "), font = (cf.Base_Font),
            command = lambda : Modifier(1), fg = "gray1", bg = "CadetBlue1").grid(row=12,column=2,ipadx=30*SCALE,ipady=5*SCALE)
plus_2 = tk.Button(main, text = ("+2  "), font = (cf.Base_Font),
            command = lambda : Modifier(2), fg = "gray1", bg = "CadetBlue1").grid(row=13,column=2,ipadx=30*SCALE,ipady=5*SCALE)
plus_5 = tk.Button(main, text = ("+5  "), font = (cf.Base_Font),
            command = lambda : Modifier(5), fg = "gray1", bg = "CadetBlue1").grid(row=14,column=2,ipadx=30*SCALE,ipady=5*SCALE)
plus_10 = tk.Button(main, text = ("+10"), font = (cf.Base_Font),
            command = lambda : Modifier(10), fg = "gray1", bg = "CadetBlue1").grid(row=15,column=2,ipadx=30*SCALE,ipady=5*SCALE)

minus_1 = tk.Button(main, text = ("-1  "), font = (cf.Base_Font),
            command = lambda : Modifier(-1), fg = "gray1", bg = "IndianRed1").grid(row=12,column=3,ipadx=30*SCALE,ipady=5*SCALE)
minus_2 = tk.Button(main, text = ("-2  "), font = (cf.Base_Font),
            command = lambda : Modifier(-2), fg = "gray1", bg = "IndianRed1").grid(row=13,column=3,ipadx=30*SCALE,ipady=5*SCALE)
minus_5 = tk.Button(main, text = ("-5  "), font = (cf.Base_Font),
            command = lambda : Modifier(-5), fg = "gray1", bg = "IndianRed1").grid(row=14,column=3,ipadx=30*SCALE,ipady=5*SCALE)
minus_10 = tk.Button(main, text = ("-10"), font = (cf.Base_Font),
            command = lambda : Modifier(-10), fg = "gray1", bg = "IndianRed1").grid(row=15,column=3,ipadx=30*SCALE,ipady=5*SCALE)

### Resets
reset_quanities = tk.Button(main, text = ("Reset Quanities"), font = (cf.Base_Font),
            command = lambda : Reset(2,V_INDEX), fg = "gray99", bg = "gray3").grid(row=12,column=6,ipadx=1*SCALE,ipady=5*SCALE)

reset_sides = tk.Button(main, text = ("Reset Sides"), font = (cf.Base_Font),
            command = lambda : Reset(3,V_INDEX), fg = "gray99", bg = "gray3").grid(row=13,column=6,ipadx=1*SCALE,ipady=5*SCALE)

reset_mod = tk.Button(main, text = ("Reset Modifier"), font = (cf.Base_Font),
            command = lambda : Reset(1,V_INDEX), fg = "Darkorchid4", bg = "gray3").grid(row=14,column=6,ipadx=1*SCALE,ipady=5*SCALE)

reset_reroll = tk.Button(main, text = ("Reset Reroll"), font = (cf.Base_Font),
            command = lambda : Reset(4,V_INDEX), fg = "red3", bg = "gray3").grid(row=15,column=6,ipadx=1*SCALE,ipady=5*SCALE)

### Numbers and Processes
counter = tk.Label(main, textvariable = number_i, font = (cf.Counter_Font),
              fg = "gray99", bg = "gray3").grid(row=0,column=14,ipadx=100*SCALE)

modifier = tk.Label(main, textvariable = number_ii, font = (cf.Modifier_Font),
              fg = "gray99", bg = "Darkorchid4").grid(row=9,column=1,ipadx=150*SCALE)

custom_quanities = tk.Label(main, textvariable = number_iii, font = (cf.Modifier_Font),
              fg = "gray99", bg = "RoyalBlue2").grid(row=8,column=0,ipadx=1*SCALE)

custom_sides = tk.Label(main, textvariable = number_iv, font = (cf.Modifier_Font),
              fg = "gray99", bg = "Brown2").grid(row=8,column=1,ipadx=150*SCALE)

direction_type = tk.Label(main, text = cf.Direction_Output, font = ('system'),
              fg = "gray99", bg = "gray3").grid(row=8,column=14,ipadx=150*SCALE)

game_set = tk.Label(main, text = cf.Game, font = ('system'),
              fg = "gray99", bg = "gray3").grid(row=9,column=14,ipadx=150*SCALE)

rerolls = tk.Label(main, textvariable = number_v, font = (cf.Modifier_Font),
              fg = "gray99", bg = "red3").grid(row=10,column=1,ipadx=150*SCALE)

wild_dice_var = tk.Label(main, textvariable = number_vi, font = (cf.Modifier_Font),
              fg = "gray99", bg = "orange3").grid(row=11,column=1,ipadx=150*SCALE)

log = tk.Text(main, height=7, width=18, bg = "dark slate gray", fg = "SeaGreen1")
log.grid(row=0,column=1,ipadx=100*SCALE)
log.config(state="disabled")

main.mainloop()