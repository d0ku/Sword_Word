from Functions import clear_screen

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

        for i in range(0, x):
            xsize.append(matrix[:])

        self.matrix_empty = matrix[:]

        return xsize

    def change_x(self):
        self.xsize+=1
        if self.xsize==100:
            self.xsize=20
        self.reset()

    def change_y(self):
        self.ysize+=1
        if self.ysize==100:
            self.ysize=20
        self.reset() 

    def reset(self):
        self.matrix = self.generate_2D_grid(self.xsize, self.ysize)

    def words_connect(self, words):
        self.words = words

    def organize_grid(self):

        xsize = []

        matrix = ["." for y in range(0, self.ysize)]

        for i in range(0, self.xsize):
            xsize.append(matrix[:])

        for x in self.words:
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