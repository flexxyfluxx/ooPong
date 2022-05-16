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
        
        # Berechne Austrittswinkel mitsamt Modifikationen:
        exit_angle =  int((180 - original_angle) % 360) + randint(-10, 10) + ball.spin
        ball.spin = 0
        
        """
        Wird der Ball angeschnitten (d.h. der Schläger bewegt sich beim Aufschlag),
        bekommt er je nach Geschwindigkeit und Richtung des Schlägers eine Drehung.
        Trifft er dann auf eine Oberfläche, wird diese Drehung aufgebraucht und der
        Austrittswinkel entsprechend modifiziert.
        """
        if (schlaeger.true_direction == NORTH and original_angle % 360 in range(90, 270)) \
                or schlaeger.true_direction == SOUTH and original_angle % 360 not in range(90, 270):
            ball.spin = int(schlaeger.velocity * 10)
            
        elif (schlaeger.true_direction == SOUTH and original_angle % 360 in range(90, 270)) \
                or schlaeger.true_direction == NORTH and original_angle % 360 not in range(90, 270):
            ball.spin = int(-schlaeger.velocity * 10)
        
        """
        Falls der Austrittswinkel weniger als 10° zum Schläger beträgt,
        wird er entsprechend korrigiert, um diese Grenze nicht zu überschreiten.
        """
        if original_angle in range(90, 270) and exit_angle in range(80, 280):
            exit_angle = 80 if abs(exit_angle - 80) < abs(exit_angle - 280) \
                    else 280
            
        elif original_angle not in range(90, 270) and (exit_angle < 100 or exit_angle > 260):
            exit_angle = 100 if abs(exit_angle - 100) < abs(exit_angle - 260) \
                    else 260
        
        ball.setDirection(exit_angle)
        return 20