# In der ersten Version werde ich lediglich 

# Imports:
from gamegrid import GameGrid, Actor
import os

# Definitionsbereich

# Dict mit den relevanten Bildern: (Ich mach's jetzt schon mal ausführlich, damit ich's später nicht muss)
IMG = {
    "schlaeger" : os.path.abspath(".\images\schlaeger_small.jpg"),
    "ball" : os.path.abspath(".\images\ball.jpg"),
}

# Richtungskonstanten:
E = 0
S = 90
W = 180
N = 270

# Schläger-Actorklasse:
class Schlaeger(Actor):
    def __init__(self):
        Actor.__init__(self, IMG
    
    def act():
        self.move()
    
    def move():
        self.setDirection()


# Main-Bereich
if __name__ == "__main__":
    pass