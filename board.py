
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

    def Move(self, origin, dr, ds): #dr stands for direction row, ds stands for direction space (y and x respectively)
        if abs(dr) != 1 or abs(ds) != 1:
            print "Can only move 1 space in each direction!"
        dest = (origin[0] + dr,origin[1] + ds)
        print dest, "is the destination"
        
        print self.pos[origin[0]][origin[1]], "has been selected"
        
        if self.pos[origin[0]][origin[1]] != None: #Check if a playable piece has been selected
            print "piece detected"
            
            #Check if playable piece is moveable in chosen direction
            if (self.pos[origin[0]][origin[1]][P_COL] == 0 and dr == 1) or (self.pos[origin[0]][origin[1]][P_COL] == 1 and dr == -1) or self.pos[origin[0]][origin[1]][P_KING] == True:
                
                if (dest[0] > self.width - 1 or dest[0] < 0) or (dest[1] > self.height - 1 or dest[1] < 0): #check if the piece is going to move out of bounds
                    print "can't move, piece out of bounds"
                elif self.pos[dest[0]][dest[1]] != None: #if the destination is not clear...
                    print "destination blocked..."
                    if self.pos[dest[0]][dest[1]][P_COL] == self.pos[origin[0]][origin[1]][P_COL]: #check if the space is occupied by your own colour
                        print "can't move, piece occupied by own colour"
                    else: #If piece is enemy color...
                        if self.pos[dest[0] + dr][dest[1] + ds] != None: #check if piece is capturable
                            print "can't move, capture blocked"
                        else:
                            #Capture piece
                            print "capturing..."
                            self.pos[dest[0] + dr][dest[1] + ds] = self.pos[origin[0]][origin[1]]
                            self.pos[dest[0]][dest[1]] = None
                            self.pos[origin[0]][origin[1]] = None
                else:
                    print "moving..."
                    self.pos[dest[0]][dest[1]] = self.pos[origin[0]][origin[1]]
                    self.pos[origin[0]][origin[1]] = None
                    #Move piece
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

    def GetStats(self):
        statList = []
        for row in range(len(self.pos)):
            for space in range(len(self.pos[row])):
                
                mode = row % 2
                
                if space % 2 != mode:
                    
                    if self.pos[row][space] == None:
                        statList.append(0)
                        
                    else:
                        if self.pos[row][space][P_COL] == 0:
                            if self.pos[row][space][P_KING] == True:
                                statList.append(-3)
                            else:
                                statList.append(-1)
                        else:
                            if self.pos[row][space][P_KING] == True:
                                statList.append(3)
                            else:
                                statList.append(1)
        return statList
                            

    
board = NewBoard(8, 8)
board.Draw()
