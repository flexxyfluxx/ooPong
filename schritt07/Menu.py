""" Menu:
Hier wird die Menu-Klasse beschrieben.
"""

""" Imports: """
import gamegrid as gg
import javax.swing as jxs
import ConfigParser as cp
from constants_etc import *

""" class Menu:
Erzeugt ein Fenster, in dem man einiges einstellen kann:
- Spielfenstergröße,
- Hindernisse,
- Spielernamen,
- Ball-Startgeschwindigkeit/-beschleunigung,
- Schläger-Geschwindigkeit/-beschleunigung
+more

Von hier aus startet man zudem das Spiel und kann eine Game History einsehen.
"""

class Menu(jxs.JFrame):
    def __init__(self):
        jxs.JFrame.__init__(self)
        
        self._parser = cp.ConfigParser()
        self._key_left_up = None
        self._key_left_dn = None
        self._key_right_up = None
        self._key_right_dn = None
        
        self._create_things()
        self._place_things()
    
    def _create_things(self):
        self._btn_play = jxs.JButton("Play!", actionPerformed = self.play)
        
        self._chkbx_obstacles = jxs.JCheckBox("Enable Obstacles")
        
        self._txtfield_wndwheight = jxs.JTextField()
        
        self._txtfield_wndwwidth = jxs.JTextField()
        
        """
        Keybind Array:
        self._btns_keybinds[SIDE][DIRECTION]
        """
        self._btns_keybinds = [
            [jxs.JButton(), jxs.JButton()],
            [jxs.JButton(), jxs.JButton()]
        ]
        
        self._btn_resetkeybinds = jxs.JButton()
        
    
    def _place_things(self):
        pass
    
    def play(self):
        pass
    
    def push_settings(self):
        # Falls Abschnitt Keybinds nicht vorhanden: rekonstruieren.
        if not self._parser.has_section("Keybinds"):
            self._parser.add_section("Keybinds")
        
        # Keybinds in settings.ini schreiben:
        self._parser.set("Keybinds", "LEFT_UP", self._key_left_up)
        self._parser.set("Keybinds", "LEFT_DN", self._key_left_dn)
        self._parser.set("Keybinds", "RIGHT_UP", self._key_right_up)
        self._parser.set("Keybinds", "RIGHT_DN", self._key_right_dn)
    
    def pull_settings(self):
        self._parser.read("settings.ini")
        
        
            
        
        self._key_left_up = self._parser.getint("Keybinds", "LEFT_UP")
        self._key_left_dn = self._parser.getint("Keybinds", "LEFT_DN")
        self._key_right_up = self._parser.getint("Keybinds", "RIGHT_UP")
        self._key_right_dn = self._parser.getint("Keybinds", "RIGHT_DN")
    
if __name__ == "__main__":
    menu = Menu()