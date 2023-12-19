'''
Ideal use 16:9 or 16:10 ratios smaller than your computer's resolution
such as '1920x1080' or '1280x720'
'''

from tkinter import Scrollbar
import sound_database as sd


#Base_Font = 'Dubai 10'
#Counter_Font = 'Arial 72'
#Modifier_Font = 'Arial 20'
#Log_Font = 'lucida 20 bold italic' ### Default lucida 20 bold italic

class Game_Set(object):
    def __init__(self, lista = [], index = -1):
        self.lista = lista
        self.index = index
    def run(self, num):
        return self.lista[num]

def Res_Check(check, num_i, num_ii):
    if Game == check:
        return num_i
    else:
        return num_ii

No_Game = Game_Set([
    'None',
    'Dubai 10',
    'Arial 72',
    'Arial 20',
    'lucida 20 bold italic',
    "gray10",
    "dark slate gray",
    "slate gray",
    "sea green",
    "dark slate gray",
    "sea green",
    'system 8 bold'], 0)

Dungeons_and_Dragons = Game_Set([
    'Dungeons and Dragons',
    'Dubai 10',
    'Arial 72',
    'Arial 20',
    'lucida 20 bold italic',
    "gray10",
    "dark slate gray",
    "slate gray",
    "sea green",
    "dark slate gray",
    "sea green",
    'system 8 bold'], 1)

GURPS = Game_Set([
    'GURPS',
    'Dubai 10',
    'Arial 72',
    'Arial 20',
    'lucida 20 bold italic',
    "gray10",
    "dark slate gray",
    "slate gray",
    "sea green",
    "dark slate gray",
    "sea green",
    'system 8 bold'], 2)

Savage_Worlds = Game_Set([
    'Savage Worlds',
    'Dubai 10',
    'Arial 72',
    'Arial 20',
    'lucida 20 bold italic',
    "gray10",
    "dark slate gray",
    "slate gray",
    "sea green",
    "dark slate gray",
    "sea green",
    'system 8 bold'], 3)

Neomath = Game_Set([
    'Neomath',
    'Calibri 12',
    'Haettenschweiler 84',
    'Haettenschweiler 36',
    'system 16 bold',
    "gray10",
    "dark slate gray",
    "slate gray",
    "sea green",
    "dark slate gray",
    "sea green",
    'system 8 bold'], 4)

Nintendo = Game_Set([
    'Nintendo',
    'Dubai 10',
    'Arial 72',
    'Arial 20',
    'lucida 20 bold italic',
    'gray10',
    'red4',
    'slate gray',
    'grey95',
    'red4',
    'grey95',
    'system 8 bold'], 5)

All = Game_Set([
    'All',
    'Dubai 10',
    'Arial 72',
    'Arial 20',
    'system 16 bold',
    "gray10",
    "dark slate gray",
    "slate gray",
    "sea green",
    "dark slate gray",
    "sea green",
    'system 8 bold'], 6)

'''
def Font_Check(Games_Lister = Games_List, Font = 'Base_Font', Theme = 0):
    if Font is 'Base_Font':
        Base_Font_Lister = ['Dubai 10','Dubai 10','Dubai 10','Dubai 10']
'''

Game_List = [
    No_Game,
    Dungeons_and_Dragons,
    GURPS,
    Savage_Worlds,
    Neomath,
    Nintendo,
    All
]

MEGA_LIST = [
    Game_List
]

Config_Window = True

### Default is None. Games have specfic dices.
Game = Game_List[4] ### < Functions
Game_Theme = Game_List[4] ### < Graphics
Resolution = '1440x960' #Res_Check(Game_List[4], '960x960', '1440x960') #'1280x960'
Scale = 0.1
### Default 'system 8'
Base_Font = Game_Theme.run(1) ### 1
Counter_Font = Game_Theme.run(2) ### 2
Modifier_Font = Game_Theme.run(3) ### 3
Log_Font = Game_Theme.run(4) ### 4, Default lucida 20 bold italic
Individual_Dice_Font = Game_Theme.run(11)
Reset_After_Roll = False

Sounds = False
Sound_Theme = sd.THEME[0]

Pictures = False
Version = '3.5.1'
Text_Size_Scale = 1
Background_Color = Game_Theme.run(5) ### 5
Scroll_Color_t = Game_Theme.run(6) ### 6
Scroll_Color_hl = Game_Theme.run(7) ### 7
Scroll_Color_bg = Game_Theme.run(8) ### 8
Scroll_Color_hlbg = Game_Theme.run(9) ### 9

Direction_Output = 'Advance_Compass'

FUNCTIONS_LIST = [
    Game,
    Game_Theme
    ]

'''
'Compass' (Directions under a compass)
'Advance_Compass' (With additional, more precise directions)
'Simple_Compass' (Only with N, E, S, W)
'Degress' (In degrees)
'Radians' (In radians)
'''

'''

Games
'None' 0
'Dungeons and Dragons' 1
'GURPS' 2
'Savage Worlds' 3
'All' 99 < It will display the most valid dices

'''
