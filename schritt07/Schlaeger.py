""" Schlaeger:
Hier wird die Schlaeger-Klasse beschrieben.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import *

# --- Definitionsbereich ---

""" class Schlaeger: 
Erzeugt ein Schläger-Objekt, das sich auf dem Feld auf und ab bewegt.
"""
class Schlaeger(gg.Actor):
    def __init__(self, key_up, key_dn, ball, max_y = WINDOW_HEIGHT):
        # Wird kein max_y-Wert gegeben, wird der Randwert des Fensters benutzt.
        gg.Actor.__init__(self, SPRITE['schlaeger'])
        
        self.max_y = max_y - 82
        self.min_y = 82
        
        self.key_up = key_up
        self.key_dn = key_dn
        
        self._last_direction = None
        
        self._ball = ball
        
        self._accel = 0
        self._recent_turn = False
    
    def act(self):
        self._do_border_things()
        """
        self.setY(self._ball.getY())
        """
        self.move()
        #"""
    
    def _do_border_things(self):
        if self.getY() <= self.min_y:
            self.setY(self.min_y)
            self._accel = 1
        elif self.getY() >= self.max_y:
            self.setY(self.max_y)
            self._accel = 1
    
    def move(self):
        """
        Bewegungs-Methode. Hier wird der Schläger bei gedrückter Bewegungstaste bewegt.
        Es wird immer ein Richtungswechsel bevorzugt, wenn beide Tasten gedrückt sind,
        d.h. es sind auch "schlampige" Wechsel möglich, bei denen man die vorherige
        Richtungstaste noch gedrückt hält.
        -> höhere Wechselpräzision
        """
        if self._accel > PADDLE_ACCEL_LIMIT: self._accel = PADDLE_ACCEL_LIMIT
        
        if gg.isKeyPressed(self.key_up) and gg.isKeyPressed(self.key_dn):
            if self._has_momentum:
                    self._accel = 1
            
            if self._last_direction == NORTH:
                self.setY(self.getY() + int(PADDLE_SPEED * self._accel))
                
            elif self._last_direction == SOUTH:
                self.setY(self.getY() - int(PADDLE_SPEED * self._accel))
                
            self._accel *= 1.1 if self._accel < PADDLE_ACCEL_LIMIT else PADDLE_ACCEL_LIMIT
            self._has_momentum = False
                
        
        elif gg.isKeyPressed(self.key_up) and not gg.isKeyPressed(self.key_dn):
            if  self._last_direction == SOUTH:
                self._accel = 1
            self.setY(self.getY() - int(PADDLE_SPEED * self._accel))
            self._last_direction = NORTH
            self._accel *= 1.1 if self._accel < PADDLE_ACCEL_LIMIT else PADDLE_ACCEL_LIMIT
            self._has_momentum = True
        
        elif gg.isKeyPressed(self.key_dn) and not gg.isKeyPressed(self.key_up):
            if  self._last_direction == NORTH:
                self._accel = 1
            self.setY(self.getY() + int(PADDLE_SPEED * self._accel))
            self._last_direction = SOUTH
            self._accel *= 1.1 if self._accel < PADDLE_ACCEL_LIMIT else PADDLE_ACCEL_LIMIT
            self._has_momentum = True
        
        else:
            # Falls keine Taste gedrückt: Letzte Richtung clearen.
            self._last_direction = None
            self._has_momentum = False
            self._accel = 1
        """
        print(self._accel)
        print(self._has_momentum)
        print("---")
        #"""
        
# -------- MAIN --------
if __name__ == "__main__":
    pass