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
    def __init__(self, key_up, key_dn, max_y = WINDOW_HEIGHT): # Wird kein max_y-Wert gegeben, ist der Standard, dass der untere Rand gerade berührt wird.
        gg.Actor.__init__(self, SPRITE['schlaeger'])
        
        self.max_y = max_y
        self.min_y = 0
        
        self.key_up = key_up
        self.key_dn = key_dn
        
        self._last_direction = NORTH
    
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
        """
        Bewegungs-Methode. Hier wird der Schläger bei gedrückter Bewegungstaste bewegt.
        Je nachdem, in welche Richtung der Schläger sich schon bewegt, ändert sich die Abfragereihenfolge.
        Dadurch ist der Richtungswechsel von oben nach unten mechanisch identisch mit dem von unten nach oben,
        da die Tastendrücke seriell abgefragt werden müssen.
        """
        if self._last_direction == NORTH:
            if gg.isKeyPressed(self.key_dn):
                self.setY(self.getY() + PADDLE_SPEED)
                self._last_direction = SOUTH
                
            elif gg.isKeyPressed(self.key_up):
                self.setY(self.getY() - PADDLE_SPEED)
                
        elif self._last_direction == SOUTH:
            if gg.isKeyPressed(self.key_up):
                self.setY(self.getY() - PADDLE_SPEED)
                self._last_direction = NORTH
                
            elif gg.isKeyPressed(self.key_dn):
                self.setY(self.getY() + PADDLE_SPEED)

def event_key_press(event):
    """
    Hört auf Keypresses und verarbeitet diese.
    """
    key_codes = gg.getPressedKeyCodes()
    
    if KEY['space'] in key_codes:
        if gg.isRunning():
            gg.doPause()
            gg.setStatusText("Press SPACE to unpause!")
        else:
            gg.doRun()
            gg.setStatusText("Press SPACE to pause!")
    
# -------- MAIN --------
if __name__ == "__main__":
    pass