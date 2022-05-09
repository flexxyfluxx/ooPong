""" Anzeige:
Hier wird die Anzeige-Klasse beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import *
from Spieler import *

""" class Anzeige:
Erzeugt die Anzeige, die die Punktzahlen der Spieler anzeigt.
"""
class Anzeige():
    def __init__(self, window, player_1, player_2):
        self.window = window
        self.wndw_bg = window.getBg()
        self.wndw_width = window.getPgWidth()
        self.wndw_height = window.getPgHeight()
        
        self.player_1 = player_1
        self.player_2 = player_2
    
    def show_score(self):
        print("SPIELSTAND: "+str(self.player_1.get_points())+":"+str(self.player_2.get_points())
        )
    
    def show_player_names(self):
        pass