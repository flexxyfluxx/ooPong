""" Ball:
Beschreibt die Ball-Klasse.
"""

""" Imports: """
import gamegrid as gg
from constants_etc import * # Konstanten in ein eigenes Modul verkapselt, um diese universeller verwenden zu können. (Main ist übersichtlicher :D)
from Anzeige import *
from random import randint, choice

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
        self._start_pos = gg.Location((self.min_x + self.max_x // 2), (self.min_y + self.max_y // 2))
        self._anzeige = None
    
    def act(self):
        self.move(BALL_SPEED)
        
        if self.getX() <= self.min_x:
            self._do_goal_things(WEST)
            self.setLocation(self._start_pos)
            self.setDirection(choice(START_DIRECTIONS))
        elif self.getX() >= self.max_x:
            self._do_goal_things(EAST)
            self.setLocation(self._start_pos)
            self.setDirection(choice(START_DIRECTIONS))
            
        
        self.setDirection(self.get_exit_angle())
        #print(self.getDirection())
        
    
    def get_exit_angle(self, paddle=None):
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
            
            # Falls der Originalwinkel bei Nord-Süd-Kollision steil ist (Aufprallwinkel < 70°), springt der Ball stattdessen im 45°-Winkel weg,
            # um das Spiel nicht zu verlangsamen:
            chance = randint(1,2)
            if original_angle in range(70, 90) or original_angle in range(250, 270) and chance == 1:
                return int((original_angle - 45) % 360)
            if original_angle in range(90, 110) or original_angle in range(270, 290) and chance == 1:
                return int((original_angle - 225) % 360)
            
            #self.setY(self.min_y)
            return int(360 - original_angle) # Kein Modulo nötig, da der gegebene und der entstehende Winkel nicht über 360 / unter 0 sein können
        
        # Falls keine Kollision vorhanden: Ursprungsrichtung zurückgeben.
        return int(original_angle)
    
    def _do_goal_things(self, side):
        if not isinstance(self._anzeige, Anzeige):
            print("[ERROR] Dem Ball ist keine Anzeige zugewiesen!")
            return
        
        elif side == WEST:
            self._anzeige.player_1.add_points(1)
            """
            self._anzeige.print_score()
            """
            self._anzeige.update_scoreboard()
            #"""
            
        elif side == EAST:
            self._anzeige.player_2.add_points(1)
            """
            self._anzeige.print_score()
            """
            self._anzeige.update_scoreboard()
            #"""
        
        else:
            print("[ERROR] Keine valide Seite für den Torschuss gegeben.")
            
    def bind_anzeige(self, anzeige):
        self._anzeige = anzeige