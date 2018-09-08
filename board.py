
import math

#some stuff to make code better and ez reads
PIECE_COL = 0
PIECE_KING = 1

class NewBoard():

    # Initial Setup
    def __init__(self, width, height):

        # Setup empty board
        self.pos = [[None for x in range(width)] for y in range(height)]

        # Setup pieces

        # total pieces remaining for each color
        totalw = round(((height - 2) * width) / 4)
        totalb = totalw
        
        for row in range(len(self.pos)):
            # check if row is odd number or even number. Will help arrange board layout.
            mode = row % 2

            # odd row, put pieces on odd spaces. even row, put pieces on even spaces.
            for space in range(len(self.pos[row])):
                    
                if space % 2 != mode:

                    #pieces are set up like this: self.pos[row][space](color {0 = white / 1 = black}, king {True/False})
                    self.pos[row][space] = (0, False)
                    totalw -= 1


        #break if there are no more pieces left to place
            if totalw < 1:
                break

            
        #doing same thing, but for black pieces 
        for row in range(len(self.pos) -1, -1, -1):

            mode = row % 2
            
            for space in range(len(self.pos[row]) -1, -1, -1):
                if space % 2 != mode:
                    self.pos[row][space] = (1, False)
                    totalb -= 1
            
            if totalb < 1:
                break

        
    #print board
    def Draw(self):
        for row in range(len(self.pos)):
            for space in range(len(self.pos[row])):
                if self.pos[row][space] != None:
                    if self.pos[row][space][PIECE_COL] == 0:
                        print "O",
                    else:
                        print "X",
                else:
                    print "·",
            print "\n",


board = NewBoard(8, 8)
board.Draw()
