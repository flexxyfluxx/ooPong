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
from DumbSchlaeger import *

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

def play_game(show_debug_bar, obstacles = False):
    main_grid = gg.makeGameGrid(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, 1, None, None,
                                        show_debug_bar, keyPressed = event_key_press)
    
    the_ball = Ball()
    schlaeger_1 = Schlaeger(KEY['w'], KEY['s'], the_ball)
    schlaeger_2 = Schlaeger(KEY['arr_up'], KEY['arr_dn'], the_ball)
    if obstacles:
        obstacle_1 = DumbSchlaeger(config.WINDOW_HEIGHT)
        obstacle_2 = DumbSchlaeger(config.WINDOW_HEIGHT)
        gg.addActor(obstacle_1, gg.Location(2 * config.WINDOW_WIDTH // 5, config.WINDOW_HEIGHT // 2), NORTH)
        gg.addActor(obstacle_2, gg.Location(3 * config.WINDOW_WIDTH // 5, config.WINDOW_HEIGHT // 2), SOUTH)
    
    p1_name = inputString("Name Spieler 1: (Weniger als 24 Zeichen!)")
    while len(p1_name) > 24:
        p1_name = inputString("Name Spieler 1: (Weniger als 24 Zeichen!)")
    
    p2_name = inputString("Name Spieler 2: (Weniger als 24 Zeichen!)")
    while len(p2_name) > 24:
        p2_name = inputString("Name Spieler 2: (Weniger als 24 Zeichen!)")
    
    player_1 = Spieler(p1_name)
    player_2 = Spieler(p2_name)
    
    the_anzeige = Anzeige(main_grid, player_1, player_2)
    
    the_ball.bind_anzeige(the_anzeige)
    the_ball.bind_schlaeger(schlaeger_1, schlaeger_2)

    location_s1 = gg.Location(50, config.WINDOW_HEIGHT // 2)
    location_s2 = gg.Location(config.WINDOW_WIDTH - 50, config.WINDOW_HEIGHT // 2)
    gg.addActor(schlaeger_1, location_s1)
    gg.addActor(schlaeger_2, location_s2)
    
    location_ball = gg.Location(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2)
    #"""
    gg.addActor(the_ball, location_ball, choice(START_DIRECTIONS))
    """
    # Specific Angle Debug
    gg.addActor(the_ball, location_ball, 0)
    #"""
    
    ball_collider = Collider()
    
    schlaeger_1.addActorCollisionListener(ball_collider)
    schlaeger_2.addActorCollisionListener(ball_collider)
    
    the_ball.addActorCollisionListener(ball_collider)
    
    the_ball.addCollisionActor(schlaeger_1)
    the_ball.addCollisionActor(schlaeger_2)
    
    if obstacles:
        obstacle_1.addActorCollisionListener(ball_collider)
        obstacle_2.addActorCollisionListener(ball_collider)
        the_ball.addCollisionActor(obstacle_1)
        the_ball.addCollisionActor(obstacle_2)

    gg.setSimulationPeriod(10)
    
    gg.setTitle("Ponk!")
    gg.addStatusBar(20)
    gg.setStatusText("Press SPACE to start!")
    gg.show()
    the_anzeige.show_scoreboard()
    #"""
    the_anzeige.show_player_names()
    """
    the_anzeige.print_player_names()
    #"""
    
    gg.setStatusText("Press SPACE to pause!")
# ----- ENDE DEFINITIONSBEREICH -----

# -------- MAIN --------
if __name__ == "__main__":
    play_game(True, True)
"""
if __name__ == "ponk":
    play_game(False, config.get_obstacle_state())
#"""