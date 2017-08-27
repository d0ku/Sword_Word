from Getch import getch
from GridLogos import logos
import time
import os
import random
import select
import sys


gamespeed = 0.04


def clear_screen():
    if os.name == 'posix':
        # clear
        os.system("clear")
        print("clear")
    elif os.name == 'nt':
        os.system("cls")
        print("cls")


class Grid2D:
    xsize = 0
    ysize = 0
    matrix = []
    players = []
    obstacles = []
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

        floor = ["_" for y in range(0, y)]

        for i in range(0, x):
            xsize.append(matrix[:])

        for i in range(0, x):
            xsize[i][int(round(y / 2 + 1))] = "_"
            xsize[i][int(round(y / 2 - 2))] = "_"

        self.matrix_empty = matrix[:]
        self.matrix_empty[int(round(y / 2 + 1))] = "_"
        self.matrix_empty[int(round(y / 2 - 2))] = "_"

       # for x in range(0,x):
      #  for y in range (0,y):
        #    if y==player_location[1]:
        #     matrix[x][y]='_'
        return xsize

    def restart(self):
        self.matrix = self.generate_2D_grid(self.xsize, self.ysize)

    def connect_player(self, player):
        self.players.append(player)

    # def change_character(self,string, position, char_to_change_to):
     #   to_return = ""
      #  temp = list(string)
       # temp[position] = char_to_change_to
        # for i in temp:
        #   to_return += temp[i]
        # return to_return

    def print_2D_grid(self):

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

        print(self.players[0].x, self.players[0].y)

xsize = 20
ysize = 10

mapa = Grid2D(xsize, ysize)
player1 = Player(2, int(round(ysize / 2)), "stand", 3, "x", mapa)

game = Game(mapa, player1)

mapa.connect_player(player1)

# player_location = [2, int(round(ysize / 2)), "stand"]  # initial settings
# matrix = generate_2D_grid(xsize, ysize, player_location)  # initial settings


logos(1)  # displays first menu entry

# window=curses.initscr()
# window.timeout(500)
# curses.noecho()

# a=select.select([sys.stdin.read(1)],[],[],5)
i = 0
a = ""
while a != 'q':
    # mapa.print_2D_grid()

    if i % 5 == 0:
        mapa.generate_random_obstacles()
        mapa.add_obstacles_to_map()

    game.print_map()
    game.check_collisions()
    print("TIMEPASS" + str(i))
    # try:
    a = getch(gamespeed)

    # except:
    #   print("noinput")
    if a != "q" and a != "p":
        if a == "w" or a == " ":
            game.player_jump(player1)
        elif a == "s":
            game.player_slide(player1)

        # player1.move(a)
    if a == "p" or a == chr(033):
        logos(6)
    i += 1

# os.system("reset")
