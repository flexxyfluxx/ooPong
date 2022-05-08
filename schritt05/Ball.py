""" Ball:
Beschreibt die Klasse Ball.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können. (Main ist übersichtlicher :D)
from random import randint

""" class Ball:
Beschreibt einen Ball, der sich bewegt und an den Schlägern abprallt.
"""
class Ball(gg.Actor):
    def __init__(self, min_x = 0, min_y = 0, max_x = WINDOW_WIDTH, max_y = WINDOW_HEIGHT):
        gg.Actor.__init__(self, SPRITE['ball'])
        
        # Da der Ball ca. 20x20px groß ist, werden die Minmax-Werte jw. entsprechend um 10 verschoben.
        self.min_x = min_x + 10
        self.max_x = max_x - 10
        self.min_y = min_y + 10
        self.max_y = max_y - 10
    
    def act(self):
        
        self.move(BALL_SPEED)
        
        #print(self.get_exit_angle())
        self.setDirection(self.get_exit_angle())
        
    
    def get_exit_angle(self, collision_type=BORDER, paddle=None):
        original_angle = self.getDirection()
        
        # Rand-Kollision:
        if collision_type is BORDER:
            # Ost-West-Kollision:
            if ((self.getX() <= self.min_x and original_angle < 270 and original_angle > 90) \
                    or (self.getX() >= self.max_x and (original_angle  < 90 or original_angle > 270))):
                #self.setX(self.min_x)
                return int((180 - original_angle) % 360)
            
            # Nord-Süd-Kollision:
            if ((self.getY() <= self.min_y and original_angle < 360 and original_angle > 180 ) \
                    or (self.getY() >= self.max_y and original_angle < 180)):
                #self.setY(self.min_y)
                return int(360 - original_angle) # Kein Modulo nötig, da der gegebene und der entstehende Winkel nicht über 360 / unter 0 sein können
            
            # Falls keine Kollision vorhanden: Ursprungsrichtung zurückgeben.
            return int(original_angle)
        
        # Schläger-Kollision:
        elif collision_type is PADDLE:
            if abs(paddle.getX() - self.getX()) < 10: # y-Kollision
                return int(360 - original_angle)
            
            exit_angle =  int((180 - original_angle) % 360) + randint(-30, 30)
            # x-Kollision
            if original_angle in range(90, 270) and exit_angle in range(80, 280):
                return 80 if abs(exit_angle - 80) < abs(exit_angle - 280) \
                else 280
                
            if (original_angle not in range(90, 270)) and (exit_angle < 100 or exit_angle > 260):
                return 100 if abs(exit_angle - 100) < abs(exit_angle - 260) \
                else 260
            
            return exit_angle





