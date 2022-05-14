""" Universal Constants Module:
Enthält die ganzen Dicts und so.
Hier werden außerdem die Settings aus der INI geparsed
und Konstanten zugewiesen.
"""

""" Imports: """
from os.path import abspath # oh nyo the namespace OwO~ onwy impowt whats neccessawy~~ rawr :3
from gamegrid import getKeyCodeWait
import ConfigParser as cp

# ----- SETTINGS VON INI LADEN -----

class Cfg(): # Dataclass mit den Settings aus der INI.
    def __init__(self):
        self.parser = cp.ConfigParser()
        self.parser.read("settings.ini")
        
        self.WINDOW_HEIGHT = self.parser.getint('WindowDimensions', 'WINDOW_HEIGHT')
        self.WINDOW_HEIGHT = 200 if self.WINDOW_HEIGHT < 200 else self.WINDOW_HEIGHT
        
        self.WINDOW_WIDTH = self.parser.getint('WindowDimensions', 'WINDOW_WIDTH')
        self.WINDOW_WIDTH = 200 if self.WINDOW_WIDTH < 200 else self.WINDOW_WIDTH
        
        self.PADDLE_SPEED = self.parser.getint('GameSettings', 'PADDLE_SPEED')
        self.PADDLE_ACCEL_LIMIT = self.parser.getfloat('GameSettings', 'PADDLE_ACCEL_LIMIT')
        self.BALL_SPEED = self.parser.getint('GameSettings', 'BALL_SPEED')
        self.OBSTACLES = self.parser.getboolean('GameSettings', 'OBSTACLES')
        
        self.KEY_LEFT_UP =  self.parser.getint('Keybinds', 'LEFT_UP') if self.parser.has_option('Keybinds', 'LEFT_UP') \
                        else self.parser.getint('DefaultKeybinds', 'LEFT_UP')
        self.KEY_LEFT_DN = self.parser.getint('Keybinds', 'LEFT_DN') if self.parser.has_option('Keybinds', 'LEFT_DN') \
                        else self.parser.getint('DefaultKeybinds', 'LEFT_DN')
        self.KEY_RIGHT_UP = self.parser.getint('Keybinds', 'RIGHT_UP') if self.parser.has_option('Keybinds', 'RIGHT_UP') \
                        else self.parser.getint('DefaultKeybinds', 'RIGHT_UP')
        self.KEY_RIGHT_DN = self.parser.getint('Keybinds', 'RIGHT_DN') if self.parser.has_option('Keybinds', 'RIGHT_DN') \
                        else self.parser.getint('DefaultKeybinds', 'RIGHT_DN')
    
    def write_wndw_height(self, new):
        if not isinstance(new, int):
            print("[error] Cfg.write_wndw_height: Non-Int value given! Naughty, naughty!")
            return
        
        self.WINDOW_HEIGHT = new
        self.parser.set('WindowDimensions', 'WINDOW_HEIGHT', new)
    
    def get_wndw_height(self):
        return self.WINDOW_HEIGHT
        
    def write_wndw_width(self, new):
        if not isinstance(new, int):
            print("[ERROR] Cfg.write_wndw_width: Non-Int value given! Naughty, naughty!")
            return
        
        self.WINDOW_WIDTH = new
        self.parser.set('WindowDimensions', 'WINDOW_WIDTH', new)
    
    def get_wndw_width(self):
        return self.WINDOW_WIDTH
    
    def write_ball_speed(self, new):
        if not isinstance(new, int):
            print("[ERROR] Cfg.write_ball_speed: Non-Int value given! Naughty, naughty!")
            return
        
        self.BALL_SPEED = new
        self.parser.set('GameSettings', 'BALL_SPEED', new)
    
    def get_ball_speed(self):
        return self.BALL_SPEED
    
    def write_obstacles(self, new):
        if not isinstance(new, bool):
            print("[ERROR] Cfg.write_obstacles: Non-Bool value given! Naughty, naughty!")
            return
        
        self.OBSTACLES = new
        self.parser.set('GameSettings', 'OBSTACLES', 1 if new else 0)
    
    def get_obstacle_state(self):
        return self.OBSTACLES

    def write_key_left_up(self, new):
        if not isinstance(new, int):
            print("[ERROR] Cfg.write_key_left_up: Non-Int value given! Naughty, naughty!")
            return
        
        self.KEY_LEFT_UP = new
        self.parser.set('Keybinds', 'LEFT_UP', new)
    
    def get_key_left_up(self):
        return self.KEY_LEFT_UP
    
    def write_key_left_dn(self, new):
        if not isinstance(new, int):
            print("[ERROR] Cfg.write_key_left_dn: Non-Int value given! Naughty, naughty!")
            return
        
        self.KEY_LEFT_DN = new
        self.parser.set('Keybinds', 'LEFT_DN', new)
    
    def get_key_left_dn(self):
        return self.KEY_LEFT_DN
    
    def write_key_right_up(self, new):
        if not isinstance(new, int):
            print("[ERROR] Cfg.write_key_right_up: Non-Int value given! Naughty, naughty!")
            return
        
        self.KEY_RIGHT_UP = new
        self.parser.set('Keybinds', 'RIGHT_UP', new)
    
    def get_key_right_up(self):
        return self.KEY_RIGHT_UP
    
    def write_key_right_dn(self, new):
        if not isinstance(new, int):
            print("[ERROR] Cfg.write_key_right_dn: Non-Int value given! Naughty, naughty!")
            return
        
        self.KEY_RIGHT_DN = new
        self.parser.set('Keybinds', 'RIGHT_DN', new)
    
    def get_key_right_dn(self):
        return self.KEY_RIGHT_DN
    
    def commit_to_ini(self):
        fileobj = open('settings.ini', 'w')
        self.parser.write(fileobj)
        fileobj.close()


config = Cfg()

# ----- ENDE SETTINGS LADEN -----

# ----- KONSTANTEN -----
""" Dict mit den Paths zu den relevanten Bildern: """
SPRITE = {
    "schlaeger": abspath("./sprites/schlaeger_small.jpg"),
    "ball": abspath("./sprites/ball.jpg")
    # fwd slashes, da \b zu nem specialchar gemacht wird(?????)
}

""" Richtungskonstanten: """
EAST = 0
SOUTH = 90
WEST = 180
NORTH = 270

""" Keypress-Dict """
KEY = {
    'arr_up': 38,
    'arr_dn': 40,
    'arr_lt': 37,
    'arr_rt': 39,
    'esc': 27,
    'ctrl': 17,
    'shift': 16,
    'space': 32,
    'a': 65,
    'b': 66,
    'c': 67,
    'd': 68,
    'e': 69, # nice
    'f': 70,
    'g': 71,
    'h': 72,
    'i': 73,
    'j': 74,
    'k': 75,
    'l': 76,
    'm': 77,
    'n': 78,
    'o': 79,
    'p': 80,
    'q': 81,
    'r': 82,
    's': 83,
    't': 84,
    'u': 85,
    'v': 86,
    'w': 87,
    'x': 88,
    'y': 89,
    'z': 90,
    '0': 48,
    '1': 49,
    '2': 50,
    '3': 51,
    '4': 52,
    '5': 53,
    '6': 54,
    '7': 55,
    '8': 56,
    '9': 57
}

START_DIRECTIONS = list(range(0, 60)) \
                + list(range(120, 240)) \
                + list(range(300, 359))

""" Blanke Objekte des Typs 'object' sind nur mit sich selbst identisch.
Hiermit kann ich arbiträre Konstanten definieren, die zB. hier nur zur
Spezifikation eines Funktionsverhaltens dienen:

obj1 = object()
obj2 = object()
print(obj1 is obj2) # prints False
print(obj1 == obj2) # prints False

obj3 = object()
ref = obj3
print(obj3 is ref) # prints True
print(obj3 == ref) # prints True

Dies ist bei den Richtungen nicht sinnvoll, da diese etwas weiteres bedeuten
und nicht nur selbstidentisch sein müssen.

(veraltet; ich hab auf den Weg mal was implementiert, habs aber wieder entfernt)
"""
# ----- ENDE KONSTANTEN -----