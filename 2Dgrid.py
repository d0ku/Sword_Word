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
