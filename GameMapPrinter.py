import threading
import time

class GameMapPrinter(threading.Thread):
    """That class aim is to redraw 'map' every Game.timeout seconds"""
    def __init__(self, game_object):
        threading.Thread.__init__(self)
        self.game_object=game_object

    def run(self):
        while self.game_object.end_printer!=1: #this should be locked in some way
            print("ALIVE!")
            self.game_object.print_map() #
            time.sleep(self.game_object.timeout)
            self.game_object.words_move()
            self.game_object.check_collisions()
            self.game_object.add_word()
        self.game_object.end_printer=0