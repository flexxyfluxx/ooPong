""" MAIN:
Hier wird der Hauptprogrammablauf beschrieben.
"""
# Imports:
import gamegrid as gg
from Schlaeger import *
from constants_etc import *

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