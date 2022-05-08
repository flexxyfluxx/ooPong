""" Schlaeger:
Hier wird die Klasse Schlaeger beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import *

# --- Definitionsbereich ---

""" class Schlaeger: 
Erzeugt ein Schläger-Objekt, das sich auf dem Feld auf und ab bewegt.
"""
class Schlaeger(gg.Actor):
    def __init__(self, key_up, key_dn, ball, max_y = WINDOW_HEIGHT): # Wird kein max_y-Wert gegeben, ist der Standard, dass der untere Rand gerade berührt wird.
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
        Je nachdem, in welche Richtung der Schläger sich schon bewegt, ändert sich die Abfragereihenfolge.
        Dadurch ist der Richtungswechsel von oben nach unten mechanisch identisch mit dem von unten nach oben,
        da die Tastendrücke seriell abgefragt werden müssen.
        """
        if gg.isKeyPressed(self.key_up) and gg.isKeyPressed(self.key_dn):
            if self._last_direction == NORTH:
                self.setY(self.getY() + PADDLE_SPEED)
            if self._last_direction == SOUTH:
                self.setY(self.getY() - PADDLE_SPEED)
        
        elif gg.isKeyPressed(self.key_up) and not gg.isKeyPressed(self.key_dn):
            self.setY(self.getY() - PADDLE_SPEED)
            self._last_direction = NORTH
        
        elif gg.isKeyPressed(self.key_dn) and not gg.isKeyPressed(self.key_up):
            self.setY(self.getY() + PADDLE_SPEED)
            self._last_direction = SOUTH
        
        else:
            self._last_direction = None
        """
        if self._last_direction == NORTH:
            if gg.isKeyPressed(self.key_dn) or (gg.isKeyPressed(self.key_dn) and gg.isKeyPressed(self.key_up)):
                self.setY(self.getY() + PADDLE_SPEED)
                self._last_direction = SOUTH
                
            elif gg.isKeyPressed(self.key_up):
                self.setY(self.getY() - PADDLE_SPEED)
                
        elif self._last_direction == SOUTH:
            if gg.isKeyPressed(self.key_up) or (gg.isKeyPressed(self.key_dn) and gg.isKeyPressed(self.key_up)):
                self.setY(self.getY() - PADDLE_SPEED)
                
            elif gg.isKeyPressed(self.key_dn):
                self.setY(self.getY() + PADDLE_SPEED)
                self._last_direction = NORTH
"""
# -------- MAIN --------
if __name__ == "__main__":
    pass