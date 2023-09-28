import math as mt
import tkinter as tk
from tkinter.constants import S, X
import numpy as np
#import os
import config as cf
import random as rd
import winsound as ws
#import sound_database as sd
#import graphics as gp
'''
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
'''

RESOLUTION = cf.Resolution
SCALE = cf.Scale

change_sfx_i = cf.Sound_Theme[0]
roll_sfx_i = cf.Sound_Theme[1]
critical_roll = cf.Sound_Theme[2]
failure_roll = cf.Sound_Theme[3]

### Windows Starts

main = tk.Tk()
main.geometry(RESOLUTION)
main.title("Game Super Dice")
main.configure(background=cf.Background_Color)
main.clipboard_get

if cf.Config_Window is True:

    cfw = tk.Tk()
    cfw.geometry('300x600')
    cfw.title("Config Window")
    cfw.configure(background=cf.Background_Color)
    cfw.clipboard_get

### Windows Ends

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

Counters_var = tk.IntVar() ### Counters
Modifier_var = tk.IntVar() ### Modifier
Quanities_var = tk.IntVar() ### Quanities
Sides_var = tk.IntVar() ### Sides
Rerolls_var = tk.IntVar() ### Rerolls
Wild_Dice_var = tk.IntVar() ### Wild Dice Varible

class DICE_USED: ### For Dice
    def __init__(self, text):
        self.text = text
    def set(self, text):
        self.text = text

dice_used = DICE_USED("None")

V_INDEX = [Counters_var,Modifier_var,Quanities_var,Sides_var,Rerolls_var,Wild_Dice_var]

### Rollers
def Roll_Dice(quanity, sides, special, printer, amount):
    steps = 0
    a = 0 ## Normal Result
    b = 0 ## Wild Dice
    critical_objective = quanity*sides
    r = quanity
    t = Rerolls_var.get()
    while steps < quanity:
            if steps == 0:
                individual_dice_log.config(state="normal")
                individual_dice_log.insert(tk.INSERT, " {")
                individual_dice_log.config(state="disabled")
            roll = rd.randint(1,sides)
            individual_dice_log.config(state="normal")
            individual_dice_log.insert(tk.INSERT, " ["+str(roll)+"] ")
            individual_dice_log.config(state="disabled")
            #DICE_USED.set(str(quanity)+"D"+str(sides))
            if roll <= t and r > 0:
                roll = rd.randint(1,sides)
            a = a + roll
            steps = steps + 1
    while steps == quanity:
            mod = Modifier_var.get()
            wild_check = Wild_Dice_var.get()
            a = a + mod
            if wild_check == 1:
                b = rd.randint(1,6)
                individual_dice_log.config(state="normal")
                individual_dice_log.insert(tk.INSERT, " ["+str(b)+"W] ")
                individual_dice_log.config(state="disabled")
                #DICE_USED.set(str(quanity)+"D"+str(sides))
                if b > a:
                    a = b
                    Counters_var.set(a)
            else:
                Counters_var.set(a)
            if printer is True:
                if special == 'percent':
                    log.config(state="normal")
                    individual_dice_log.config(state="normal")
                    log.insert(tk.INSERT, " ["+str(a)+"%]")
                    individual_dice_log.insert(tk.INSERT, "% Dice } \n")
                    log.config(state="disabled")
                    individual_dice_log.config(state="disabled")
                    #dice_used = "%"
                    if cf.Sounds is True:
                        sound_result = rd.randint(0,len(roll_sfx_i))
                        ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                        if a == critical_objective:
                            ws.PlaySound(critical_roll[sound_result], ws.SND_ASYNC)
                else:
                    log.config(state="normal")
                    individual_dice_log.config(state="normal")
                    log.insert(tk.INSERT, " ["+str(a)+"] ")
                    individual_dice_log.insert(tk.INSERT, str(quanity)+"D"+str(sides)+"s } \n")
                    log.config(state="disabled")
                    individual_dice_log.config(state="disabled")
                    #DICE_USED.set(str(quanity)+"D"+str(sides))
                    if cf.Sounds is True:
                        sound_result = rd.randint(0,len(roll_sfx_i))
                        ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                        if a == critical_objective:
                            ws.PlaySound(critical_roll[sound_result], ws.SND_ASYNC)
            if cf.Reset_After_Roll is True:
                Modifier_var.set(0)
                Quanities_var.set(0)
                Sides_var.set(0)
                Rerolls_var.set(0)
                Wild_Dice_var.set(0)
            return a
    while quanity == -1 and sides == -1:
            q = Quanities_var.get()
            s = Sides_var.get()
            quanity == q
            sides = s
            if q <= 0 or s <= 0:
                log.config(state="normal")
                log.insert(tk.INSERT, "[No Negative Numbers]")
                log.config(state="disabled")
                #DICE_USED.set(str(quanity)+"D"+str(sides))
                if cf.Sounds is True:
                    sound_result = rd.randint(0,len(roll_sfx_i))
                    ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                    if a == critical_objective:
                            ws.PlaySound(critical_roll[sound_result], ws.SND_ASYNC)
                if cf.Reset_After_Roll is True:
                    Modifier_var.set(0)
                    Quanities_var.set(0)
                    Sides_var.set(0)
                    Rerolls_var.set(0)
                    Wild_Dice_var.set(0)
                return a
            while steps < q and q > 0:
                a = a + rd.randint(1,sides)
                steps = steps + 1
                while steps == q:
                    mod = Modifier_var.get()
                    wild_check = Wild_Dice_var.get()
                    a = a + mod
                    if wild_check == 1:
                        b = rd.randint(1,6)
                        if b > a:
                            a = b
                            Counters_var.set(a)
                    else:
                        Counters_var.set(a)
                    log.config(state="normal")
                    log.insert(tk.INSERT, " ["+str(a)+"] ")
                    log.config(state="disabled")
                    #DICE_USED.set(str(quanity)+"D"+str(sides))
                    if cf.Sounds is True:
                        sound_result = rd.randint(0,len(roll_sfx_i))
                        ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                        if a == critical_objective:
                            ws.PlaySound(critical_roll[sound_result], ws.SND_ASYNC)
                    if cf.Reset_After_Roll is True:
                        Modifier_var.set(0)
                        Quanities_var.set(0)
                        Sides_var.set(0)
                        Rerolls_var.set(0)
                        Wild_Dice_var.set(0)
                    return a

def Determined_Direction():
    steps = 0
    a = 0
    quanity = 1
    while steps < quanity:
            a = a + rd.randint(1,360)
            steps = steps + 1
    while steps == quanity:
            Counters_var.set(a)
            if cf.Direction_Output == 'Degrees':
                log.config(state="normal")
                individual_dice_log.config(state="normal")
                log.insert(tk.INSERT, " ["+str(a)+"] ")
                individual_dice_log.insert(tk.INSERT, " { Directional } \n")
                log.config(state="disabled")
                individual_dice_log.config(state="disabled")
                dice_used = "Directional"
                if cf.Sounds is True:
                    sound_result = rd.randint(0,len(roll_sfx_i))
                    ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                return a
            elif cf.Direction_Output == 'Radians':
                b = (a*mt.pi)/180
                log.config(state="normal")
                individual_dice_log.config(state="normal")
                log.insert(tk.INSERT, " ["+str(round(b,1))+"] ")
                individual_dice_log.insert(tk.INSERT, " { Directional } \n")
                log.config(state="disabled")
                individual_dice_log.config(state="disabled")
                dice_used = "Directional"
                if cf.Sounds is True:
                    sound_result = rd.randint(0,len(roll_sfx_i))
                    ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                return a
            elif cf.Direction_Output == 'Compass':
                compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
                b = (a/45)-1
                log.config(state="normal")
                individual_dice_log.config(state="normal")
                log.insert(tk.INSERT, " ["+compass[int(round(b,0))]+"] ")
                individual_dice_log.insert(tk.INSERT, " { Directional } \n")
                log.config(state="disabled")
                individual_dice_log.config(state="disabled")
                dice_used = "Directional"
                if cf.Sounds is True:
                    sound_result = rd.randint(0,len(roll_sfx_i))
                    ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                return a
            elif cf.Direction_Output == 'Advance_Compass':
                compass = ["N", "NNE", "NE", "NEE", "E", "SEE", "SE", "SSE", "S", "SSW", "SW", "SWW", "W", "NWW", "NW", "NNW"]
                b = (a/22.5)-1
                log.config(state="normal")
                individual_dice_log.config(state="normal")
                log.insert(tk.INSERT, " ["+compass[int(round(b,0))]+"] ")
                individual_dice_log.insert(tk.INSERT, " { Directional } \n")
                log.config(state="disabled")
                individual_dice_log.config(state="disabled")
                dice_used = "Directional"
                if cf.Sounds is True:
                    sound_result = rd.randint(0,len(roll_sfx_i))
                    ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                return a
            elif cf.Direction_Output == 'Simple_Compass':
                compass = ["N", "E", "S", "W"]
                b = (a/90)-1
                log.config(state="normal")
                individual_dice_log.config(state="normal")
                log.insert(tk.INSERT, " ["+compass[int(round(b,0))]+"] ")
                individual_dice_log.insert(tk.INSERT, " { Directional } \n")
                log.config(state="disabled")
                individual_dice_log.config(state="disabled")
                dice_used = "Directional"
                if cf.Sounds is True:
                    sound_result = rd.randint(0,len(roll_sfx_i))
                    ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                return a
            else:
                log.config(state="normal")
                log.insert(tk.INSERT, "[Error, you need the correct direction string. Check config]")
                log.config(state="disabled")
                dice_used = "Directional"
                if cf.Sounds is True:
                    sound_result = rd.randint(0,len(roll_sfx_i))
                    ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
                return a

def Clear_Log():
    log.config(state="normal")
    log.delete('1.0', tk.END)
    log.config(state="disabled")
    individual_dice_log.config(state="normal")
    individual_dice_log.delete('1.0', tk.END)
    individual_dice_log.config(state="disabled")
    if cf.Sounds is True:
        sound_result = rd.randint(0,len(roll_sfx_i))
        ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)

def Modifier(num):
    get = Modifier_var.get()
    b = num + get
    Modifier_var.set(b)
    if cf.Sounds is True:
        sound_result = rd.randint(0,len(change_sfx_i))
        ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
    return b

def Set_Custom_Quanity(num):
    a = Quanities_var.get()
    if a < 0:
        q = 0
        Quanities_var.set(q)
        if cf.Sounds is True:
            sound_result = rd.randint(0,len(change_sfx_i))
            ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
        return q
    else:
        q = num + a
        Quanities_var.set(q)
        if cf.Sounds is True:
            sound_result = rd.randint(0,len(change_sfx_i))
            ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
        return q

def Set_Custom_Sides(num):
    a = Sides_var.get()
    if a < 0:
        s = 0
        Sides_var.set(s)
        if cf.Sounds is True:
            sound_result = rd.randint(0,len(change_sfx_i))
            ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
        return s
    else:
        s = num + a
        Sides_var.set(s)
        if cf.Sounds is True:
            sound_result = rd.randint(0,len(change_sfx_i))
            ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
        return s

def Set_Reroll(num):
    a = Rerolls_var.get()
    if a < 0:
        r = 0
        Rerolls_var.set(r)
        if cf.Sounds is True:
            sound_result = rd.randint(0,len(change_sfx_i))
            ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
        return r
    else:
        r = num + a
        Rerolls_var.set(r)
        if cf.Sounds is True:
            sound_result = rd.randint(0,len(change_sfx_i))
            ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
        return r

def Reset(num, l):
    l[num].set(0)

def wild_change(num):
    if num == 0:
        Wild_Dice_var.set(0)
        if cf.Sounds is True:
            sound_result = rd.randint(0,len(change_sfx_i))
            ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
        return 0
    elif num == 1:
        Wild_Dice_var.set(1)
        if cf.Sounds is True:
            sound_result = rd.randint(0,len(change_sfx_i))
            ws.PlaySound(change_sfx_i[sound_result], ws.SND_ASYNC)
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
        log.insert(tk.INSERT, "\n ["+suite[4]+"] \n")
    else:
        log.insert(tk.INSERT, "\n ["+str(r)+" of "+suite[s]+"] \n")
    log.config(state="disabled")
    if cf.Sounds is True:
        sound_result = rd.randint(0,len(roll_sfx_i))
        ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
    return r

def hit_zone():
    body_parts = ["Skull", "Face", "Right Leg", "Right Arm", "Torso", "Groin", "Left Arm", "Left Leg", "Hand", "Foot", "Neck"]
    r = Roll_Dice(3,6,'none',False)
    if r == 3 or r == 4:
        x = 0
    elif r == 5:
        x = 1
    elif r == 6 or r == 7:
        x = 2
    elif r == 8:
        x = 3
    elif r == 9 or r == 10:
        x = 4
    elif r == 11:
        x = 5
    elif r == 12:
        x = 6
    elif r == 13 or r == 14:
        x = 7
    elif r == 15:
        x = 8
    elif r == 16:
        x = 9
    elif r == 17 or r == 18:
        x = 10
    else:
        x = 4
    result = body_parts[x]
    log.config(state="normal")
    individual_dice_log.config(state="normal")
    log.insert(tk.INSERT, "\n ["+result+"] \n")
    individual_dice_log.insert(tk.INSERT, " } \n")
    log.config(state="disabled")
    individual_dice_log.config(state="disabled")
    if cf.Sounds is True:
        sound_result = rd.randint(0,len(roll_sfx_i))
        ws.PlaySound(roll_sfx_i[sound_result], ws.SND_ASYNC)
    return result

class pic_r:
    def __init__ (self, image):
        self.image = image
    def run(self, checker):
        if checker is True:
            return tk.PhotoImage(file=self.image)
        else:
            return None

def switch_game(lista = cf.Game):
    lister_q = len(lista)
    current_lister_index = cf.Game.index
    result = current_lister_index + 1
    if result > lister_q:
        result = 0
    cf.Game = cf.Game_List[result]

### Main

### Dices
d2b = tk.Button(main, text = ("d2      "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=2,ipadx=120*SCALE,ipady=5*SCALE)
d2b2 = tk.Button(main, text = ("2d2    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=3,ipadx=120*SCALE,ipady=5*SCALE)
d2b3 = tk.Button(main, text = ("3d2    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=4,ipadx=120*SCALE,ipady=5*SCALE)
d2b4 = tk.Button(main, text = ("4d2    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=5,ipadx=120*SCALE,ipady=5*SCALE)
d2b5 = tk.Button(main, text = ("5d2    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=6,ipadx=120*SCALE,ipady=5*SCALE)
d2b6 = tk.Button(main, text = ("6d2    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=7,ipadx=120*SCALE,ipady=5*SCALE)
d2b7 = tk.Button(main, text = ("7d2    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=8,ipadx=120*SCALE,ipady=5*SCALE)
d2b8 = tk.Button(main, text = ("8d2    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=9,ipadx=120*SCALE,ipady=5*SCALE)
d2b9 = tk.Button(main, text = ("9d2    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=10,ipadx=120*SCALE,ipady=5*SCALE)
d2b10 = tk.Button(main, text = ("10d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=11,ipadx=120*SCALE,ipady=5*SCALE)
d2b11 = tk.Button(main, text = ("11d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=12,ipadx=120*SCALE,ipady=5*SCALE)
d2b12 = tk.Button(main, text = ("12d2  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,2,'none',True), fg = "red3", bg = "gray3").grid(row=1,column=13,ipadx=120*SCALE,ipady=5*SCALE)
                   

d4b = tk.Button(main, text = ("d4      "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=2,ipadx=120*SCALE,ipady=5*SCALE)
d4b2 = tk.Button(main, text = ("2d4    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=3,ipadx=120*SCALE,ipady=5*SCALE)
d4b3 = tk.Button(main, text = ("3d4    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=4,ipadx=120*SCALE,ipady=5*SCALE)
d4b4 = tk.Button(main, text = ("4d4    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=5,ipadx=120*SCALE,ipady=5*SCALE)
d4b5 = tk.Button(main, text = ("5d4    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=6,ipadx=120*SCALE,ipady=5*SCALE)
d4b6 = tk.Button(main, text = ("6d4    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=7,ipadx=120*SCALE,ipady=5*SCALE)
d4b7 = tk.Button(main, text = ("7d4    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=8,ipadx=120*SCALE,ipady=5*SCALE)
d4b8 = tk.Button(main, text = ("8d4    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=9,ipadx=120*SCALE,ipady=5*SCALE)
d4b9 = tk.Button(main, text = ("9d4    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=10,ipadx=120*SCALE,ipady=5*SCALE)
d4b10 = tk.Button(main, text = ("10d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=11,ipadx=120*SCALE,ipady=5*SCALE)
d4b11 = tk.Button(main, text = ("11d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=12,ipadx=120*SCALE,ipady=5*SCALE)
d4b12 = tk.Button(main, text = ("12d4  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,4,'none',True), fg = "orange", bg = "gray3").grid(row=2,column=13,ipadx=120*SCALE,ipady=5*SCALE)


d6b = tk.Button(main, text = ("d6      "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=2,ipadx=120*SCALE,ipady=5*SCALE)
d6b2 = tk.Button(main, text = ("2d6    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=3,ipadx=120*SCALE,ipady=5*SCALE)
d6b3 = tk.Button(main, text = ("3d6    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=4,ipadx=120*SCALE,ipady=5*SCALE)
d6b4 = tk.Button(main, text = ("4d6    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=5,ipadx=120*SCALE,ipady=5*SCALE)
d6b5 = tk.Button(main, text = ("5d6    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=6,ipadx=120*SCALE,ipady=5*SCALE)
d6b6 = tk.Button(main, text = ("6d6    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=7,ipadx=120*SCALE,ipady=5*SCALE)
d6b7 = tk.Button(main, text = ("7d6    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=8,ipadx=120*SCALE,ipady=5*SCALE)
d6b8 = tk.Button(main, text = ("8d6    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=9,ipadx=120*SCALE,ipady=5*SCALE)
d6b9 = tk.Button(main, text = ("9d6    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=10,ipadx=120*SCALE,ipady=5*SCALE)
d6b10 = tk.Button(main, text = ("10d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=11,ipadx=120*SCALE,ipady=5*SCALE)
d6b11 = tk.Button(main, text = ("11d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=12,ipadx=120*SCALE,ipady=5*SCALE)
d6b12 = tk.Button(main, text = ("12d6  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,6,'none',True), fg = "yellow3", bg = "gray3").grid(row=3,column=13,ipadx=120*SCALE,ipady=5*SCALE)

d8b = tk.Button(main, text = ("d8      "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=2,ipadx=120*SCALE,ipady=5*SCALE)
d8b2 = tk.Button(main, text = ("2d8    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=3,ipadx=120*SCALE,ipady=5*SCALE)
d8b3 = tk.Button(main, text = ("3d8    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=4,ipadx=120*SCALE,ipady=5*SCALE)
d8b4 = tk.Button(main, text = ("4d8    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=5,ipadx=120*SCALE,ipady=5*SCALE)
d8b5 = tk.Button(main, text = ("5d8    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=6,ipadx=120*SCALE,ipady=5*SCALE)
d8b6 = tk.Button(main, text = ("6d8    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=7,ipadx=120*SCALE,ipady=5*SCALE)
d8b7 = tk.Button(main, text = ("7d8    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=8,ipadx=120*SCALE,ipady=5*SCALE)
d8b8 = tk.Button(main, text = ("8d8    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=9,ipadx=120*SCALE,ipady=5*SCALE)
d8b9 = tk.Button(main, text = ("9d8    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=10,ipadx=120*SCALE,ipady=5*SCALE)
d8b10 = tk.Button(main, text = ("10d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=11,ipadx=120*SCALE,ipady=5*SCALE)
d8b11 = tk.Button(main, text = ("11d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=12,ipadx=120*SCALE,ipady=5*SCALE)
d8b12 = tk.Button(main, text = ("12d8  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,8,'none',True), fg = "OliveDrab2", bg = "gray3").grid(row=4,column=13,ipadx=120*SCALE,ipady=5*SCALE)

d10b = tk.Button(main, text = ("d10    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=2,ipadx=120*SCALE,ipady=5*SCALE)
d10b2 = tk.Button(main, text = ("2d10  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=3,ipadx=120*SCALE,ipady=5*SCALE)
d10b3 = tk.Button(main, text = ("3d10  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=4,ipadx=120*SCALE,ipady=5*SCALE)
d10b4 = tk.Button(main, text = ("4d10  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=5,ipadx=120*SCALE,ipady=5*SCALE)
d10b5 = tk.Button(main, text = ("5d10  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=6,ipadx=120*SCALE,ipady=5*SCALE)
d10b6 = tk.Button(main, text = ("6d10  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=7,ipadx=120*SCALE,ipady=5*SCALE)
d10b7 = tk.Button(main, text = ("7d10  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=8,ipadx=120*SCALE,ipady=5*SCALE)
d10b8 = tk.Button(main, text = ("8d10  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=9,ipadx=120*SCALE,ipady=5*SCALE)
d10b9 = tk.Button(main, text = ("9d10  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=10,ipadx=120*SCALE,ipady=5*SCALE)
d10b10 = tk.Button(main, text = ("10d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=11,ipadx=120*SCALE,ipady=5*SCALE)
d10b11 = tk.Button(main, text = ("11d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=12,ipadx=120*SCALE,ipady=5*SCALE)
d10b12 = tk.Button(main, text = ("12d10"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,10,'none',True), fg = "green3", bg = "gray3").grid(row=5,column=13,ipadx=120*SCALE,ipady=5*SCALE)

d12b = tk.Button(main, text = ("d12    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=2,ipadx=120*SCALE,ipady=5*SCALE)
d12b2 = tk.Button(main, text = ("2d12  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=3,ipadx=120*SCALE,ipady=5*SCALE)
d12b3 = tk.Button(main, text = ("3d12  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=4,ipadx=120*SCALE,ipady=5*SCALE)
d12b4 = tk.Button(main, text = ("4d12  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=5,ipadx=120*SCALE,ipady=5*SCALE)
d12b5 = tk.Button(main, text = ("5d12  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=6,ipadx=120*SCALE,ipady=5*SCALE)
d12b6 = tk.Button(main, text = ("6d12  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=7,ipadx=120*SCALE,ipady=5*SCALE)
d12b7 = tk.Button(main, text = ("7d12  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=8,ipadx=120*SCALE,ipady=5*SCALE)
d12b8 = tk.Button(main, text = ("8d12  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=9,ipadx=120*SCALE,ipady=5*SCALE)
d12b9 = tk.Button(main, text = ("9d12  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=10,ipadx=120*SCALE,ipady=5*SCALE)
d12b10 = tk.Button(main, text = ("10d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=11,ipadx=120*SCALE,ipady=5*SCALE)
d12b11 = tk.Button(main, text = ("11d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=12,ipadx=120*SCALE,ipady=5*SCALE)
d12b12 = tk.Button(main, text = ("12d12"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,12,'none',True), fg = "cyan3", bg = "gray3").grid(row=6,column=13,ipadx=120*SCALE,ipady=5*SCALE)


d20b = tk.Button(main, text = ("d20    "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=2,ipadx=120*SCALE,ipady=5*SCALE)
d20b2 = tk.Button(main, text = ("2d20  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(2,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=3,ipadx=120*SCALE,ipady=5*SCALE)
d20b3 = tk.Button(main, text = ("3d20  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(3,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=4,ipadx=120*SCALE,ipady=5*SCALE)
d20b4 = tk.Button(main, text = ("4d20  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(4,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=5,ipadx=120*SCALE,ipady=5*SCALE)
d20b5 = tk.Button(main, text = ("5d20  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(5,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=6,ipadx=120*SCALE,ipady=5*SCALE)
d20b6 = tk.Button(main, text = ("6d20  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(6,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=7,ipadx=120*SCALE,ipady=5*SCALE)
d20b7 = tk.Button(main, text = ("7d20  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(7,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=8,ipadx=120*SCALE,ipady=5*SCALE)
d20b8 = tk.Button(main, text = ("8d20  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(8,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=9,ipadx=120*SCALE,ipady=5*SCALE)
d20b9 = tk.Button(main, text = ("9d20  "), font = (cf.Base_Font),
            command = lambda : Roll_Dice(9,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=10,ipadx=120*SCALE,ipady=5*SCALE)
d20b10 = tk.Button(main, text = ("10d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(10,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=11,ipadx=120*SCALE,ipady=5*SCALE)
d20b11 = tk.Button(main, text = ("11d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(11,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=12,ipadx=120*SCALE,ipady=5*SCALE)
d20b12 = tk.Button(main, text = ("12d20"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(12,20,'none',True), fg = "blue violet", bg = "gray3").grid(row=7,column=13,ipadx=120*SCALE,ipady=5*SCALE)

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

d1000b = tk.Button(main, text = ("1d1000"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,1000,'none',True), fg = "grey99", bg = "gray3").grid(row=8,column=5,ipadx=120*SCALE,ipady=5*SCALE)

roll = tk.Button(main, text = ("Roll Custom"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(-1,-1,'none',True), fg = "gray99", bg = "gray3").grid(row=8,column=2,ipadx=55*SCALE,ipady=5*SCALE)

if 'GURPS' in cf.Game.lista or 'All' in cf.Game.lista:

    hit_zone_button = tk.Button(main, text = ("Hit Zone"), font = (cf.Base_Font),
                command = lambda : hit_zone(), fg = "grey99", bg = "gray3").grid(row=8,column=10,ipadx=1*SCALE,ipady=5*SCALE)

if 'Savage Worlds' in cf.Game.lista or 'All' in cf.Game.lista:
    
    joker_pic = pic_r('D:/Users/Frank/Desktop/Science/Python Projects/Game Super Dice/joker.png')
    fifty_two_cards_button_with_joker = tk.Button(main, text = ("52 Cards WJ"), font = (cf.Base_Font), image = joker_pic.run(checker = cf.Pictures),
                command = lambda : fifty_two_cards(True), fg = "sky blue", bg = "gray3").grid(row=8,column=9,ipadx=1*SCALE,ipady=5*SCALE)
    
    fifty_two_cards_button = tk.Button(main, text = ("52 Cards"), font = (cf.Base_Font),
                command = lambda : fifty_two_cards(False), fg = "sky blue", bg = "gray3").grid(row=9,column=9,ipadx=39*SCALE,ipady=5*SCALE)

    wild_pic = pic_r('D:/Users/Frank/Desktop/Science/Python Projects/Game Super Dice/Wild_Dice.png')
    wild_on = tk.Button(main, text = ("Wild On"), font = (cf.Base_Font), image = wild_pic.run(checker = cf.Pictures),
                command = lambda : wild_change(1), fg = "yellow1", bg = "gray3").grid(row=8,column=8,ipadx=39*SCALE,ipady=5*SCALE)

    wild_off = tk.Button(main, text = ("Wild Off"), font = (cf.Base_Font),
                command = lambda : wild_change(0), fg = "yellow4", bg = "gray3").grid(row=9,column=8,ipadx=39*SCALE,ipady=5*SCALE)
            
direction = tk.Button(main, text = ("┼"), font = (cf.Base_Font),
            command = lambda : Determined_Direction(), fg = "gray99", bg = "gray3").grid(row=8,column=7,ipadx=39*SCALE,ipady=5*SCALE)

percentage = tk.Button(main, text = ("%"), font = (cf.Base_Font),
            command = lambda : Roll_Dice(1,100,'percent',True), fg = "gray99", bg = "gray3").grid(row=8,column=6,ipadx=120*SCALE,ipady=5*SCALE)

reroll_plus = tk.Button(main, text = ("Reroll +1"), font = (cf.Base_Font),
            command = lambda : Set_Reroll(1), fg = "gray99", bg = "gray3").grid(row=9,column=6,ipadx=1*SCALE,ipady=5*SCALE)
            
reroll_minus = tk.Button(main, text = ("Reroll -1"), font = (cf.Base_Font),
            command = lambda : Set_Reroll(-1), fg = "gray99", bg = "gray3").grid(row=10,column=6,ipadx=1*SCALE,ipady=5*SCALE)

clear_button = tk.Button(main, text = ("Clear Log"), font = (cf.Base_Font),
            command = lambda : Clear_Log(), fg = "gray1", bg = "brown1").grid(row=1,column=0,ipadx=120*SCALE,ipady=5*SCALE)

### Modifier Addition
plus_1 = tk.Button(main, text = ("+1  "), font = (cf.Base_Font),
            command = lambda : Modifier(1), fg = "gray1", bg = "CadetBlue1").grid(row=12,column=2,ipadx=120*SCALE,ipady=5*SCALE)
plus_2 = tk.Button(main, text = ("+2  "), font = (cf.Base_Font),
            command = lambda : Modifier(2), fg = "gray1", bg = "CadetBlue1").grid(row=13,column=2,ipadx=120*SCALE,ipady=5*SCALE)
plus_5 = tk.Button(main, text = ("+5  "), font = (cf.Base_Font),
            command = lambda : Modifier(5), fg = "gray1", bg = "CadetBlue1").grid(row=14,column=2,ipadx=120*SCALE,ipady=5*SCALE)
plus_10 = tk.Button(main, text = ("+10"), font = (cf.Base_Font),
            command = lambda : Modifier(10), fg = "gray1", bg = "CadetBlue1").grid(row=15,column=2,ipadx=120*SCALE,ipady=5*SCALE)

minus_1 = tk.Button(main, text = ("-1  "), font = (cf.Base_Font),
            command = lambda : Modifier(-1), fg = "gray1", bg = "IndianRed1").grid(row=12,column=3,ipadx=120*SCALE,ipady=5*SCALE)
minus_2 = tk.Button(main, text = ("-2  "), font = (cf.Base_Font),
            command = lambda : Modifier(-2), fg = "gray1", bg = "IndianRed1").grid(row=13,column=3,ipadx=120*SCALE,ipady=5*SCALE)
minus_5 = tk.Button(main, text = ("-5  "), font = (cf.Base_Font),
            command = lambda : Modifier(-5), fg = "gray1", bg = "IndianRed1").grid(row=14,column=3,ipadx=120*SCALE,ipady=5*SCALE)
minus_10 = tk.Button(main, text = ("-10"), font = (cf.Base_Font),
            command = lambda : Modifier(-10), fg = "gray1", bg = "IndianRed1").grid(row=15,column=3,ipadx=120*SCALE,ipady=5*SCALE)

### Resets
reset_quanities = tk.Button(main, text = ("Reset Quanities"), font = (cf.Base_Font),
            command = lambda : Reset(2,V_INDEX), fg = "gray99", bg = "gray3").grid(row=12,column=6,ipadx=1*SCALE,ipady=5*SCALE)

reset_sides = tk.Button(main, text = ("Reset Sides"), font = (cf.Base_Font),
            command = lambda : Reset(3,V_INDEX), fg = "gray99", bg = "gray3").grid(row=13,column=6,ipadx=1*SCALE,ipady=5*SCALE)

reset_mod = tk.Button(main, text = ("Reset Modifier"), font = (cf.Base_Font),
            command = lambda : Reset(1,V_INDEX), fg = "Darkorchid4", bg = "gray3").grid(row=14,column=6,ipadx=1*SCALE,ipady=5*SCALE)

reset_reroll = tk.Button(main, text = ("Reset Reroll"), font = (cf.Base_Font),
            command = lambda : Reset(4,V_INDEX), fg = "red3", bg = "gray3").grid(row=15,column=6,ipadx=1*SCALE,ipady=5*SCALE)

reset_all = tk.Button(main, text = ("Reset All"), font = (cf.Base_Font),
            command = lambda : (Reset(1,V_INDEX),Reset(2,V_INDEX),Reset(3,V_INDEX),Reset(4,V_INDEX)),
            fg = "grey99", bg = "grey3").grid(row=16,column=6,ipadx=1*SCALE,ipady=5*SCALE)

### Numbers and Processes
counter = tk.Label(main, textvariable = Counters_var, font = (cf.Counter_Font),
              fg = "gray99", bg = "gray3").grid(row=0,column=14,ipadx=120*SCALE)

modifier = tk.Label(main, textvariable = Modifier_var, font = (cf.Modifier_Font),
              fg = "gray99", bg = "Darkorchid4").grid(row=11,column=0,ipadx=150*SCALE)

modifier_text = tk.Label(main, text = "Modifier", font = ('system'),
              fg = "grey99", bg = "Darkorchid4").grid(row=10,column=0,ipadx=150*SCALE)

custom_quanities_text = tk.Label(main, text = "Quanities", font = ('system'),
              fg = "grey99", bg = "RoyalBlue2").grid(row=6,column=0,ipadx=150*SCALE)

custom_quanities = tk.Label(main, textvariable = Quanities_var, font = (cf.Modifier_Font),
              fg = "gray99", bg = "RoyalBlue2").grid(row=7,column=0,ipadx=1*SCALE)

custom_sides_text = tk.Label(main, text = "Sides", font = ('system'),
              fg = "grey99", bg = "Brown2").grid(row=8,column=0,ipadx=150*SCALE)

custom_sides = tk.Label(main, textvariable = Sides_var, font = (cf.Modifier_Font),
              fg = "gray99", bg = "Brown2").grid(row=9,column=0,ipadx=150*SCALE)

direction_type = tk.Label(main, text = cf.Direction_Output, font = ('system'),
              fg = "gray99", bg = "gray3").grid(row=8,column=14,ipadx=150*SCALE)

game_set = tk.Label(main, text = cf.Game.run(0), font = ('system'),
              fg = "gray99", bg = "gray3").grid(row=9,column=14,ipadx=150*SCALE)

rerolls = tk.Label(main, textvariable = Rerolls_var, font = (cf.Modifier_Font),
              fg = "gray99", bg = "red3").grid(row=13,column=0,ipadx=150*SCALE)

rerolls_text = tk.Label(main, text = "Rerolls (<= x)", font = ('system'),
              fg = "grey99", bg = "Red3").grid(row=12,column=0,ipadx=150*SCALE)

wild_dice_var = tk.Label(main, textvariable = Wild_Dice_var, font = (cf.Modifier_Font),
              fg = "gray99", bg = "orange3").grid(row=15,column=0,ipadx=150*SCALE)

wild_dice_var_text = tk.Label(main, text = "Wild Dice", font = ('system'),
              fg = "grey99", bg = "orange3").grid(row=14,column=0,ipadx=150*SCALE)

#dice_used_button = tk.Label(main, text = dice_used, font = ('system'),
#              fg = "gray99", bg = "gray3").grid(row=1,column=14,ipadx=150*SCALE)

version = tk.Label(main, text = cf.Version, font = ('system'),
              fg = "gray99", bg = "gray3").grid(row=15,column=14,ipadx=150*SCALE)

scrollbar = tk.Scrollbar(main, troughcolor = cf.Scroll_Color_t, highlightcolor = cf.Scroll_Color_hl, bg = cf.Scroll_Color_bg,
                        highlightbackground = cf.Scroll_Color_hlbg)
scrollbar.grid(row = 0, column = 1)
scrollbar_ii = tk.Scrollbar(main, troughcolor = cf.Scroll_Color_t, highlightcolor = cf.Scroll_Color_hl, bg = cf.Scroll_Color_bg,
                        highlightbackground = cf.Scroll_Color_hlbg)
scrollbar_ii.grid(row = 17, column = 1)

'''
mylist = tk.Listbox(main, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(tk.END, "This is line number " + str(line))
mylist.grid(row = 0, column = 15)
'''

log = tk.Text(main, height=7, width=16, bg = "dark slate gray", fg = "SeaGreen1", font = cf.Log_Font, yscrollcommand = scrollbar.set)
log.grid(row=0,column=0,ipadx=120*SCALE)
log.config(state="disabled")

individual_dice_log =tk.Text(main, height=6, width=16, bg = "dark slate gray", fg = "SeaGreen1", font = cf.Individual_Dice_Font, yscrollcommand = scrollbar_ii.set)
individual_dice_log.grid(row=17,column=0,ipadx=120*SCALE)
individual_dice_log.config(state="disabled")

scrollbar.config(command = log.yview)
scrollbar_ii.config(command = individual_dice_log.yview)


### Config Window
if cf.Config_Window is True:

    def Shift_Function(Mega_List = cf.MEGA_LIST, num_i = 0):
        stat = str(cf.FUNCTIONS_LIST[num_i].index)
        x = int(stat) + 1
        if x > len(Mega_List)-1:
            cf.FUNCTIONS_LIST[num_i] = cf.FUNCTIONS_LIST[num_i]
        else:
            cf.FUNCTIONS_LIST[num_i] = cf.FUNCTIONS_LIST[num_i]

    Game_Button = tk.Button(cfw, text = ("Game"), font = (cf.Base_Font),
                command = lambda : switch_game(), fg = "grey99", bg = "gray3").grid(row=0,column=0,ipadx=120*SCALE,ipady=5*SCALE)
    Game_Text = tk.Label(cfw, text = cf.Game.run(0), font = ('system 12'),
                fg = "gray99", bg = "gray3").grid(row=0,column=1,ipadx=150*SCALE)

main.mainloop()

if cf.Config_Window is True:
    cfw.mainloop()