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
    def __init__(self, key_up, key_dn, ball, max_y = config.WINDOW_HEIGHT):
        # Wird kein max_y-Wert gegeben, wird der Randwert des Fensters benutzt.
        gg.Actor.__init__(self, SPRITE['schlaeger'])
        
        self.max_y = max_y - 82
        self.min_y = 82
        
        self.key_up = key_up
        self.key_dn = key_dn
        
        self._ref_direction = None
        self.true_direction = None
        
        self._ball = ball
        
        self.velocity = 0
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
            self.velocity = 1
        elif self.getY() >= self.max_y:
            self.setY(self.max_y)
            self.velocity = 1
    
    
    def move(self):
        """
        Bewegungs-Methode. Hier wird der Schläger bei gedrückter Bewegungstaste bewegt.
        Es wird immer ein Richtungswechsel bevorzugt, wenn beide Tasten gedrückt sind,
        d.h. es sind auch "schlampige" Wechsel möglich, bei denen man die vorherige
        Richtungstaste noch gedrückt hält.
        -> höhere Wechselpräzision
        """
        if self.velocity > config.PADDLE_ACCEL_LIMIT: self.velocity = config.PADDLE_ACCEL_LIMIT
        
        if gg.isKeyPressed(self.key_up) and gg.isKeyPressed(self.key_dn):
            if self._has_momentum:
                    self.velocity = 0
            
            if self._ref_direction == NORTH:
                self.setY(self.getY() + int(config.PADDLE_SPEED / 2 * (1 + self.velocity)))
                self.true_direction = SOUTH
                
            elif self._ref_direction == SOUTH:
                self.setY(self.getY() - int(config.PADDLE_SPEED / 2 * (1 + self.velocity)))
                self.true_direction = NORTH
                
            self.velocity += 0.1 if self.velocity < config.PADDLE_ACCEL_LIMIT else config.PADDLE_ACCEL_LIMIT
            self._has_momentum = False
        
        elif gg.isKeyPressed(self.key_up) and not gg.isKeyPressed(self.key_dn):
            if  self._ref_direction == SOUTH:
                self.velocity = 0
            self.setY(self.getY() - int(config.PADDLE_SPEED / 2 * (1 + self.velocity)))
            self._ref_direction = NORTH
            self.true_direction = NORTH
            self.velocity += 0.1 if self.velocity < config.PADDLE_ACCEL_LIMIT else config.PADDLE_ACCEL_LIMIT
            self._has_momentum = True
        
        elif gg.isKeyPressed(self.key_dn) and not gg.isKeyPressed(self.key_up):
            if  self._ref_direction == NORTH:
                self.velocity = 0
            self.setY(self.getY() + int(config.PADDLE_SPEED / 2 * (1 + self.velocity)))
            self._ref_direction = SOUTH
            self.true_direction = SOUTH
            self.velocity += 0.1 if self.velocity < config.PADDLE_ACCEL_LIMIT else config.PADDLE_ACCEL_LIMIT
            self._has_momentum = True
        
        else:
            # Falls keine Taste gedrückt: Letzte Richtung clearen.
            self._ref_direction = None
            self.true_direction = None
            self._has_momentum = False
            self.velocity = 0