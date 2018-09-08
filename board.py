import math


class NewBoard():

    def __init__(self, width, height):

        pos = [[None for x in range(width)] for y in range(height)]

        for x in range(len(pos)):
            for y in range(len(pos[x])):
                print pos[x][y]
        

board = NewBoard(8, 8)

