""" Schlaeger:
Hier wird die Klasse Schlaeger beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können. (Main ist übersichtlicher :D )

# -------- EINSTELLUNGEN --------
WINDOW_HEIGHT = 129 # Standard: 600. Werte unter 200 werden im Programmablauf auf 200 gestellt.
WINDOW_WIDTH = 5 # Standard: 800. Werte unter 200 werden im Programmablauf auf 200 gestellt.

WINDOW_HEIGHT = 800 if WINDOW_HEIGHT < 200 else WINDOW_HEIGHT
WINDOW_WIDTH = 800 if WINDOW_WIDTH < 200 else WINDOW_WIDTH
# ----- ENDE EINSTELLUNGEN ------

# --- Definitionsbereich ---

""" class Schlaeger: 
Erzeugt ein Schläger-Objekt, das sich auf dem Feld auf und ab bewegt.
"""
class Schlaeger(gg.Actor):
    def __init__(self, key_up, key_dn, max_y = WINDOW_HEIGHT): # Wird kein max_y-Wert gegeben, ist der Standard, dass der untere Rand gerade berührt wird.
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
    """       
    if KEY['w'] in key_codes and gg.isKeyPressed(KEY['w']):
        schlaeger_1.setDirection(NORTH)
        schlaeger_1.set_course(5)
        
    if KEY['s'] in key_codes and gg.isKeyPressed(KEY['s']):
        schlaeger_1.setDirection(SOUTH)
        schlaeger_1.set_course(5)
        
    if KEY['arr_up'] in key_codes and gg.isKeyPressed(KEY['arr_up']):
        schlaeger_2.setDirection(NORTH)
        schlaeger_2.set_course(5)
        
    if KEY['arr_dn'] in key_codes and gg.isKeyPressed(KEY['arr_dn']):
        schlaeger_2.setDirection(SOUTH)
        schlaeger_2.set_course(5)
    #"""
# -------- MAIN --------
if __name__ == "__main__":
    pass