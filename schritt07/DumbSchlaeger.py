""" DumbSchlaeger:
Hier wird die DumbSchlaeger-Klasse beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import *

# --- Definitionsbereich ---

""" class DumbSchlaeger: 
Erzeugt einen Hindernis-Schläger, der in der Mitte herumgaukelt und sich einfach nur senkrecht hin und her bewegt.
"""
class DumbSchlaeger(gg.Actor):
    def __init__(self, max_y):
        gg.Actor.__init__(self, SPRITE['schlaeger'])
        
        self.max_y = max_y - 82
        self.min_y = 82
    
    def act(self):
        self.move()
        
        if self.getY() >= self.max_y and not self.getDirection() == NORTH:
            self.setDirection(NORTH)
        elif self.getY() <= self.min_y and not self.getDirection() == SOUTH:
            self.setDirection(SOUTH)