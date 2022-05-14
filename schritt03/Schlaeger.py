""" Schlaeger:
Hier wird die Klasse Schlaeger beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können. (Main ist übersichtlicher :D )
import main

# --- Definitionsbereich ---

""" class Schlaeger: 
Erzeugt ein Schläger-Objekt, das sich auf dem Feld auf und ab bewegt.
"""
class Schlaeger(gg.Actor):
    def __init__(self, key_up, key_dn, max_y = main.WINDOW_HEIGHT): # Wird kein max_y-Wert gegeben, ist der Standard, dass der untere Rand gerade berührt wird.
        gg.Actor.__init__(self, SPRITE['schlaeger'])
        
        self.max_y = max_y
        self.min_y = 0
        self.setDirection(NORTH)
        
        self.key_up = key_up
        self.key_dn = key_dn
    
    def act(self):
        self.navigate()
        """
        self.move(self.move_dist)
        """
        self.move()
        #"""
    
    def navigate(self):
        if self.getY() <= self.min_y + 82:
            self.setY(self.min_y + 82)
        elif self.getY() >= self.max_y - 82:
            self.setY(self.max_y - 82)
        
    def move(self):
        if gg.isKeyPressed(self.key_up):
            self.setY(self.getY() - 5)
        elif gg.isKeyPressed(self.key_dn):
            self.setY(self.getY() + 5)

