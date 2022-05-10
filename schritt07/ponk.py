""" MAIN:
Hier wird der Hauptprogrammablauf beschrieben.
"""

""" Imports: """
import gamegrid as gg
from Schlaeger import *
from Ball import *
from Collisions import *
from constants_etc import *
from random import randint, choice
from Anzeige import *
from Spieler import *

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
    show_debug_bar = False
    main_grid = gg.makeGameGrid(WINDOW_WIDTH, WINDOW_HEIGHT, 1, None, None,
                            show_debug_bar, keyPressed = event_key_press)
    
    the_ball = Ball()
    schlaeger_1 = Schlaeger(KEY['w'], KEY['s'], the_ball)
    schlaeger_2 = Schlaeger(KEY['arr_up'], KEY['arr_dn'], the_ball)
    
    player_1 = Spieler(inputString("Name Spieler 1:"))
    player_2 = Spieler(inputString("Name Spieler 2:"))
    
    za_anzeige = Anzeige(main_grid, player_1, player_2)
    za_anzeige.print_player_names()
    
    the_ball.bind_anzeige(za_anzeige)

    location_s1 = gg.Location(50, WINDOW_HEIGHT // 2)
    location_s2 = gg.Location(WINDOW_WIDTH - 50, WINDOW_HEIGHT // 2)
    gg.addActor(schlaeger_1, location_s1)
    gg.addActor(schlaeger_2, location_s2)
    
    location_ball = gg.Location(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    #"""
    gg.addActor(the_ball, location_ball, choice(START_DIRECTIONS))
    """
    # Specific Angle Debug
    gg.addActor(the_ball, location_ball, 80)
    #"""
    
    ball_collider = Collider()
    
    schlaeger_1.addActorCollisionListener(ball_collider)
    schlaeger_2.addActorCollisionListener(ball_collider)
    the_ball.addActorCollisionListener(ball_collider)

    the_ball.addCollisionActor(schlaeger_1)
    the_ball.addCollisionActor(schlaeger_2)

    gg.setSimulationPeriod(16) # entspricht ~60tps
    
    gg.setTitle("Ponk!")
    gg.addStatusBar(20)
    gg.setStatusText("Press SPACE to start!")
    gg.show()
    za_anzeige.show_scoreboard()
    
    await_keypress(KEY['space'])
    
    gg.setStatusText("Press SPACE to pause!")  
    gg.doRun()