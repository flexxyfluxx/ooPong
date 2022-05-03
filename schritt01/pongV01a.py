# In der ersten Version werde ich lediglich 

# Imports:
from gamegrid import GameGrid, Actor
from constants import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können.

# --- Definitionsbereich ---

# Keypress-Handler:
def on_key_pressed(event):
    

# class Schlaeger:
class Schlaeger(Actor):
    def __init__(self):
        Actor.__init__(self, SPRITE['schlaeger'])
    
    def act(self, key_in = None):
        pass
        
    
    def move(self, direction, dist):
        pass


# -------- MAIN --------
if __name__ == "__main__":
    makeGameGrid(800,600,1,None,"sprites/lane.gif", False, keyPressed = onKeyPressed, keyReleased = onKeyReleased)
    
    schlaeger_1 = Schlaeger(
    
    
    
    
    
    setSimulationPeriod(50) # entspricht etwa 20tps