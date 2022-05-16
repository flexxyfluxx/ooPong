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
#from Ball import *
#from Anzeige import *
#from Collisions import *
#from DumbSchlaeger import *
#from Schlaeger import *
#from Spieler import *
#from time import sleep
from java.awt.event import KeyListener
from ponk import *

# ----- DEFINITIONSBEREICH -----

temp_btn_settings = {
    'obstacles': config.get_obstacle_state()
    # Momentan ist hier nur eine Option drin,
    # aber man könnte hier weitere Optionswerte zwischenspechern, falls nötig
}

""" Ich weiß nicht mehr, wozu ich diese Funktion benötigt habe, aber anscheinend habe ich sie mal als nötig empfunden.
# Vielleicht von damals, als ich noch Keybind-Settings implementieren wollte...

def get_key(dict_, val):
    return [key for key, v in dict_.items() if v == val]
#"""

def setup_mainmenu(menu):
    menu.jtf_wndw_height.setText(str(config.get_wndw_height()))
    menu.jtf_wndw_width.setText(str(config.get_wndw_width()))
    menu.jtf_ball_speed.setText(str(config.get_ball_speed()))
    menu.jtf_paddle_speed.setText(str(config.get_paddle_speed()))
    
    menu.jbtn_obstacles.setText("An" if config.get_obstacle_state() else "Aus")
    

def onclick_play(event, menu):
    menu.dispose()
    play_game(False, config.get_obstacle_state())


def onclick_obstacles(event, menu):
    temp_btn_settings['obstacles'] = False if temp_btn_settings['obstacles'] \
                            else True
    menu.jbtn_obstacles.setText("An" if temp_btn_settings['obstacles'] else "Aus")


def onclick_save_settings(event, menu):
    """
    Versuche, die geg. Werte als Ints zu speichern.
    So oder so wird der gespeicherte Wert wieder ins Textfield geladen.
    zB. Textfield enthält "236": 236 wird gespeichert;
        Feld enthält "236.52": 236 wird gespeichert; 236 wird ins Feld geschrieben;
        Feld enthält "Zweihundertsechsunddreißig"; enthielt vorher 200 (bereits gespeichert):
                    200 wird ins Feld geschrieben; bereits gespeicherter Wert bleibt erhalten.
    """
    try:
        config.write_wndw_height(int(menu.jtf_wndw_height.getText()))
    except:
        pass # why god why
    finally:
        menu.jtf_wndw_height.setText(str(config.get_wndw_height()))
    
    try:
        config.write_wndw_width(int(menu.jtf_wndw_width.getText()))
    except:
        pass
    finally:
        menu.jtf_wndw_width.setText(str(config.get_wndw_width()))
    
    try:
        config.write_ball_speed(int(menu.jtf_ball_speed.getText()))
    except:
        pass
    finally:
        menu.jtf_ball_speed.setText(str(config.get_ball_speed()))
    
    try:
        config.write_paddle_speed(int(menu.jtf_paddle_speed.getText()))
    except:
        pass
    finally:
        menu.jtf_paddle_speed.setText(str(config.get_paddle_speed()))
    
    # Welcome to this week's CODER FRUSTRATION, ep. [idgaf anymore]!
    # Today's show: Try-finally!!1
    # 
    # Why on god's green earth does 'finally' not suppress errors like except does?!
    # What is even the point of try block in try finally???
    # If I do Try Finally, I still get an err, but the finally block still runs.
    # so, to suppress this obv redundant err (yes of course there's an err when you turn "abcdefg" into an int! you fukcinng cANT°1!),
    # I have to put this *ugly ass* except pass abomination in between to tell it to take the err... and do FKG NOTHING
    # why even use try
    # 
    # pep 3157: implicit except pass. similar to php stfu operator (@).
    # if you put sth in try block, that means you are taking full control over err handling process (ie. isn't done automatically anymore)
    # yes this has risks, but why even use try if you want vanilla err msg's?
    
    config.write_obstacles(temp_btn_settings['obstacles'])
    
    config.commit_to_ini()

def bind_onclicks(menu):
    menu.jbtn_play.actionPerformed = lambda event: onclick_play(event, menu)
    menu.jbtn_obstacles.actionPerformed = lambda event: onclick_obstacles(event, menu)
    menu.jbtn_save_settings.actionPerformed = lambda event: onclick_save_settings(event, menu)

# ----- ENDE DEFINITIONSBEREICH -----
    
# ----- MAIN -----
if __name__ == "__main__":
    menu = MainMenu()
    setup_mainmenu(menu)
    bind_onclicks(menu)
    
    menu.setVisible(True)