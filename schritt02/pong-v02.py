""" V2:
Die Größe des Fensters ist variabel;
das Fenster hat einen Titel;
das Fenster hat eine optionale Debug-Bar;
das Fenster hat eine Status Bar mit Text;
das "Spiel" wartet auf Leertasten-Input bevor es beginnt.
"""

""" Imports: """
import gamegrid as gg
from constants import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können. (Main ist übersichtlicher :D )
from time import sleep

# -------- EINSTELLUNGEN --------
WINDOW_HEIGHT = 720 # Standard: 600. Werte unter 200 werden im Programmablauf auf 200 gestellt.
WINDOW_WIDTH = 720 # Standard: 800. Werte unter 200 werden im Programmablauf auf 200 gestellt.
# ----- ENDE EINSTELLUNGEN ------

# --- Definitionsbereich ---

""" class Schlaeger: 
Erzeugt ein Schläger-Objekt, das sich auf dem Feld auf und ab bewegt.
"""
class Schlaeger(gg.Actor):
    def __init__(self, max_y = WINDOW_HEIGHT): # Wird kein max_y-Wert gegeben, ist der Standard, dass der untere Rand gerade berührt wird.
        gg.Actor.__init__(self, SPRITE['schlaeger'])
        
        self.max_y = max_y
        self.min_y = 0
        self.move_dist = 0
    
    def act(self):
        #"""
        self.move(self.move_dist)
        """
        self.move()
        #"""
        
        if self.getY() <= self.min_y + 82: # 82, damit der Schläger gerade so den Rahmen berührt, diesen aber nicht überschreitet. (Schläger ist 164px hoch)
            self.setDirection(SOUTH)
        elif self.getY() >= self.max_y - 82: # s.o.
            self.setDirection(NORTH)
    
    def set_move_speed(self, dist):
        self.move_dist = dist

def await_keypress(key_code):
    while True:
        if gg.isKeyPressed(key_code):
            return

def event_key_press(event):
    """
    Hört auf Keypresses und verarbeitet diese.
    """
    key_code = event.getKeyCode()
    
    if key_code == KEY['space']:
        if gg.isRunning():
            gg.doPause()
            gg.setStatusText("Press SPACE to unpause!")
        else:
            gg.doRun()
            gg.setStatusText("Press SPACE to pause!")
            
    if key_code == KEY['w']:
        schlaeger_1.setDirection(NORTH)
        schlaeger_1.set_move_speed(5)
        
    if key_code == KEY['s']:
        schlaeger_1.setDirection(SOUTH)
        schlaeger_1.set_move_speed(5)
        
    if key_code == KEY['arr_up']:
        schlaeger_2.setDirection(NORTH)
        schlaeger_2.set_move_speed(5)
        
    if key_code == KEY['arr_dn']:
        schlaeger_2.setDirection(SOUTH)
        schlaeger_2.set_move_speed(5)

def event_key_release(event):
    """
    Hört auf Key-Released's und verarbeitet diese.
    """
    if not gg.isKeyPressed(KEY['w']) and not gg.isKeyPressed(KEY['w']):
        schlaeger_1.set_move_speed(0)
    if not gg.isKeyPressed(KEY['arr_up']) and not gg.isKeyPressed(KEY['arr_dn']):
        schlaeger_2.set_move_speed(0)
        

# -------- MAIN --------
if __name__ == "__main__":
    show_debug_bar = True
    gg.makeGameGrid(WINDOW_WIDTH, WINDOW_HEIGHT, 1, None, None, show_debug_bar, keyPressed = event_key_press, keyReleased = event_key_release)
    
    schlaeger_1, schlaeger_2 = Schlaeger(), Schlaeger()
    gg.addActor(schlaeger_1, gg.Location(50, WINDOW_HEIGHT // 2))
    gg.addActor(schlaeger_2, gg.Location(WINDOW_WIDTH - 50, WINDOW_HEIGHT // 2))

    gg.setSimulationPeriod(33) # entspricht ~30tps
    
    gg.setTitle("Ponk!")
    gg.addStatusBar(20)
    gg.setStatusText("Press SPACE to start!")
    gg.show()
    
    await_keypress(KEY['space'])
    
    gg.setStatusText("Press SPACE to pause!")
    gg.doRun()
    gg.doRun()