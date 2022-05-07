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
        
        self.move()
        
        #print(self.get_exit_angle())
        self.setDirection(int(self.get_exit_angle()))
        
    
    def get_exit_angle(self):
        original_angle = self.getDirection()
        
        # 
        
        if ( ( self.getX() <= self.min_x and original_angle < 270 and original_angle > 90 ) \
            or (self.getX() >= self.max_x and ( original_angle  < 90 or original_angle > 270 ) ) ):
            #self.setX(self.min_x)
            return (180 - original_angle) % 360
        
        if ( ( self.getY() <= self.min_y and original_angle < 360 and original_angle > 180 ) \
            or ( self.getY() >= self.max_y and original_angle < 180 ) ):
            #self.setY(self.min_y)
            return (360 - original_angle) % 360
        
        
        if self.getY() >= self.max_y and original_angle < 180:
            #self.setY(self.max_y)
            return (360 - original_angle) % 360
        
        return original_angle
        