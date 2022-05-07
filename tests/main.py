""" MAIN:
Hier wird der Hauptprogrammablauf beschrieben.
"""

# Imports:
import gamegrid as gg
from Schlaeger import *
from Ball import *
from constants_etc import *
from random import randint
from time import sleep

# ----- DEFINITIONSBEREICH -----
def event_key_press(event, grid):
    """
    Hört auf Keypresses und verarbeitet diese.
    """
    key_codes = grid.getPressedKeyCodes()
    
    if KEY['space'] in key_codes:
        if grid.isRunning():
            grid.doPause()
            grid.setStatusText("Press SPACE to unpause!")
        else:
            grid.doRun()
            grid.setStatusText("Press SPACE to pause!")

# ----- ENDE DEFINITIONSBEREICH -----

# -------- MAIN --------
if __name__ == "__main__":
    show_debug_bar = True
    main_grid = gg.GameGrid(WINDOW_WIDTH, WINDOW_HEIGHT, 1, None, None, show_debug_bar, keyPressed = lambda event: event_key_press(event, main_grid))
    
    schlaeger_1 = Schlaeger(main_grid, KEY['w'], KEY['s'])
    schlaeger_2 = Schlaeger(main_grid, KEY['arr_up'], KEY['arr_dn'])
    the_ball = Ball()
    
    main_grid.addActor(schlaeger_1, gg.Location(50, WINDOW_HEIGHT // 2))
    main_grid.addActor(schlaeger_2, gg.Location(WINDOW_WIDTH - 50, WINDOW_HEIGHT // 2))
    #"""
    main_grid.addActor(the_ball, gg.Location(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), randint(0, 360))
    """
    gg.addActor(the_ball, gg.Location(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 45) # Corner Debug
    #"""

    main_grid.setSimulationPeriod(33) # entspricht ~30tps
    
    main_grid.setTitle("Ponk!")
    main_grid.addStatusBar(20)
    main_grid.setStatusText("Press SPACE to start!")
    main_grid.show()
    
    await_keypress(KEY['space'])
    
    main_grid.setStatusText("Press SPACE to pause!")  
    main_grid.doRun()