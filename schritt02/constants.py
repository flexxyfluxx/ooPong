""" Universal Constants Module:
Enthält die ganzen Dicts und so.
"""

from os.path import abspath # oh nyo the namespace OwO~ onwy impowt whats neccessawy~~ rawr :3

# ----- KONSTANTEN -----
""" Dict mit den Paths zu den relevanten Bildern: """
SPRITE = {
    "schlaeger" : abspath(".\sprites\schlaeger_small.jpg"),
    "ball" : abspath(".\sprites\ball.jpg")
}

""" Richtungskonstanten: """
EAST = 0
SOUTH = 90
WEST = 180
NORTH = 270

""" Keypress-Dict """
KEY = {
    'arr_up' : 38,
    'arr_dn' : 40,
    'arr_lt' : 37,
    'arr_rt' : 39,
    'esc' : 27,
    'ctrl' : 17,
    'shift' : 16,
    'space' : 32,
    'a' : 65,
    'b' : 66,
    'c' : 67,
    'd' : 68,
    'e' : 69, # nice
    'f' : 70,
    'g' : 71,
    'h' : 72,
    'i' : 73,
    'j' : 74,
    'k' : 75,
    'l' : 76,
    'm' : 77,
    'n' : 78,
    'o' : 79,
    'p' : 80,
    'q' : 81,
    'r' : 82,
    's' : 83,
    't' : 84,
    'u' : 85,
    'v' : 86,
    'w' : 87,
    'x' : 88,
    'y' : 89,
    'z' : 90,
    '0' : 48,
    '1' : 49,
    '2' : 50,
    '3' : 51,
    '4' : 52,
    '5' : 53,
    '6' : 54,
    '7' : 55,
    '8' : 56,
    '9' : 57
}
# ----- ENDE KONSTANTEN -----

# ----- TESTBEREICH -----
if __name__ == "__main__":
    """ Hier können nach Bedarf Tests ausgefhrt werden. """
    pass