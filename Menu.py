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

    def remove_position(self, Word_object):
        self.entries_names.remove(Word_object)

    def change_position_index(self,Word_object,index):
        self.entries_names[index]=Word_object

    def get_position_index(self,Word_object):
        return self.entries_names.index(Word_object)

    def change_position(self, Word_object, Word_object_updated):
        if Word_object in self.entries_names:
            self.entries_names[self.entries_names.index(Word_object)]=Word_object_updated
        else:
            self.entries_names.append(Word_object_updated)

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
        if temp == 119 :  # add up arrow key
            #pygame.init()
            #song = pygame.mixer.Sound("music/menu_change.ogg")
            self.connected_object.music.play_sound("menu_change.ogg")
            #song.play()
            self.move_pointer("up")
        elif temp == 115:  # add down arrow key
            self.connected_object.music.play_sound("menu_change.ogg")
            self.move_pointer("down")
        elif temp == 13:
            self.connected_object.music.play_sound("menu_click.ogg")
            self.pressed_entry = self.entries_names[self.selected_entry]
            self.open_entry(self.pressed_entry)

    def open_entry(self, entry_name):
        print("This is your part :D")
        time.sleep(2)

    def reload_entries(self):
        pass


class OptionsMenu(Menu):

    def open_entry(self, entry_name):

        if entry_name.word == self.connected_object.language.menu[7].word:
            dictionary_location = os.getcwd()+"/dictionaries"
            dictionary_list = return_all_dictionaries(dictionary_location)
            dictionaries_menu = ChooseMenu("/dictionaries/")
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
            languages_menu = ChooseMenu("/languages/")
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

        if entry_name.word == self.connected_object.language.menu[13].word:
            game_menu = ChooseMenu("game_options")
            game_menu.connect_game_object(self.connected_object)
            game_menu.entries_names = []
            entries_names.append()
            game_menu.add_position(self.connected_object.language.menu[11])

            clear_screen()
            game_menu.print_menu()
            while str(game_menu.pressed_entry) != str(self.connected_object.game.menu[11]):
                temp = getch()
                game_menu.interact(temp)
            game_menu = None

        if entry_name.word == self.connected_object.language.menu[14].word:
            music_location = os.getcwd()+"/music"
            music_list = os.listdir(music_location)
            music_menu = ChooseMenu("/music/")
            music_menu.connect_game_object(self.connected_object)
            music_menu.entries_names = []
            for x in music_list:
                music_menu.add_position(x)
            music_menu.add_position(self.connected_object.language.menu[11])

            clear_screen()
            music_menu.print_menu()
            while str(music_menu.pressed_entry) != str(self.connected_object.language.menu[11]):
                temp = getch()
                music_menu.interact(temp)
            music_menu = None
            # dictionary_list=os.listdir(os.getcwd()+"/dictionaries")
        if entry_name.word == self.connected_object.language.menu[9].word:
            self.connected_object.music.switch_sound()
        if entry_name.word == self.connected_object.language.menu[10].word:
            self.connected_object.music.switch_music()

        if entry_name.word ==self.connected_object.language.menu[16].word:
            #temp = self.get_position_index(self.connected_object.language.menu[16].word)
            self.connected_object.language.menu[16].restore()
            self.connected_object.game.max_length_change()
            self.connected_object.language.menu[16].change(self.connected_object.language.menu[16].word + str(self.connected_object.game.max_length))
            #self.change_position_index(self.connected_object.language.menu[16].word + str(self.connected_object.game.max_length),temp)
        if entry_name.word==self.connected_object.language.menu[17].word:
            self.connected_object.language.menu[17].restore()
            self.connected_object.box.change_x()
            self.connected_object.language.menu[17].change(self.connected_object.language.menu[17].word + str(self.connected_object.box.xsize))
            self.connected_object.game.can_be_continued=False
        if entry_name.word==self.connected_object.language.menu[18].word:
            self.connected_object.language.menu[18].restore()
            self.connected_object.box.change_y()
            self.connected_object.language.menu[18].change(self.connected_object.language.menu[18].word + str(self.connected_object.box.ysize))
            self.connected_object.game.can_be_continued=False

        if str(entry_name) == str(self.connected_object.language.menu[11]):
            pass

        self.print_menu()

class ChooseMenu(Menu):

    def __init__(self,keyword,entries_names=[]):
        self.entries_names = entries_names
        self.keyword=keyword

    def open_entry(self,entry_name):


        for x in self.entries_names:
            if str(entry_name)==str(x) and str(x) != str(self.connected_object.language.menu[11]) and os.path.exists(os.getcwd()+self.keyword+str(entry_name)):
                if self.keyword=="/languages/":
                    self.connected_object.language.load_language(os.getcwd()+"/languages/"+str(entry_name))
                if self.keyword=="/dictionaries/":
                    self.connected_object.game.can_be_continued=False
                    self.connected_object.dictionary.load_dictionary(os.getcwd()+"/dictionaries/"+str(entry_name))
                if self.keyword=="/music/":
                    self.connected_object.music.load_music_pack(os.getcwd()+"/music/"+str(entry_name))
                    self.connected_object.music.stop_music()
                    self.connected_object.music.play_music("menu_music.ogg")

        if str(entry_name)==str(self.connected_object.language.menu[11]):
            pass

        self.print_menu()



class MainMenu(Menu):

    def open_entry(self, entry_name):

        if str(entry_name) == str(self.connected_object.language.menu[5]):
            clear_screen()

            print(self.connected_object.language.menu[15])

            time.sleep(2)

            sys.exit()
        elif str(entry_name) == str(self.connected_object.language.menu[0]):
            self.connected_object.music.stop_remember("Menu")
            self.connected_object.music.play_music("game_music.ogg")

            self.connected_object.game.reset()

            while self.connected_object.game.exit_state != 1:
                self.connected_object.game.start_game()
            #self.connected_object.game.exit_state = 0  #this should be locked (threading)
            self.connected_object.music.stop_remember("Game")
            self.connected_object.music.play_remember("Menu")
            # Start the game
        elif entry_name.word == self.connected_object.language.menu[1].word:
            
            if self.connected_object.game.can_be_continued == True:
                self.connected_object.music.stop_remember("Menu")
                self.connected_object.music.play_remember("Game")
                self.connected_object.game.continued=True
                self.connected_object.game.start_game()
                while self.connected_object.game.exit_state != 1:
                    self.connected_object.game.start_game()
                #self.connected_object.game.exit_state = 0  #this should be locked (threading)
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
            options_menu.add_position(self.connected_object.language.menu[14])
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
        
        elif entry_name.word == self.connected_object.language.menu[13].word:
            game_options=OptionsMenu()
            game_options.connect_game_object(self.connected_object)
            game_options.entries_names = []
            self.connected_object.language.menu[16].restore()
            self.connected_object.language.menu[16].change(self.connected_object.language.menu[16].word + str(self.connected_object.game.max_length))
            game_options.add_position(self.connected_object.language.menu[16])
            self.connected_object.language.menu[17].restore()
            self.connected_object.language.menu[17].change(self.connected_object.language.menu[17].word + str(self.connected_object.box.xsize))
            game_options.add_position(self.connected_object.language.menu[17])
            self.connected_object.language.menu[18].restore()
            self.connected_object.language.menu[18].change(self.connected_object.language.menu[18].word + str(self.connected_object.box.ysize))
            game_options.add_position(self.connected_object.language.menu[18])
            game_options.add_position(self.connected_object.language.menu[11])

            clear_screen()
            game_options.print_menu()
            while str(game_options.pressed_entry) != str(self.connected_object.language.menu[11]):
                temp = getch()
                game_options.interact(temp)
            game_options = None
        self.print_menu()
