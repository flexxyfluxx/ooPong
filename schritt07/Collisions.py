""" Collision:
Hier wird die Collision-Klasse beschrieben, die den Ball mit dem Schläger kollidieren lassen.
"""

""" Imports: """
import gamegrid as gg
from Ball import *
from Schlaeger import *
from random import randint

""" class Collider:
Erstellt das Kollisionsobjekt, das Kollisionen zwischen Schläger und Ball verwaltet.
"""
class Collider(gg.GGActorCollisionListener):
    """
    Kollision:
    Dem Ausgangswinkel wird nach dessen Berechnung eine zufällige Varianz von +-30° gegeben.
    Dem Ball wird dann dieser variierte Exitwinkel als Richtung gegeben.
    """
    def collide(self, ball, schlaeger):
        original_angle = ball.getDirection()
        
        exit_angle =  int((180 - original_angle) % 360) + randint(-10, 10) + ball.spin
        ball.spin = 0
        if schlaeger.true_direction == NORTH:
            ball.spin = int(-schlaeger.velocity * 10)
        elif schlaeger.true_direction == SOUTH:
            ball.spin = int(schlaeger.velocity * 10)
        
        
        if original_angle in range(90, 270) and exit_angle in range(80, 280):
            # Ball kann nicht zu flach abspringen.
            exit_angle = 80 if abs(exit_angle - 80) < abs(exit_angle - 280) \
                    else 280
            
        elif original_angle not in range(90, 270) and (exit_angle < 100 or exit_angle > 260):
            exit_angle = 100 if abs(exit_angle - 100) < abs(exit_angle - 260) \
                    else 260
        
        ball.setDirection(exit_angle)
        return 20