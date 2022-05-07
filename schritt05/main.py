""" MAIN:
Hier wird der Hauptprogrammablauf beschrieben.
"""

# Imports:
import gamegrid as gg
from Schlaeger import *
from Ball import *
from constants_etc import *
from random import randint

# ----- DEFINITIONSBEREICH -----
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

def await_keypress(key_code):
    """
    wartet auf den gegebenen Keypress.
    """
    while getKeyCodeWait() != key_code:
        pass
# ----- ENDE DEFINITIONSBEREICH -----

# -------- MAIN --------
if __name__ == "__main__":
    show_debug_bar = True
    gg.makeGameGrid(WINDOW_WIDTH, WINDOW_HEIGHT, 1, None, None, show_debug_bar, keyPressed = event_key_press)
    
    schlaeger_1 = Schlaeger(KEY['w'], KEY['s'])
    schlaeger_2 = Schlaeger(KEY['arr_up'], KEY['arr_dn'])
    the_ball = Ball()
    
    gg.addActor(schlaeger_1, gg.Location(50, WINDOW_HEIGHT // 2))
    gg.addActor(schlaeger_2, gg.Location(WINDOW_WIDTH - 50, WINDOW_HEIGHT // 2))
    #"""
    gg.addActor(the_ball, gg.Location(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), randint(0, 360))
    """
    gg.addActor(the_ball, gg.Location(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 45) # Corner Debug
    #"""

    gg.setSimulationPeriod(33) # entspricht ~30tps
    
    gg.setTitle("Ponk!")
    gg.addStatusBar(20)
    gg.setStatusText("Press SPACE to start!")
    gg.show()
    
    await_keypress(KEY['space'])
    
    gg.setStatusText("Press SPACE to pause!")  
    gg.doRun()