""" Anzeige:
Hier wird die Anzeige-Klasse beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import *
from Spieler import *
import java.awt.Color as j_Color
import java.awt.Font as j_Font
from main import Cfg

""" class Anzeige:
Erzeugt die Anzeige, die die Punktzahlen der Spieler anzeigt.
"""
class Anzeige():
    def __init__(self, window, player_1, player_2):
        self.window = window
        self.wndw_bg = window.getBg() # you are useless. you serve no purpose. why do you exist? who created you?
        self.wndw_width = window.getPgWidth()
        self.wndw_height = window.getPgHeight()
        
        self.scoreboard = gg.GGTextField(window, gg.Location(self.wndw_width // 2, 32), True)
        self.scoreboard.setTextColor(j_Color.white)
        self.scoreboard.setFont(j_Font("Arial", j_Font.BOLD, 64))
        
        self.player_1 = player_1
        self._p1_plaque = gg.GGTextField(window, player_1.get_name(), gg.Location(64, self.wndw_height - 20), False)
        self._p1_plaque.setTextColor(j_Color.white)
        self._p1_plaque.setFont(j_Font("Arial", j_Font.BOLD, 32))
        
        self.player_2 = player_2
        self._p2_plaque = gg.GGTextField(window, player_2.get_name(), gg.Location(0, 0), False)
        self._p2_plaque.setTextColor(j_Color.white)
        self._p2_plaque.setFont(j_Font("Arial", j_Font.BOLD, 32))
        self._p2_plaque.setLocation(gg.Location(self.wndw_width - self._p2_plaque.getTextWidth() - 64, self.wndw_height - 20))
        
        self.update_scoreboard()
        
        self._vs = gg.GGTextField(window, "VS", gg.Location(0, self.wndw_height - 36), False)
        self._vs.setFont(j_Font("Arial", j_Font.BOLD, 64))
        self._vs.setTextColor(j_Color.white)
        self._vs.setLocation(gg.Location(self.wndw_width // 2 - self._vs.getTextWidth() // 2, self.wndw_height - 36))
    
    def print_score(self):
        print("SPIELSTAND: "+str(self.player_1.get_points())+":"+str(self.player_2.get_points()))
        self.scoreboard.show()
        
    def show_scoreboard(self):
        self.scoreboard.show()
    
    def hide_scoreboard(self):
        self.scoreboard.hide()
    
    def update_scoreboard(self):
        self.scoreboard.setText(str(self.player_1.get_points()) + " : " + str(self.player_2.get_points()))
        self.scoreboard.setLocation(gg.Location(self.wndw_width // 2 - self.scoreboard.getTextWidth() // 2, 32))
    
    def print_player_names(self):
        print("SPIELER 1: "+self.player_1.get_name() \
            + "\nSPIELER 2: "+self.player_2.get_name())
        
    def show_player_names(self):
        self._p1_plaque.show()
        self._p2_plaque.show()
        self._vs.show()
        
    def hide_player_names(self):
        self._p1_plaque.hide()
        self._p2_plaque.hide()
        self._vs.hide()