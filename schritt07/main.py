""" Menu:
Hier werden die MainMenu-Methoden definiert.
"""

""" Imports: """
import gamegrid as gg
import ConfigParser as cp
from constants_etc import *
import MainMenu
import ConfigParser as cp # o_o realization
import sys
from Ball import *
from Anzeige import *
from Collisions import *
from DumbSchlaeger import *
from Schlaeger import *
from Spieler import *
from time import sleep
from java.awt.event import KeyListener
from ponk import *

# ----- DEFINITIONSBEREICH -----

temp_btn_settings = {
    'obstacles': config.get_obstacle_state(),
    'left_up': config.get_key_left_up(),
    'left_dn': config.get_key_left_dn(),
    'right_up': config.get_key_right_up(),
    'right_dn': config.get_key_right_dn()
}

# Keylistener für das Mainmenu definieren/erstellen
def kbind_things(event, menu):
    if menu.key == 1: # Left Up
        print("Left Up bind registered!")
        menu.key = 0
    if menu.key == 2: # Left Down
        print("Left Down bind registered!")
        menu.key = 0
    if self.key == 3: # Right Up
        print("Right Up bind registered!")
        menu.key = 0
    if self.key == 4: # Right Down
        print("Right Down bind registered!")
        menu.key = 0

def get_key(dict_, val):
    return [key for key, v in dict_.items() if v == val]

def setup_mainmenu(menu):
    menu.jtf_wndw_height.setText(str(config.get_wndw_height()))
    menu.jtf_wndw_width.setText(str(config.get_wndw_width()))
    menu.jtf_ball_speed.setText(str(config.get_ball_speed()))
    
    menu.jbtn_obstacles.setText("An" if config.get_obstacle_state() else "Aus")
    
    menu.jbtn_kbind_left_up.setText(str(get_key(KEY, config.get_key_left_up())[0]))
    menu.jbtn_kbind_left_dn.setText(str(get_key(KEY, config.get_key_left_dn())[0]))
    menu.jbtn_kbind_right_up.setText(str(get_key(KEY, config.get_key_right_up())[0]))
    menu.jbtn_kbind_right_dn.setText(str(get_key(KEY, config.get_key_right_dn())[0]))

def onclick_play(event, menu):
    menu.dispose()
    del sys.modules['MainMenu']
    """
    import ponk
    """
    play_game(False, config.get_obstacle_state())
    #"""

def onclick_obstacles(event, menu):
    temp_settings['obstacles'] = False if config.get_obstacle_state() \
                            else True
    menu.jbtn_obstacles.setText("An" if temp_settings['obstacles'] else "Aus")
    
def onclick_kbind_left_up(event, menu):
    menu.key = 1

def onclick_kbind_left_dn(event, menu):
    menu.key = 2

def onclick_kbind_right_up(event, menu):
    menu.key = 3

def onclick_kbind_right_dn(event, menu):
    menu.key = 4

def onclick_save_settings(event, menu):
    try:
        config.write_wndw_height(int(menu.jtf_wndw_height.getText()))
    finally:
        menu.jtf_wndw_height.setText(str(config.get_wndw_height()))
    
    try:
        config.write_wndw_width(int(menu.jtf_wndw_width.getText()))
    finally:
        menu.jtf_wndw_width.setText(str(config.get_wndw_width()))
    
    try:
        config.write_ball_speed(int(menu.jtf_ball_speed.getText()))
    finally:
         menu.jtf_ball_speed.setText(str(config.get_ball_speed()))
    
    config.write_obstacles(temp_btn_settings['obstacles'])
    config.write_key_left_up(temp_btn_settings['left_up'])
    config.write_key_left_dn(temp_btn_settings['left_dn'])
    config.write_key_right_up(temp_btn_settings['right_up'])
    config.write_key_right_dn(temp_btn_settings['right_dn'])
    
    config.commit_to_ini()


def bind_onclicks(menu):
    menu.jbtn_play.actionPerformed = lambda event: onclick_play(event, menu)
    menu.jbtn_obstacles.actionPerformed = lambda event: onclick_obstacles(event, menu)
    menu.jbtn_save_settings.actionPerformed = lambda event: onclick_save_settings(event, menu)
    menu.jbtn_kbind_left_up.actionPerformed = lambda event: onclick_kbind_left_up(event, menu)
    menu.jbtn_kbind_left_dn.actionPerformed = lambda event: onclick_kbind_left_dn(event, menu)
    menu.jbtn_kbind_right_up.actionPerformed = lambda event: onclick_kbind_right_up(event, menu)
    menu.jbtn_kbind_right_dn.actionPerformed = lambda event: onclick_kbind_right_dn(event, menu)

# ----- ENDE DEFINITIONSBEREICH -----
    
# ----- MAIN -----
if __name__ == "__main__":
    menu = MainMenu()
    menu.keyPressed = lambda event: kbind_things(event, menu)
    setup_mainmenu(menu)
    bind_onclicks(menu)
    
    menu.setVisible(True)