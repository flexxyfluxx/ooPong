""" Universal Constants Module:
Enthält die ganzen Dicts und so.
Hier werden außerdem die Settings aus der INI geparsed
und Konstanten zugewiesen.
"""

""" Imports: """
from os.path import abspath

# oh nyo the namespace OwO~ onwy impowt whats neccessawy~~ rawr :3
from gamegrid import getKeyCodeWait
import ConfigParser as cp # o_o realization

# ----- SETTINGS VON INI LADEN -----
parser = cp.ConfigParser()
parser.read("settings.ini")

WINDOW_HEIGHT = parser.getint('WindowDimensions', 'WINDOW_HEIGHT')
WINDOW_HEIGHT = 200 if WINDOW_HEIGHT < 200 else WINDOW_HEIGHT

WINDOW_WIDTH = parser.getint('WindowDimensions', 'WINDOW_WIDTH')
WINDOW_WIDTH = 200 if WINDOW_WIDTH < 200 else WINDOW_WIDTH

PADDLE_SPEED = parser.getint('GameSettings', 'PADDLE_SPEED')
BALL_SPEED = parser.getint('GameSettings', 'BALL_SPEED')
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