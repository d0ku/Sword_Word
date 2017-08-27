from Getch import getch
import os
import sys
import time
from Functions import clear_screen
from Grid2D import Grid2D
from WordsGenerating import Random_Word_Generator, Word
from Functions import clear_screen, Colors, return_all_dictionaries
from Game import Game
from Language import Word


class Menu:
    pressed_entry = ""
    entries_names = []
    selected_entry = 0
    connected_object = None

    def __init__(self, entries_names=[]):
        self.entries_names = entries_names

    def connect_game_object(self, object):
        self.connected_object = object

    def print_menu(self):
        clear_screen()

        for x in self.entries_names:
    
            if type(x) is Word:
                x.update()
                if x != self.entries_names[self.selected_entry]:
                    print("    " + str(x))
                else:
                    print("  > " + str(x))
            else:
                if x != self.entries_names[self.selected_entry]:
                    print("    " + str(x))
                else:
                    print("  > " + str(x))



    def add_position(self, Word_object):
        self.entries_names.append(Word_object)

    def move_pointer(self, direction):
        if direction == "up":
            if self.selected_entry >= 1:
                self.selected_entry -= 1
        if direction == "down":
            if self.selected_entry < len(self.entries_names) - 1:
                self.selected_entry += 1
        self.print_menu()

    def interact(self, button):
        temp = ord(button)
        if temp == 119:  # add up arrow key
            #pygame.init()
            #song = pygame.mixer.Sound("music/menu_change.ogg")
            self.connected_object.music.play_sound("music/menu_change.ogg")
            #song.play()
            self.move_pointer("up")
        elif temp == 115:  # add down arrow key
            self.connected_object.music.play_sound("music/menu_change.ogg")
            self.move_pointer("down")
        elif temp == 13:
            self.connected_object.music.play_sound("music/menu_click.ogg")
            self.pressed_entry = self.entries_names[self.selected_entry]
            self.open_entry(self.pressed_entry)

    def open_entry(self, entry_name):
        print("This is your part :D")
        time.sleep(2)

    def reload_entries(self):
        pass


class OptionsMenu(Menu):

    def open_entry(self, entry_name):

        print(self.entries_names)
        print("ENTRYSTUFF")
        print(entry_name)
        print(self.pressed_entry)
        if entry_name.word == self.connected_object.language.menu[7].word:
            dictionary_location = os.getcwd()+"/dictionaries"
            dictionary_list = return_all_dictionaries(dictionary_location)
            dictionaries_menu = DictionariesMenu()
            dictionaries_menu.connect_game_object(self.connected_object)
            dictionaries_menu.entries_names = []
            for x in dictionary_list:
                dictionaries_menu.add_position(x)
            dictionaries_menu.add_position(self.connected_object.language.menu[11])

            clear_screen()
            dictionaries_menu.print_menu()
            while str(dictionaries_menu.pressed_entry) != str(self.connected_object.language.menu[11]):
                temp = getch()
                dictionaries_menu.interact(temp)
            dictionaries_menu = None
            # dictionary_list=os.listdir(os.getcwd()+"/dictionaries")
        if entry_name.word == self.connected_object.language.menu[8].word:
            language_location = os.getcwd()+"/languages"
            language_list = os.listdir(language_location)
            languages_menu = LanguagesMenu()
            languages_menu.connect_game_object(self.connected_object)
            languages_menu.entries_names = []
            for x in language_list:
                languages_menu.add_position(x)
            languages_menu.add_position(self.connected_object.language.menu[11])

            clear_screen()
            languages_menu.print_menu()
            while str(languages_menu.pressed_entry) != str(self.connected_object.language.menu[11]):
                temp = getch()
                languages_menu.interact(temp)
            languages_menu = None
            # dictionary_list=os.listdir(os.getcwd()+"/dictionaries")
        if entry_name.word == self.connected_object.language.menu[9].word:
            self.connected_object.music.switch_sound()
        if entry_name.word == self.connected_object.language.menu[10].word:
            self.connected_object.music.switch_music()


        if str(entry_name) == str(self.connected_object.language.menu[11]):
            pass

        self.print_menu()

class DictionariesMenu(Menu):

    def open_entry(self, entry_name):


        print(self.pressed_entry)
        for x in self.entries_names:
            if str(entry_name)==str(x) and str(x) !=str(self.connected_object.language.menu[11]) and os.path.exists(os.getcwd()+"/dictionaries/"+str(entry_name)):
                print("SLOWNIK")
                time.sleep(2)
                self.connected_object.game.can_be_continued=False
                self.connected_object.dictionary.load_dictionary(os.getcwd()+"/dictionaries/"+str(entry_name))
                break

        if str(entry_name) == str(self.connected_object.language.menu[11]):
            pass

        self.print_menu()

class LanguagesMenu(Menu):

    def open_entry(self, entry_name):

        print(self.entries_names)
        print(entry_name)
        print(self.pressed_entry)
        print(str(self.entries_names[2]))
        for x in self.entries_names:
            if str(entry_name)==str(x) and str(x) !=str(self.connected_object.language.menu[11]) and os.path.isdir(os.getcwd()+"/languages/"+str(entry_name)):
                self.connected_object.language.load_language(os.getcwd()+"/languages/"+str(entry_name))
                print(x)
                time.sleep(2)
                self.print_menu()
        if str(entry_name) == str(self.connected_object.language.menu[11]):
            pass

        self.print_menu()




class MainMenu(Menu):

    def open_entry(self, entry_name):

        if str(entry_name) == str(self.connected_object.language.menu[5]):
            clear_screen()

            print("See you soon :) ")

            time.sleep(2)

            sys.exit()
        elif str(entry_name) == str(self.connected_object.language.menu[0]):
            self.connected_object.music.stop_remember("Menu")
            self.connected_object.music.play_music("music/game_music.ogg")

            self.connected_object.game.reset()

            self.connected_object.game.add_word()
            while self.connected_object.game.exit_state != 1:
                self.connected_object.game.run()
            self.connected_object.game.exit_state = 0
            self.connected_object.music.stop_remember("Game")
            self.connected_object.music.play_remember("Menu")
            # Start the game
            #
        elif entry_name.word == self.connected_object.language.menu[1].word:
            
            if self.connected_object.game.can_be_continued == True:
                self.connected_object.music.stop_remember("Menu")
                self.connected_object.music.play_remember("Game")
                self.connected_object.game.continued=True
                self.connected_object.game.add_word()
                while self.connected_object.game.exit_state != 1:
                    self.connected_object.game.run()
                self.connected_object.game.exit_state = 0
                self.connected_object.music.stop_remember("Game")
                self.connected_object.music.play_remember("Menu")
                # Load the game
            else:
                clear_screen()
                print(self.connected_object.language.menu[6].word)
                time.sleep(2)

        elif entry_name.word == self.connected_object.language.menu[2].word:
            options_menu = OptionsMenu()
            options_menu.connect_game_object(self.connected_object)
            options_menu.entries_names = []
            options_menu.add_position(self.connected_object.language.menu[7])
            options_menu.add_position(self.connected_object.language.menu[8])
            options_menu.add_position(self.connected_object.language.menu[9])
            options_menu.add_position(self.connected_object.language.menu[10])
            options_menu.add_position(self.connected_object.language.menu[11])
            clear_screen()
            options_menu.print_menu()
            while str(options_menu.pressed_entry) != str(self.connected_object.language.menu[11]):
                temp = getch()
                options_menu.interact(temp)
            options_menu = None

        elif entry_name.word == self.connected_object.language.menu[3].word:
            with open(self.connected_object.language.location+"/help.txt", "r") as help:
                clear_screen()
                for x in help:
                    print(x)

                keyboard = Colors.GREEN + "`" + Colors.ENDCOLOR + Colors.YELLOW + "1" + Colors.ENDCOLOR + Colors.YELLOW + "2" + Colors.ENDCOLOR + Colors.YELLOW + "3" + Colors.ENDCOLOR + Colors.RED + "4" + Colors.ENDCOLOR + Colors.BLUE + "5" + Colors.ENDCOLOR + Colors.BLUE + "6" + Colors.ENDCOLOR + Colors.BLUE + "7" + Colors.ENDCOLOR + Colors.RED + "8" + Colors.ENDCOLOR + Colors.YELLOW + "9" + Colors.ENDCOLOR + Colors.YELLOW + "0" + Colors.ENDCOLOR + Colors.YELLOW + "-" + Colors.ENDCOLOR + Colors.GREEN + "=" + Colors.ENDCOLOR + "\n" + Colors.GREEN + "TAB" + Colors.ENDCOLOR + Colors.YELLOW + "q" + Colors.ENDCOLOR + Colors.YELLOW + "w" + Colors.ENDCOLOR + Colors.RED + "e" + Colors.ENDCOLOR + Colors.BLUE + "r" + Colors.ENDCOLOR + Colors.BLUE + "t" + Colors.ENDCOLOR + Colors.BLUE + "y" + Colors.ENDCOLOR + Colors.BLUE + "u" + Colors.ENDCOLOR + Colors.RED + "i" + Colors.ENDCOLOR + Colors.YELLOW + "o" + Colors.ENDCOLOR + Colors.YELLOW + "p" + Colors.ENDCOLOR + Colors.YELLOW + \
                    "[" + Colors.ENDCOLOR + Colors.YELLOW + "]" + Colors.ENDCOLOR + Colors.GREEN + "\\" + Colors.ENDCOLOR + "\n" + Colors.GREEN + "CAPS" + Colors.ENDCOLOR + Colors.YELLOW + "a" + Colors.ENDCOLOR + Colors.YELLOW + "s" + Colors.ENDCOLOR + Colors.RED + "d" + Colors.ENDCOLOR + Colors.BLUE + "f" + Colors.ENDCOLOR + Colors.BLUE + "g" + Colors.ENDCOLOR + Colors.BLUE + "h" + Colors.ENDCOLOR + Colors.BLUE + "j" + Colors.ENDCOLOR + Colors.RED + "k" + Colors.ENDCOLOR + Colors.YELLOW + "l" + Colors.ENDCOLOR + Colors.YELLOW + ";" + Colors.ENDCOLOR + Colors.YELLOW + "'" + Colors.ENDCOLOR + \
                    Colors.GREEN + "ENTER" + Colors.ENDCOLOR + "\n" + Colors.GREEN + "SHIFT" + Colors.ENDCOLOR + Colors.YELLOW + "z" + Colors.ENDCOLOR + Colors.YELLOW + "x" + Colors.ENDCOLOR + Colors.RED + "c" + Colors.ENDCOLOR + Colors.BLUE + "v" + Colors.ENDCOLOR + Colors.BLUE + "b" + Colors.ENDCOLOR + \
                    Colors.BLUE + "n" + Colors.ENDCOLOR + Colors.BLUE + Colors.RED + "m" + Colors.ENDCOLOR + Colors.YELLOW + "," + Colors.ENDCOLOR + Colors.YELLOW + \
                    "." + Colors.ENDCOLOR + Colors.YELLOW + "/" + Colors.ENDCOLOR + \
                    Colors.GREEN + "SHIFT" + Colors.ENDCOLOR + "\n" + "                SPACE"
                print(keyboard)
                print(self.connected_object.language.menu[11].word)
                getch()

        elif entry_name.word == self.connected_object.language.menu[4].word:
            with open(self.connected_object.language.location+ "/my_credits.txt", "r") as credits:
                clear_screen()
                for x in credits:
                    print(x)
                    time.sleep(1)
                print(self.connected_object.language.credits[0].word)
                getch()
            # open credits
            #
        self.print_menu()
