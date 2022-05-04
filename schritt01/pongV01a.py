""" V1:
Die Schläger existieren auf einem Feld und bewegen sich auf und ab.
"""

""" Imports: """
import gamegrid as gg
from constants import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können. (Main ist übersichtlicher :D )

# --- Definitionsbereich ---

""" class Schlaeger: 
Erzeugt ein Schläger-Objekt, das sich auf dem Feld auf und ab bewegt.
"""
class Schlaeger(gg.Actor):
    def __init__(self):
        gg.Actor.__init__(self, SPRITE['schlaeger'])
    
    def act(self):
        self.move()
        
        if self.getY() <= 82: # 82, damit der Schläger gerade so den Rahmen berührt, diesen aber nicht überschreitet. (Schläger ist 164px hoch)
            self.setDirection(SOUTH)
        elif self.getY() >= 518: # s.o.
            self.setDirection(NORTH)

def event_key_press(event):
    """
    Hört auf Keypresses und verarbeitet diese.
    """
    key_code = event.getKeyCode()
    if key_code == KEY['w']:
        schlaeger_1.setDirection(NORTH)
    if key_code == KEY['s']:
        schlaeger_1.setDirection(SOUTH)
    if key_code == KEY['arr_up']:
        schlaeger_2.setDirection(NORTH)
    if key_code == KEY['arr_dn']:
        schlaeger_2.setDirection(SOUTH)

# -------- MAIN --------
if __name__ == "__main__":
    gg.makeGameGrid(800, 600, 1, None, None, False, keyPressed = event_key_press)
    
    schlaeger_1, schlaeger_2 = Schlaeger(), Schlaeger()
    gg.addActor(schlaeger_1, gg.Location(50, 300), NORTH)
    gg.addActor(schlaeger_2, gg.Location(750, 300), NORTH)
    
    gg.setSimulationPeriod(33) # entspricht 30tps
    
    gg.show()
    gg.doRun()