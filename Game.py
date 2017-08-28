import os
import math
import sys
import random
import time
import re
from Getch import getch
from Grid2D import Grid2D
from WordsGenerating import Random_Word_Generator, Word
from Functions import clear_screen,Colors

class Game:
    continued=False
    can_be_continued=False
    is_it_safe=True
    deleted=False
    deleted_chars=0
    deleted_words=0
    entered_chars=0
    exit_state=0
    clock_start=0
    words = []
    word_to_append=""
    previous_word=""
    last_word = ""
    timeout = 0.25   # timeout / getch_timeout musi byc wieksze niz 1.5
    max_length = 5
    start_time = 0
    end_time = 0
    cycles = 0
    #getch_timeout=0.66
    #getch_counter=0

    def __init__(self, box,language):
        self.box = box
        self.connect_language(language)
        self.map_connect_words()

    def choose_generator(self, dictionary):
        self.dictionary = dictionary
        self.dictionary.set_box(self.box)

    def set_pace(self,pace):
        if pace=="slow":
            self.timeout=0.5
        if pace=="normal":
            self.timeout=0.25
        if pace=="fast":
            self.timeout=0.15


    def set_max_word_length(self,length):
        self.max_length=length
        
    def add_word(self):

        for x in self.words:
            if x.begin_point<=0:
                self.is_it_safe=False
                break

        if self.word_to_append=="":
            self.word_to_append=self.dictionary.random_word(self.max_length)

        if self.is_it_safe == True  and self.word_to_append!="":
            
            self.words.append(self.word_to_append)
            self.word_to_append=self.dictionary.random_word(self.max_length)

        self.is_it_safe=True

    def print_map(self):
        clear_screen()

        print(self.language.game[6].word+str(round(self.entered_chars/(time.time()-self.clock_start) *60,2)))
        print(self.language.game[5].word+str(round(self.deleted_chars/(time.time()-self.clock_start) *60,2)))
        print(self.language.game[0].word+str(self.deleted_words))

        if self.deleted:
            print(self.language.game[1].word+Colors.GREEN+self.previous_word+Colors.ENDCOLOR)
        else:
            print(self.language.game[1].word+Colors.RED+ self.previous_word+Colors.ENDCOLOR)


        

        
        self.box.print_2D_grid(0)

        does_it_contain=False

        for x in self.words:
            
            if re.match(str(self.last_word),x.word):
                does_it_contain=True
                break
        if does_it_contain:
            print(self.language.game[2].word+Colors.GREEN+self.last_word+Colors.ENDCOLOR)
        else:
            print(self.language.game[2].word+Colors.RED+ self.last_word+Colors.ENDCOLOR)

    def map_connect_words(self):
        self.box.words_connect(self.words)
    def connect_language(self,language):
        self.language=language

    def check_words_and_input(self, word):
        for x in self.words:
            # for i in x.word:
           #     print(i)
            # for i in word:
             #   print(i)
            #print("Comparison "+x.word)
            #print("ypur_word_ "+word)
            if word == x.word:
                self.deleted_chars+=len(word)
                self.deleted=True
                self.deleted_words+=1
                self.words.remove(x)
                break

        if self.deleted:
            self.music_object.play_sound("succes.ogg")
        else:
            self.music_object.play_sound("failure.ogg")

    def reset(self):
        self.word_to_append=""
        self.entered_chars=0
        self.clock_start=0
        self.deleted_chars=0
        temp=self.words[:]
        self.can_be_continued=False
        for x in temp:
            self.words.remove(x)
        self.deleted_word=""
        self.deleted_words=0
        self.exit_state=0
        self.previous_word=""
        self.last_word = ""
        self.start_time = 0
        self.end_time = 0
        self.cycles = 0
        #self.getch_counter=0

    def words_move(self):
        for x in self.words:
            x.begin_point += 1
            x.end_point += 1

    def connect_music(self,music_object):
        self.music_object=music_object

    def check_collisions(self):
        for x in self.words:
            if x.end_point >self.box.xsize:
                clear_screen()
                self.music_object.play_sound("game_lost.ogg")
                print(self.language.game[3].word)
                self.exit_state=1
                print(self.language.game[4].word)
                time.sleep(2)
                getch()

    def char_handling(self,char):
        if char!=None:
            self.music_object.play_sound("button_pressed.ogg",1)
            if ord(char)==13 or ord(char)==32:
                self.deleted=False
                self.previous_word=self.last_word
                self.check_words_and_input(self.last_word)
                self.last_word=""
                self.print_map()
                return None
            elif ord(char)==127:
                self.last_word=self.last_word[0:len(self.last_word)-1]
                self.print_map()
                return None
            elif ord(char)==27:
                self.time_backup=time.time()-self.clock_start
                #here comes the menu invoke
                #sys.exit()
                self.exit_state=1
            else:
                self.entered_chars+=1
                self.last_word+=char
                self.print_map()
                return None

    def run(self):
        self.can_be_continued=True
        if self.cycles == 0:
            self.clock_start=time.time()
            self.start_time = time.clock()
            self.print_map()
            self.end_time=time.clock()

        if self.continued:
            self.clock_start=time.time()-self.time_backup
            self.start_time = time.clock()
            self.end_time=time.clock()
            self.continued=False

        #self.end_time=time.clock()+self.getch_timeout*self.getch_counter
        #self.last_word=input()
        getch_start_time=time.time()
        temp=getch(0.20)
        self.end_time+=time.time()-getch_start_time
        getch_start_time=0
        #self.getch_counter+=1
        self.char_handling(temp)

        #i, o, e = select.select([], [], [], self.timeout)
        # if (i):

        # else:
        #    print("TIMEOUT")

        #self.last_word = input()
        

        #self.check_words_and_input(self.last_word)

        if self.end_time - self.start_time > self.timeout:
            # that for is not elegant
            for x in range(0, int(round((self.end_time - self.start_time) / self.timeout))):

                self.words_move()
                self.check_collisions()
                self.print_map()

            self.start_time = self.end_time
            self.end_time=time.clock()
        self.add_word()
        self.cycles += 1


# box=Grid2D(60,20)
# box.print_2D_grid()


# for x in range(0,100000):
#    print(dictionary.random_english_word())
