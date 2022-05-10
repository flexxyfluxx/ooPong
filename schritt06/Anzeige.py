""" Anzeige:
Hier wird die Anzeige-Klasse beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import *
from Spieler import *
import java.awt.Color as j_Colors
import java.awt.Font as j_Font

""" class Anzeige:
Erzeugt die Anzeige, die die Punktzahlen der Spieler anzeigt.
"""
class Anzeige():
    def __init__(self, window, player_1, player_2):
        self.window = window
        self.wndw_bg = window.getBg()
        self.wndw_width = window.getPgWidth()
        self.wndw_height = window.getPgHeight()
        self.scoreboard = gg.GGTextField(window, "0 : 0", gg.Location(self.wndw_width // 2, 20), True)
        self.scoreboard.setTextColor(j_Colors.white)
        self.scoreboard.setFont(j_Font("Arial", j_Font.BOLD, 48))
        
        self.player_1 = player_1
        self.player_2 = player_2
    
    def print_score(self):
        print("SPIELSTAND: "+str(self.player_1.get_points())+":"+str(self.player_2.get_points()))
        self.scoreboard.show()
        
    def show_scoreboard(self):
        self.scoreboard.show()
    
    def hide_scoreboard(self):
        self.scoreboard.hide()
    
    def update_scoreboard(self):
        self.scoreboard.setText(str(self.player_1.get_points()) + " : " + str(self.player_2.get_points()))
    
    def print_player_names(self):
        print("SPIELER 1: "+self.player_1.get_name() \
        + "\nSPIELER 2: "+self.player_2.get_name())