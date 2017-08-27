import os
import sys
import random
import timeit
import select
import time
from Getch import getch


def clear_screen():
    if os.name == 'posix':
        # clear
        os.system("clear")
        print("clear")
    elif os.name == 'nt':
        os.system("cls")
        print("cls")


class Random_Word_Generator:

    dictionary = {}
    dictionary_length = 0

    def __init__(self):
        pass

    def load_english_dictionary(self):
        with open("words_alpha.txt", "r") as english_dictionary:
            words = []
            file_length = 0
            for x in english_dictionary:
                file_length += 1
                words.append(x)

        indexes = [x for x in range(0, file_length)]

        self.dictionary = dict(zip(indexes, words))
        self.dictionary_length = file_length

    def set_box(self, box):
        self.box = box

    def random_english_word(self, max_length=50):

        word_number = random.randint(0, self.dictionary_length)
        corresponding_word = self.dictionary[word_number]
        while len(corresponding_word) > max_length:
            word_number = random.randint(0, self.dictionary_length - 2)
            corresponding_word = self.dictionary[word_number]

        word_object_to_return = Word(corresponding_word, self.box)
        return word_object_to_return


class Word:
    word = ""
    length = 0
    begin_point = 0
    end_point = 0
    height = 0

    def __init__(self, word, box):
        self.box = box
        temp = ""
        for x in word:
            if x != "\n":
                temp += x
        self.word = temp
        self.length = len(word)
        self.height = random.randint(0, len(self.box.matrix[0]) - 1)
        self.end_point = 0
        self.begin_point = self.end_point - self.length


class Grid2D:
    xsize = 0
    ysize = 0
    matrix = []
    words = []
    previous = -1
    counter = 0
    matrix_empty = []

    def __init__(self, x, y):
        self.xsize = x
        self.ysize = y
        self.matrix = self.generate_2D_grid(self.xsize, self.ysize)

    def generate_2D_grid(self, x, y):

        xsize = []

        matrix = ["." for y in range(0, y)]

        #floor = ["_" for y in range(0, y)]

        for i in range(0, x):
            xsize.append(matrix[:])

        self.matrix_empty = matrix[:]

        return xsize

    def restart(self):
        self.matrix = self.generate_2D_grid(self.xsize, self.ysize)

    def words_connect(self, words):
        self.words = words

    def connect_player(self, player):
        self.players.append(player)

    # def change_character(self,string, position, char_to_change_to):
     #   to_return = ""
      #  temp = list(string)
       # temp[position] = char_to_change_to
        # for i in temp:
        #   to_return += temp[i]
        # return to_return
        #
    def organize_grid(self):

        xsize = []

        matrix = ["." for y in range(0, self.ysize)]

        #floor = ["_" for y in range(0, y)]
        print("Organizacja")
        for i in range(0, self.xsize):
            xsize.append(matrix[:])

        # for x in self.words:
            #print (x.word)

        for x in self.words:
            # print(x.begin_point)
            # print(x.end_point)
            if x.end_point >= 0:
                if x.begin_point >= 0:
                    begin = x.begin_point
                else:
                    begin = 0
                counter = 0
                for i in range(x.end_point, begin + 1, -1):
                    if x.word[x.length - counter - 2] != "\n":
                        xsize[i - 2][x.height] = x.word[x.length - counter - 2]
                    counter += 1
                    # print(x.height)
                    # print(x.begin_point-x.end_point+x.length)
                    # if x.length-(x.length-i)<x.length-1:

        return xsize

    def print_2D_grid(self, do_clear_screen=1):

        if do_clear_screen == 1:
            clear_screen()

        matrix_temp = self.organize_grid()

        wall = ""
        for i in range(0, len(self.matrix) + 2):
            wall += "#"

        print(wall)
        to_be_printed = []
        # map printing
        temp = "#"

        for y in range(0, len(matrix_temp[0])):
            for x in range(0, len(matrix_temp)):
                temp += str(matrix_temp[x][y])
            temp += "#"
            print(temp)
            temp = "#"

        print(wall)


class Game:
    words = []
    dictionary = {}
    last_word = ""
    timeout = 0.1
    max_length = 5
    start_time = 0
    end_time = 0
    cycles = 0
    getch_timeout=0.1

    def __init__(self, box):
        self.box = box

    def choose_generator(self, dictionary):
        self.dictionary = dictionary
        self.dictionary.set_box(self.box)

    def add_word(self):
        temp = self.dictionary.random_english_word(self.max_length)
        is_it_safe = True
        # if self.box.organize_grid()[0][temp.height] == ".":
        for x in self.words:
            if x.begin_point <= 0:
                is_it_safe = False
                break
        if is_it_safe:
            self.words.append(temp)

    def print_map(self):
        clear_screen()
        print("Last word: " + self.last_word)
        self.box.print_2D_grid(0)

    def map_connect_words(self):
        self.box.words_connect(self.words)

    def check_words_and_input(self, word):
        for x in self.words:
            # for i in x.word:
           #     print(i)
            # for i in word:
             #   print(i)
            #print("Comparison "+x.word)
            #print("ypur_word_ "+word)
            if word == x.word:
                self.print_map()
                print("LUUUUUUl")
                self.words.remove(x)
                break

    def words_move(self):
        for x in self.words:
            x.begin_point += 1
            x.end_point += 1

    def check_collisions(self):
        for x in self.words:
            if x.end_point > self.box.xsize:
                print("GAME OVER")
                sys.exit()

    def char_handling(self,char):
        if char!=None:
            if ord(char)==13 or ord(char)==32:
                self.check_words_and_input(self.last_word)
                self.last_word=""
                self.print_map()
                return None
            if ord(char)==127:
                self.last_word=self.last_word[0:len(self.last_word)-1]
                self.print_map()
                return None
            else:
                self.last_word+=char
                self.print_map()
                return None

    def run(self):

        if self.cycles == 0:
            self.start_time = time.clock()
            self.print_map()
            self.end_time=time.clock()


        #self.last_word=input()
        temp=getch(self.getch_timeout)
        self.end_time+=self.getch_timeout
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
box = Grid2D(50, 10)
dictionary = Random_Word_Generator()
dictionary.load_english_dictionary()
game = Game(box)
game.choose_generator(dictionary)
game.map_connect_words()

game.add_word()
while True:
    game.run()

# for x in range(0,100000):
#    print(dictionary.random_english_word())
