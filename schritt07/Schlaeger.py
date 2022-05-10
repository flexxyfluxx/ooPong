""" Schlaeger:
Hier wird die Schlaeger-Klasse beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import *

# --- Definitionsbereich ---

""" class Schlaeger: 
Erzeugt ein Schläger-Objekt, das sich auf dem Feld auf und ab bewegt.
"""
class Schlaeger(gg.Actor):
    def __init__(self, key_up, key_dn, ball, max_y = WINDOW_HEIGHT):
        # Wird kein max_y-Wert gegeben, wird der Randwert des Fensters benutzt.
        gg.Actor.__init__(self, SPRITE['schlaeger'])
        
        self.max_y = max_y
        self.min_y = 0
        
        self.key_up = key_up
        self.key_dn = key_dn
        
        self._last_direction = None
        
        self._ball = ball
    
    def act(self):
        self._do_border_things()
        """
        self.setY(self._ball.getY())
        """
        self.move()
        #"""
    
    def _do_border_things(self):
        if self.getY() <= self.min_y + 82:
            self.setY(self.min_y + 82)
        elif self.getY() >= self.max_y - 82:
            self.setY(self.max_y - 82)
    
    def move(self):
        """
        Bewegungs-Methode. Hier wird der Schläger bei gedrückter Bewegungstaste bewegt.
        Es wird immer ein Richtungswechsel bevorzugt, wenn beide Tasten gedrückt sind,
        d.h. es sind auch "schlampige" Wechsel möglich, bei denen man die vorherige
        Richtungstaste noch gedrückt hält.
        -> höhere Wechselpräzision
        """
        if gg.isKeyPressed(self.key_up) and gg.isKeyPressed(self.key_dn):
            if self._last_direction == NORTH:
                self.setY(self.getY() + PADDLE_SPEED)
            elif self._last_direction == SOUTH:
                self.setY(self.getY() - PADDLE_SPEED)
        
        elif gg.isKeyPressed(self.key_up) and not gg.isKeyPressed(self.key_dn):
            self.setY(self.getY() - PADDLE_SPEED)
            self._last_direction = NORTH
        
        elif gg.isKeyPressed(self.key_dn) and not gg.isKeyPressed(self.key_up):
            self.setY(self.getY() + PADDLE_SPEED)
            self._last_direction = SOUTH
        
        else:
            # Falls keine Taste gedrückt: Letzte Richtung clearen.
            self._last_direction = None
        
# -------- MAIN --------
if __name__ == "__main__":
    pass