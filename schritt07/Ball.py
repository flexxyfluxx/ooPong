""" Ball:
Beschreibt die Ball-Klasse.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können. (Main ist übersichtlicher :D)
from Anzeige import *
from random import randint, choice
from time import sleep
#from math import tan
from Schlaeger import *

""" class Ball:
Beschreibt einen Ball, der sich bewegt und an den Schlägern abprallt.
"""
class Ball(gg.Actor):
    def __init__(self, min_x = 0, min_y = 0, max_x = config.WINDOW_WIDTH, max_y = config.WINDOW_HEIGHT):
        gg.Actor.__init__(self, SPRITE['ball'])
        # Da der Ball ca. 20x20px groß ist, werden die Minmax-Werte jw. entsprechend um 10 verschoben.
        self.min_x = min_x + 10
        self.max_x = max_x - 10
        self.min_y = min_y + 10
        self.max_y = max_y - 10
        self._start_pos = gg.Location((self.min_x + self.max_x // 2), (self.min_y + self.max_y // 2))
        self._anzeige = None
        self.schlaeger_1 = None
        self.schlaeger_2 = None
        
        self._point = False
        
        self._velocity = 0
    
    def act(self):
        if self._point:
            sleep(0.75)
            self._point = False
        
        self.setDirection(self.get_exit_angle())
        #print(self.getDirection())
        
        """# collision class is obsolete?? o_o
        self._next_x = self.getNextMoveLocation().x
        if self.getX() + ((self.getNextMoveLocation().x - self.getX()) / 5 * config.BALL_SPEED) < self.schlaeger_1.getX():
            self._intercept_factor = abs(self.getX() - 50) / abs(self.getX() - self._next_x)
            self._ball_paddle_intercept = self.getY() - tan((self.getDirection()) % 360) * self._intercept_factor
            print(self._ball_paddle_intercept)
            
            if self.schlaeger_1.getY() + 82 > self._ball_paddle_intercept > self.schlaeger_1.getY() - 82:
                self.setLocation(self.schlaeger_1.getX(), int(self._ball_paddle_intercept))
        
        elif self.getX() + ((self.getNextMoveLocation().x - self.getX()) / 5 * config.BALL_SPEED) > self.schlaeger_2.getX():
            self._intercept_factor = abs(self.getX() - (self.max_x - 50)) / abs(self.getX() - self._next_x)
            self._ball_paddle_intercept = self.getX() + tan((self.getDirection()) % 360) * self._intercept_factor
            print(self._ball_paddle_intercept)
            
            if self.schlaeger_2.getY() + 82 > self._ball_paddle_intercept > self.schlaeger_2.getY() - 82:
                self.setLocation(self.schlaeger_2.getX(), int(self._ball_paddle_intercept))
        """
        self._velocity += 0.02 if self._velocity < 1 else 0
        self.move(int(config.BALL_SPEED * self._velocity))
        
        
        if self.getX() <= self.min_x and not self._point:
            self._do_goal_things(WEST)
            self.setLocation(self._start_pos)
            self.setDirection(choice(START_DIRECTIONS))
            self._point = True
        elif self.getX() >= self.max_x and not self._point:
            self._do_goal_things(EAST)
            self.setLocation(self._start_pos)
            self.setDirection(choice(START_DIRECTIONS))
            self._point = True
        
    
    def get_exit_angle(self):
        original_angle = self.getDirection()
        
        """ nur zu Debug-Zwecken: Da eine Kollision an der Ost-/Westwand einem Tor entspricht, ist keine Kollision nötig.
        # Ost-West-Kollision:
        if ((self.getX() <= self.min_x and original_angle < 270 and original_angle > 90) \
                or (self.getX() >= self.max_x and (original_angle  < 90 or original_angle > 270))):
            #self.setX(self.min_x)
            return int((180 - original_angle) % 360)
        #"""
        
        # Nord-Süd-Kollision:
        if ((self.getY() <= self.min_y and original_angle < 360 and original_angle > 180) \
                or (self.getY() >= self.max_y and original_angle < 180)):
            
            # Falls der Originalwinkel bei Nord-Süd-Kollision steil ist (Aufprallwinkel < 70°),
            # springt der Ball stattdessen im 45°-Winkel weg, um das Spiel zu beschleunigen:
            chance = randint(1,2)
            if original_angle in range(70, 90) or original_angle in range(250, 270) and chance == 1:
                return int((original_angle - 45) % 360)
            
            if original_angle in range(90, 110) or original_angle in range(270, 290) and chance == 1:
                return int((original_angle - 225) % 360)
            
            #self.setY(self.min_y)
            return int(360 - original_angle)
            # Kein Modulo nötig, da der gegebene und der entstehende Winkel nicht über 360 / unter 0 sein können
        
        # Falls keine Kollision vorhanden: Ursprungsrichtung zurückgeben.
        return int(original_angle)
    
    def _do_goal_things(self, side):
        self._velocity = 0
        if not isinstance(self._anzeige, Anzeige):
            print("[ERROR] Dem Ball ist keine Anzeige zugewiesen!")
            return
        
        elif side == WEST:
            self._anzeige.player_2.add_points(1)
            """
            self._anzeige.print_score()
            """
            self._anzeige.update_scoreboard()
            #"""
            
        elif side == EAST:
            self._anzeige.player_1.add_points(1)
            """
            self._anzeige.print_score()
            """
            self._anzeige.update_scoreboard()
            #"""
        
        else:
            print("[ERROR] Keine valide Seite für den Torschuss gegeben.")
        
        for c in range(2):
            self._anzeige.scoreboard.hide()
            sleep(0.25)
            self._anzeige.scoreboard.show()
            sleep(0.25)
        
    def bind_anzeige(self, anzeige):
        self._anzeige = anzeige
    
    def bind_schlaeger(self, schlaeger_1, schlaeger_2):
        if isinstance(schlaeger_1, Schlaeger) and isinstance(schlaeger_2, Schlaeger):
            self.schlaeger_1 = schlaeger_1
            self.schlaeger_2 = schlaeger_2
            return
        print("[ERROR] bind_schlaeger nimmt genau 2 Schlaeger-Objekte (und self)!")