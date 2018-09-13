
import math
import os

#some stuff to make code better and ez reads
P_COL = 0
P_KING = 1

UP = 1
DOWN = -1
LEFT = -1
RIGHT = 1


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
                    
                if space % 2 == mode:

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
                if space % 2 == mode:
                    self.pos[row][space] = (1, False)
                    totalb -= 1
            
            if totalb < 1:
                break

    def Move(self, originY, originX, dirY, dirX): #dirX stands for direction row, dirY stands for direction space (y and x respectively)
        if abs(dirX) != 1 or abs(dirY) != 1:
            print "Can only move 1 space in each direction!"
            return False
        dest = (originX + dirX,originY + dirY)
        
        if self.pos[originX][originY] != None: #Check if a playable piece has been selected
            
            #Check if playable piece is moveable in chosen direction
            if (self.pos[originX][originY][P_COL] == 0 and dirX == 1) or (self.pos[originX][originY][P_COL] == 1 and dirX == -1) or self.pos[originX][originY][P_KING] == True:
                
                if (dest[0] > self.width - 1 or dest[0] < 0) or (dest[1] > self.height - 1 or dest[1] < 0): #check if the piece is going to move out of bounds
                    print "can't move, piece out of bounds"
                    return False
                elif self.pos[dest[0]][dest[1]] != None: #if the destination is not clear...
                    print "destination blocked..."
                    if self.pos[dest[0]][dest[1]][P_COL] == self.pos[originX][originY][P_COL]: #check if the space is occupied by your own colour
                        print "can't move, piece occupied by own colour"
                        return False
                    else: #If piece is enemy color...
                        if self.pos[dest[0] + dirX][dest[1] + dirY] != None: #check if piece is capturable
                            print "can't move, capture blocked"
                            return False
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
                return False
        else:
            print "Origin must be an existing piece"
            return False
                            
        
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
                
                if space % 2 == mode:
                    
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
                            

    
board = NewBoard(8, 8) #Create the standard 8 by 8 board
done = False

# Turn handling woo!
while not done:
    
    print "\n" * 100 # clear screen
    board.Draw() #draw board

    #prompt appropriate player to select a piece to move
    if board.turn == 0:
        print "\nIt is white's turn. What piece do you want to move? (x y)"
    else:
        print "\nIt is black's turn. What piece do you want to move? (x y)"

    # this loop will keep running until the player makes a valid move
    while True: 
        
        pMove = [0, 0, 0, 0] # variable used to store player's move
        
        try:
            
            origin = map(int, raw_input("Piece Coordinate: ").split()) #Prompt player for origin piece coordinate
            
            if board.pos[origin[1]][origin[0]][P_COL] != board.turn:
                print "You can't move that piece, it's not yours!"
                continue
            else:
                pMove[0] = origin[0]
                pMove[1] = origin[1]
                print pMove

                
        except:
            print "Err! Please enter a valid x coordinate and y coordinate seperated by a space"
            continue

        print "\nWhat direction do you want to move? UP/DOWN LEFT/RIGHT)"
    
        try:
            direction = map(str, raw_input("Destination: ").lower().split())
            print direction
            if direction[0] == "up":
                pMove[2] = UP
            elif direction[0] == "down":
                pMove[2] = DOWN
            else:
                print "Please enter a valid direction for the first argument"
                continue

            if direction[1] == "left":
                pMove[3] = LEFT
            elif direction[1] == "right":
                pMove[3] = RIGHT
            else:
                print "Please enter a valid direction for the second argument"
                continue
        except:
            print "Error NANI! Please enter y direction (up/down) and x direction (left/right) seperated by a space"

        if board.Move(pMove[0], pMove[1], pMove[3], pMove[2]) == False:
            continue
        else:
            board.turn = (board.turn - 1) * -1
            break
            


