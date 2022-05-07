""" Collision:
Hier wird die Collision-Klasse beschrieben, die den Ball mit dem Schläger kollidieren lassen.
"""

""" class Collider:
Erstellt das Kollisionsobjekt, das Kollisionen zwischen Schläger und Ball verwaltet.
"""
class Collider(GGActorCollisionListener):
    def __init__(self):
        pass
    
    def collide(self, ball, schlaeger):