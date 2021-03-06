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
        
        # y-Kollision
        if abs(schlaeger.getX() - ball.getX()) < 10 \
                and False: # zu Debugzwecken
            exit_angle = int(360 - original_angle)
        
        else:
            exit_angle =  int((180 - original_angle) % 360) + randint(-30, 30)
            
            # x-Kollision
            if original_angle in range(90, 270) and exit_angle in range(80, 280):
                # Ball kann nicht zu flach abspringen.
                exit_angle = 80 if abs(exit_angle - 80) < abs(exit_angle - 280) \
                        else 280
                
            elif original_angle not in range(90, 270) and (exit_angle < 100 or exit_angle > 260):
                exit_angle = 100 if abs(exit_angle - 100) < abs(exit_angle - 260) \
                        else 260
        
        ball.setDirection(exit_angle)
        return 20