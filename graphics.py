from tkinter import * 
from tkinter.ttk import *

DATABASE = {
  'Wild Dice': PhotoImage(file = r"D:/Users/Frank/Desktop/Science/Python Projects/Game Super Dice/graphics/Wild Dice.png")
}

def get(name):
  if name in DATABASE:
    if DATABASE[name][1] is None:
      print('loading image:', name)
      DATABASE[name][1] = PhotoImage(file=DATABASE[name][0])
    return DATABASE[name][1]
  return None