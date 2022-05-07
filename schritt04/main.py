""" MAIN:
Hier wird der Hauptprogrammablauf beschrieben.
"""

# Imports:
import gamegrid as gg
from Schlaeger import *
from Ball import *
from constants_etc import *
from random import randint

# ----- FUNKTIONEN -----
def await_keypress(key_code):
    while getKeyCodeWait() != key_code:
        pass
    
""" BONUS:
# Bullshit rekursive python3.8+ - Variante: (rip assignment expression)
def get_start_direction():
    return direction if (direction := randint(0, 359)) in range(0, 60) \
                                        or direction in range(120, 240) \
                                        or direction in range(300, 359) \
        else get_start_direction()
"""

# ----- ENDE FUNKTIONEN -----

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
    gg.addActor(the_ball, gg.Location(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), choice(START_DIRECTIONS))
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