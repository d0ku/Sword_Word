import os
import sys
import random
import time

from Getch import getch
from Grid2D import Grid2D
from WordsGenerating import Random_Word_Generator, Word
from Functions import clear_screen
from Game import Game
from Menu import Menu,MainMenu,OptionsMenu
from Music import Music
from Language import Language

class GameObjects:
    
    def __init__(self):
        self.language=Language()
        self.box = Grid2D(50, 10)
        self.dictionary = Random_Word_Generator()
        self.dictionary.load_dictionary()
        self.game = Game(self.box,self.language)
        self.game.choose_generator(self.dictionary)
        self.music=Music()
        self.game.connect_music(self.music)

    def connect_music(self,music):
        self.music=music
        self.game.connect_music(self.music)


#music = Music()
#music.play_music(self.connected_object.music.music_location+"menu_music.ogg")
game_itself=GameObjects()
#game_itself.connect_music(music)
game_itself.music.play_music("menu_music.ogg")

menu = MainMenu()
menu.add_position(game_itself.language.menu[0])
menu.add_position(game_itself.language.menu[1])
menu.add_position(game_itself.language.menu[13]) #to_be_added
menu.add_position(game_itself.language.menu[2])
menu.add_position(game_itself.language.menu[3])
menu.add_position(game_itself.language.menu[4])
menu.add_position(game_itself.language.menu[5])
menu.connect_game_object(game_itself)
menu.print_menu()
temp="l" #27 Esc
while True:
    temp = getch()
    print("1st")
    menu.interact(temp)
