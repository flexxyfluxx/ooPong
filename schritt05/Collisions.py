""" Collision:
Hier wird die Collision-Klasse beschrieben, die den Ball mit dem Schläger kollidieren lassen.
"""

# Imports:
import gamegrid as gg
from Ball import *
from Schlaeger import *

""" class Collider:
Erstellt das Kollisionsobjekt, das Kollisionen zwischen Schläger und Ball verwaltet.
"""
class Collider(gg.GGActorCollisionListener):
    """
    Kollision:
    Dem Exit-Winkel wird eine zufällige Varianz von +-30° gegeben.
    Dem Ball wird dann dieser variierte Exitwinkel als Richtung gegeben.
    (siehe Methode Ball.get_exit_angle mit collision_type = PADDLE
    """
    def collide(self, ball, schlaeger):
        ball.setDirection(ball.get_exit_angle(PADDLE, schlaeger))
        return 10