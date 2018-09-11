
import math

#some stuff to make code better and ez reads
P_COL = 0
P_KING = 1

class NewBoard():

    # Initial Setup
    def __init__(self, width, height):

        # Setup empty board
        self.pos = [[None for x in range(width)] for y in range(height)]

        self.width = width
        self.height = height

        self.turn = 0
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
                    self.pos[row][space] = [0, False]
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

    def Move(self, originY, originX, dirY, dirX): #dirX stands for direction row, dirY stands for direction space (y and x respectively)
        if abs(dirX) != 1 or abs(dirY) != 1:
            print "Can only move 1 space in each direction!"
        dest = (originX + dirX,originY + dirY)
        print dest, "is the destination"
        
        print self.pos[originX][originY], "has been selected"
        
        if self.pos[originX][originY] != None: #Check if a playable piece has been selected
            print "piece detected"
            
            #Check if playable piece is moveable in chosen direction
            if (self.pos[originX][originY][P_COL] == 0 and dirX == 1) or (self.pos[originX][originY][P_COL] == 1 and dirX == -1) or self.pos[originX][originY][P_KING] == True:
                
                if (dest[0] > self.width - 1 or dest[0] < 0) or (dest[1] > self.height - 1 or dest[1] < 0): #check if the piece is going to move out of bounds
                    print "can't move, piece out of bounds"
                elif self.pos[dest[0]][dest[1]] != None: #if the destination is not clear...
                    print "destination blocked..."
                    if self.pos[dest[0]][dest[1]][P_COL] == self.pos[originX][originY][P_COL]: #check if the space is occupied by your own colour
                        print "can't move, piece occupied by own colour"
                    else: #If piece is enemy color...
                        if self.pos[dest[0] + dirX][dest[1] + dirY] != None: #check if piece is capturable
                            print "can't move, capture blocked"
                        else:
                            #Capture piece
                            print "capturing..."
                            self.pos[dest[0] + dirX][dest[1] + dirY] = self.pos[originX][originY]
                            self.pos[dest[0]][dest[1]] = None
                            self.pos[originX][originY] = None
                            if ((dest[0] + dirX == self.height - 1) and self.pos[dest[0] + dirX][dest[1] + dirY][P_COL] == 0) or ((dest[0] + dirX == 0) and self.pos[dest[0] + dirX][dest[1] + dirY][P_COL] == 1):
                                print "King me!"
                                self.pos[dest[0] + dirX][dest[1] + dirY][P_KING] = True
                else:
                    print "moving..."
                    self.pos[dest[0]][dest[1]] = self.pos[originX][originY]
                    self.pos[originX][originY] = None
                    #Move piece
                    if ((dest[0] == self.height - 1) and self.pos[dest[0]][dest[1]][P_COL] == 0) or ((dest[0] == 0) and self.pos[dest[0] + dirX][dest[1] + dirY][P_COL] == 1):
                        print "King me!"
                        self.pos[dest[0] + dirX][dest[1] + dirY][P_KING] = True
            else:
                print "You can't move in that direction!"
        else:
            print "Origin must be an existing piece"
                            
        
    #print board
    def Draw(self):
        print "\n"
        for row in range(len(self.pos) - 1, -1, -1):
            print row,
            for space in range(len(self.pos[row])):
                if self.pos[row][space] != None:
                    if self.pos[row][space][P_COL] == 0:
                        print "O",
                    else:
                        print "X",
                else:
                    print "·",
            print "\n",
            if row == 0:
                print "|",
                for space in range(len(self.pos[row])):
                    print space,
                print "\n"

          
    def GetStats(self, flipped):
        statList = []
        
        if flipped == True:
            order = -1
        else:
            order = 1
            
        for row in range(len(self.pos)):
            for space in range(len(self.pos[row])):
                
                mode = row % 2
                
                if space % 2 != mode:
                    
                    if self.pos[row][space] == None:
                        statList.append(0)
                        
                    else:

                        if self.pos[row][space][P_COL] == 0:
                            if self.pos[row][space][P_KING] == True:
                                statList.append(-3 * order)
                            else:
                                statList.append(-1 * order)
                        else:
                            if self.pos[row][space][P_KING] == True:
                                statList.append(3 * order)
                            else:
                                statList.append(1 * order)
        return statList
                            

    
board = NewBoard(8, 8)
board.Draw()
