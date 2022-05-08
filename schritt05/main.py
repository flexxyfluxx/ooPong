""" MAIN:
Hier wird der Hauptprogrammablauf beschrieben.
"""

# Imports:
import gamegrid as gg
from Schlaeger import *
from Ball import *
from Collisions import *
from constants_etc import *
from random import randint, choice

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
    gg.makeGameGrid(
        WINDOW_WIDTH, WINDOW_HEIGHT, 1, None, None,
        show_debug_bar, keyPressed = event_key_press
    )
    
    the_ball = Ball()
    schlaeger_1 = Schlaeger(KEY['w'], KEY['s'], the_ball)
    schlaeger_2 = Schlaeger(KEY['arr_up'], KEY['arr_dn'], the_ball)
    
    location_s1 = gg.Location(50, WINDOW_HEIGHT // 2)
    location_s2 = gg.Location(WINDOW_WIDTH - 50, WINDOW_HEIGHT // 2)
    gg.addActor(schlaeger_1, location_s1)
    gg.addActor(schlaeger_2, location_s2)
    
    location_ball = gg.Location(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    #"""
    gg.addActor(the_ball, location_ball, choice(START_DIRECTIONS))
    """
    # Corner Debug
    gg.addActor(the_ball, location_ball, 0)
    #"""
    
    ball_collider = Collider()
    schlaeger_1.addActorCollisionListener(ball_collider)
    schlaeger_2.addActorCollisionListener(ball_collider)
    the_ball.addActorCollisionListener(ball_collider)

    the_ball.addCollisionActor(schlaeger_1)
    the_ball.addCollisionActor(schlaeger_2)

    gg.setSimulationPeriod(8) # entspricht ~120tps
    
    gg.setTitle("Ponk!")
    gg.addStatusBar(20)
    gg.setStatusText("Press SPACE to start!")
    gg.show()
    
    await_keypress(KEY['space'])
    
    gg.setStatusText("Press SPACE to pause!")  
    gg.doRun()