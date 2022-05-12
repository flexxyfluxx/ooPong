""" Menu:
Hier werden die MainMenu-Methoden definiert.
"""

""" Imports: """
import gamegrid as gg
import ConfigParser as cp
from constants_etc import *
import MainMenu
import ConfigParser as cp # o_o realization

# ----- SETTINGS VON INI LADEN -----
parser = cp.ConfigParser()
parser.read("settings.ini")
class Cfg():
    WINDOW_HEIGHT = parser.getint('WindowDimensions', 'WINDOW_HEIGHT')
    WINDOW_HEIGHT = 200 if WINDOW_HEIGHT < 200 else WINDOW_HEIGHT
    
    WINDOW_WIDTH = parser.getint('WindowDimensions', 'WINDOW_WIDTH')
    WINDOW_WIDTH = 200 if WINDOW_WIDTH < 200 else WINDOW_WIDTH
    
    PADDLE_SPEED = parser.getint('GameSettings', 'PADDLE_SPEED')
    PADDLE_ACCEL_LIMIT = parser.getfloat('GameSettings', 'PADDLE_ACCEL_LIMIT')
    BALL_SPEED = parser.getint('GameSettings', 'BALL_SPEED')
    OBSTACLES = parser.getboolean('GameSettings', 'OBSTACLES')
    
    KEYBINDS = [
        [
            parser.getint('Keybinds', 'LEFT_UP') if parser.has_option('Keybinds', 'LEFT_UP') \
                    else parser.getint('DefaultKeybinds', 'LEFT_UP'),
            parser.getint('Keybinds', 'LEFT_DN') if parser.has_option('Keybinds', 'LEFT_DN') \
                    else parser.getint('DefaultKeybinds', 'LEFT_DN')
        ],
        [
            parser.getint('Keybinds', 'RIGHT_UP') if parser.has_option('Keybinds', 'RIGHT_UP') \
                    else parser.getint('DefaultKeybinds', 'RIGHT_UP'),
            parser.getint('Keybinds', 'RIGHT_DN') if parser.has_option('Keybinds', 'RIGHT_DN') \
                    else parser.getint('DefaultKeybinds', 'RIGHT_DN')
        ]
    ]
# ----- ENDE SETTINGS LADEN -----

# ----- DEFINITIONSBEREICH -----

def get_key(dict_, val):
    return [key for key, v in dict_.items() if v == val]

def setup_MainMenu(menu):
    menu.jtf_wndw_height.setText(str(WINDOW_HEIGHT))
    menu.jtf_wndw_width.setText(str(WINDOW_WIDTH))
    menu.jtf_ball_speed.setText(str(BALL_SPEED))
    
    menu.jtb_obstacles.setText(str(OBSTACLES))
    
    menu.jbtn_kbind_left_up.setText(get_key(KEY, KEYBINDS[0][0]))
    menu.jbtn_kbind_left_dn.setText(get_key(KEY, KEYBINDS[0][1]))
    menu.jbtn_kbind_right_up.setText(get_key(KEY, KEYBINDS[1][0]))
    menu.jbtn_kbind_right_dn.setText(get_key(KEY, KEYBINDS[1][1]))

def onclick_play(event):
    print("Yey lesgo")

def onclick_obstacles(event):
    print(menu.jtb_obstacles.getAccessibleContext())

def onclick_save_settings(event):
    print("Click!")

def onclick_kbind_left_up(event):
    pass

def onclick_kbind_left_dn(event):
    pass

def onclick_kbind_right_up(event):
    pass

def onclick_kbind_right_dn(event):
    pass

def bind_onclicks(menu):
    menu.jbtn_play.actionPerformed = onclick_play
    menu.jtb_obstacles.actionPerformed = onclick_obstacles
    menu.jbtn_kbind_left_up.actionPerformed = onclick_kbind_left_up
    menu.jbtn_kbind_left_dn.actionPerformed = onclick_kbind_left_dn
    menu.jbtn_kbind_right_up.actionPerformed = onclick_kbind_right_up
    menu.jbtn_kbind_right_dn.actionPerformed = onclick_kbind_right_dn

# ----- ENDE DEFINITIONSBEREICH -----
    
# ----- MAIN -----
if __name__ == "__main__":
    menu = MainMenu()
    bind_onclicks(menu)
    
    menu.setVisible(True)