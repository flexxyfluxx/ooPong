# In der ersten Version werde ich lediglich 

# Imports:
import gamegrid as gg
from constants import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können.

# --- Definitionsbereich ---

# class Schlaeger:
class Schlaeger(gg.Actor):
    def __init__(self):
        gg.Actor.__init__(self, SPRITE['schlaeger'])
    
    def act(self):
        self.move()
        
        if self.getY() <= 80:
            self.setDirection(SOUTH)
        elif self.getY() >= 520:
            self.setDirection(NORTH)


# -------- MAIN --------
if __name__ == "__main__":
    gg.makeGameGrid(800, 600, 1, None, None, False)
    
    schlaeger_1, schlaeger_2 = Schlaeger(), Schlaeger()
    gg.addActor(schlaeger_1, gg.Location(50, 300), NORTH)
    gg.addActor(schlaeger_2, gg.Location(750, 300), NORTH)

    gg.setSimulationPeriod(33) # entspricht 30tps
    
    gg.show()
    while True:
        if pass:
            break()
    gg.doRun()