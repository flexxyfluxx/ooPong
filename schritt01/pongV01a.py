# In der ersten Version werde ich lediglich 

# Imports:
from gamegrid import GameGrid, Actor
from os.path import abspath # oh nyo the namespace OwO~ onwy impowt whats neccessawy~~ rawr :3

# Definitionsbereich

# Dict mit den Paths zu den relevanten Bildern: (Ich mach's jetzt schon mal ausführlich, damit ich's später nicht muss)
SPRITE = {
    "schlaeger" : abspath(".\images\schlaeger_small.jpg"),
    "ball" : abspath(".\images\ball.jpg")
}

# Richtungskonstanten:
E = 0
S = 90
W = 180
N = 270

# Schläger-Actorklasse:
class Schlaeger(Actor):
    def __init__(self):
        Actor.__init__(self, SPRITE['schlaeger'])
    
    def act():
        pass
    
    def move():
        pass


# Main-Bereich
if __name__ == "__main__":
    pass