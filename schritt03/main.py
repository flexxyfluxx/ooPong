""" MAIN:
Hier wird der Hauptprogrammablauf beschrieben.
"""
# Imports:
import gamegrid as gg
from Schlaeger import *
from constants_etc import *

# -------- EINSTELLUNGEN --------
WINDOW_HEIGHT = 129 # Standard: 600. Werte unter 200 werden im Programmablauf auf 200 gestellt.
WINDOW_WIDTH = 5 # Standard: 800. Werte unter 200 werden im Programmablauf auf 200 gestellt.

WINDOW_HEIGHT = 800 if WINDOW_HEIGHT < 200 else WINDOW_HEIGHT
WINDOW_WIDTH = 800 if WINDOW_WIDTH < 200 else WINDOW_WIDTH
# ----- ENDE EINSTELLUNGEN ------

# DEFINITIONSBEREICH
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
    show_debug_bar = True
    gg.makeGameGrid(WINDOW_WIDTH, WINDOW_HEIGHT, 1, None, None, show_debug_bar, keyPressed = event_key_press)
    
    schlaeger_1 = Schlaeger(KEY['w'], KEY['s'])
    schlaeger_2 = Schlaeger(KEY['arr_up'], KEY['arr_dn'])
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