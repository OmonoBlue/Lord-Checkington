
import math
import os
import pickle
from pygame import *

#some stuff to make code better and ez reads
P_COL = 0
P_KING = 1

UP = 1
DOWN = -1
LEFT = -1
RIGHT = 1

SPACE_ABC = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    }


class NewBoard():

    # Initial Setup
    def __init__(self, width, height):

        # Setup empty board
        self.pos = [None] * width
        for column in range(len(self.pos)):
            self.pos[column] = [None] * height

        self.width = width
        self.height = height

        self.turn = 0
        # Setup pieces

        # total pieces remaining for each color
        totalw = round(((height - 2) * width) / 4)
        totalb = totalw
        
        for row in range(height):
            # check if row is odd number or even number. Will help arrange board layout.
            mode = row % 2

            # odd row, put pieces on odd spaces. even row, put pieces on even spaces.
            for space in range(width):
                    
                if space % 2 == mode:

                    #pieces are set up like this: self.pos[row][space](color {0 = white / 1 = black}, king {True/False})
                    self.pos[space][row] = [0, False]
                    totalw -= 1


        #break if there are no more pieces left to place
            if totalw < 1:
                break

            
        #doing same thing, but for black pieces 
        for row in range(height -1, -1, -1):

            mode = row % 2
            
            for space in range(width -1, -1, -1):
                if space % 2 == mode:
                    self.pos[space][row] = (1, False)
                    totalb -= 1
            
            if totalb < 1:
                break
    
    def CheckMove(self, oriCor, direction):
        
        origin = self.pos[oriCor[0]][oriCor[1]]
        destination = self.pos[oriCor[0] + direction[0]][oriCor[1] + direction[1]]

        #Check if there is a moveable piece
        if origin == None:
            print "No piece in origin"
            return False
        
        elif ((origin[P_COL] == 0 and direction[1] <= -1) or (origin[P_COL] == 1 and direction[1] >= 1)) and origin[P_KING] == False:
            print "Can't move in that direction"
            return False

        elif destination != None:
            if destination[P_COL] == origin[P_COL]:
                print "Can't capture own colour!"
                return False
            elif (oriCor[0] + direction[0] * 2 > self.width + 1) or (oriCor[1] + direction[1] * 2  > self.height + 1) or (oriCor[0] + direction[0] * 2 < 0) or (oriCor[1] + direction[1] * 2  < 0):
                print "Can't go out of bounds!"
                return False
                
            elif self.pos[oriCor[0] + direction[0] * 2][oriCor[1] + direction[1] * 2] != None:
                print "Capture Blocked"
                return False
            else:
                print "Capture Possible"
                return "Capture"
        else:
            return True

        
    def Move(self, origin, moveList):         
        if isinstance(origin, tuple) and len(origin) == 2:

            if isinstance(moveList, tuple):

                if len(moveList) == 2:
                    if isinstance(moveList[0], tuple):
                        isSingleMove = False
                    else:
                        isSingleMove = True
                elif len(moveList) < 2:
                    print "Error! Move must be either one or multiple co-ordinates!"
                    return
                else:
                    isSingleMove = False
            else:
                print "Error! Move must be a list!"
                return
        else:
            print "Error, origin must be a co-ordiante"
            return

        print "isSingleMove:", isSingleMove
        if isSingleMove:
            direction = ( (moveList[0] - origin[0]) / abs(moveList[0] - origin[0]) , (moveList[1] - origin[1]) / abs(moveList[1] - origin[1]) )

            print "direction", direction
            if self.CheckMove(origin, direction):
                self.pos[moveList[0]][moveList[1]] = self.pos[origin[0]][origin[1]]
                self.pos[origin[0]][origin[1]] = None
            elif self.CheckMove(origin, direction) == False:
                print "Can't move there!"
                return
            else:
                self.pos[moveList[0] + direction[0] * 2][moveList[1] + direction[1] *2] = self.pos[origin[0]][origin[1]]
                self.pos[moveList[0] + direction[0]][moveList[1] + direction[1]] = None
                self.pos[origin[0]][origin[1]] = None
        else:
            newOrigin = origin
            for move in moveList:
                direction = ( (move[0] - newOrigin[0]) / abs(move[0] - newOrigin[0]) , (move[1] - newOrigin[1]) / abs(move[1] - newOrigin[1]) )
                if self.CheckMove(newOrigin, direction) == "Capture":
                    self.pos[move[0]][move[1]] = self.pos[newOrigin[0]][newOrigin[1]]
                    self.pos[move[0] - direction[0]][move[1] - direction[1]] = None
                    self.pos[newOrigin[0]][newOrigin[1]] = None
                    newOrigin = (move[0], move[1])

                else:
                    print "Can't preform move: " + str(newOrigin) + "to " + str(move) + " Ending here..."
                    return

                
        
    #print board
    def Draw(self, highlight = None):
        if highlight != None:
            if type(highlight) == list or type(highlight) == tuple:
                highlightSpace = highlight
            else:
                print "Error! Highlight has to be a coordinate"
                highlightSpace = None
        else:
            highlightSpace = None

        
        for row in range(self.height -1, -1, -1):
            print row,
            
            for space in range(self.width):
                
                if self.pos[space][row] != None:
                    if self.pos[space][row][P_COL] == 0:
                        if highlightSpace != None and self.pos[space][row] == highlightSpace:
                            print "[o]",
                        else:
                            print "O",
                    elif self.pos[space][row][P_COL] == 1:
                        if highlightSpace != None and self.pos[space][row] == highlightSpace:
                            print "[x]",
                        else:
                            print "X",
                else:
                    print "-",
            print ""

        print " ",
        for num in range(len(SPACE_ABC)):
            print SPACE_ABC[num],
            
          
    def GetStats(self, flipped):
        statList = []
        
        if flipped == True:
            order = -1
        else:
            order = 1
            
        for row in range(len(self.pos)):
            for space in range(len(self.pos[row]) - 1, -1 ,-1):
                
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

    @staticmethod
    def Save(board, filename = None):
        if filename == None:
            name = board.Name
        else:
            name = filename
        savefile = open(os.path.join('BoardSaves', name), 'w')
        pickle.dump(board, savefile)
        savefile.close()
        

    @staticmethod
    def Load(filename):
        savefile = open(os.path.join('BoardSaves', filename), 'r')
        newBoard = pickle.load(savefile)
        savefile.close()
        return newBoard

    

    
board = NewBoard.Load("Board Test 2.bin") #Create the standard 8 by 8 board
done = False


board.Draw()

# Turn handling woo!
##while not done:
##    
##    print "\n" * 100 # clear screen
##    print board.GetStats(False)
##    board.Draw() #draw board
##
##    #prompt appropriate player to select a piece to move
##    if board.turn == 0:
##        print "\nIt is white's turn. What piece do you want to move? (x y)"
##    else:
##        print "\nIt is black's turn. What piece do you want to move? (x y)"
##
##    # this loop will keep running until the player makes a valid move
##    while True: 
##        
##        pMove = [0, 0, 0, 0] # variable used to store player's move
##        
##        try:
##            
##            origin = map(int, raw_input("Piece Coordinate: ").split()) #Prompt player for origin piece coordinate
##            
##            if board.pos[origin[1]][origin[0]][P_COL] != board.turn:
##                print "You can't move that piece, it's not yours!"
##                continue
##            else:
##                pMove[0] = origin[0]
##                pMove[1] = origin[1]
##                print pMove
##
##                
##        except:
##            print "Err! Please enter a valid x coordinate and y coordinate seperated by a space"
##            continue
##
##        print "\nWhat direction do you want to move? UP/DOWN LEFT/RIGHT)"
##    
##        try:
##            direction = map(str, raw_input("Destination: ").lower().split())
##            print direction
##            if direction[0] == "up":
##                pMove[2] = UP
##            elif direction[0] == "down":
##                pMove[2] = DOWN
##            else:
##                print "Please enter a valid direction for the first argument"
##                continue
##
##            if direction[1] == "left":
##                pMove[3] = LEFT
##            elif direction[1] == "right":
##                pMove[3] = RIGHT
##            else:
##                print "Please enter a valid direction for the second argument"
##                continue
##        except:
##            print "Error NANI! Please enter y direction (up/down) and x direction (left/right) seperated by a space"
##
##        if board.Move(pMove[0], pMove[1], pMove[3], pMove[2]) == False:
##            continue
##        else:
##            board.turn = (board.turn - 1) * -1
##            break
##            
##
