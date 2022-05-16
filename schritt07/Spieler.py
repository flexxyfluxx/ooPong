""" Spieler:
Beschreibt die Spieler-Klasse.
"""

# keine Imports luhl

""" class Spieler:
erzeugt das Spieler-Objekt, welches Namen, Punktzahl und Highscore besitzt.
"""
class Spieler():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.highscore = 0 # you are useless. you are nothing to me.
    
    
    def get_name(self):
        return self.name
    
    
    def set_points(self, points):
        self.points = count
    
    
    def get_points(self):
        return self.points
    
    
    def add_points(self, points):
        self.points += points