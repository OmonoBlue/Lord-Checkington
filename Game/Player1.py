import random
import board

Game = board.NewBoard(8, 8)

testBoard = [['  X ', 'R01P', '  X ', 'R03P', '  X ', 'R05P', '  X ', 'R07P'],
            ['R10P', '  X ', 'R12P', '  X ', 'R14P', '  X ', 'R16P', '  X '],
            ['  X ', 'R21P', '  X ', '    ', '  X ', 'R25P', '  X ', 'R27P'],
            ['    ', '  X ', '    ', '  X ', 'R23P', '  X ', 'B36P', '  X '],
            ['  X ', '    ', '  X ', 'B52P', '  X ', '    ', '  X ', '    '],
            ['B50P', '  X ', '    ', '  X ', 'B54P', '  X ', '    ', '  X '],
            ['  X ', 'B61P', '  X ', 'B63P', '  X ', 'B65P', '  X ', 'B67P'],
            ['    ', '  X ', 'B72P', '  X ', '    ', '  X ', 'B76P', '  X ']]

millerCols = {0 : "B",
              1 : "R"}

millerPiece = {True : "K",
               False : "P"}

def millerDraw(givenBoard):
    for x in range(len(givenBoard)) :
        print "|",
        for y in range(len(givenBoard[x])) :
                print givenBoard[x][y] + " |" ,
        print ""
        
def main(givenBoard, givenCol):

    Game.Miller2Board(givenBoard)
    
    # Un-stupify variables
    if givenCol == "B":
        moveCol = 0
    elif givenCol == "R":
        moveCol = 1
    else:
        raise Exception("Given move colour is not as expected")

    Game.turn = moveCol

    # Get some baseline available moves
    starterMoves, movesAreCaps = Game.GetValidMoves(moveCol)

    #return starterMoves
    
    # Draw the MillerBoard
    #millerDraw(givenBoard)
        
    
    if movesAreCaps:
        maxMove = []
        for move in starterMoves:
            if len(move) > len(maxMove):
                maxMove = move

        moveChoice = maxMove
    else: 
        moveChoice = starterMoves[random.randint(0, len(starterMoves) - 1)]

    #Start assembling the final move
    finalCol = millerCols[Game.pos[moveChoice[0][0]][moveChoice[0][1]][board.P_COL]]
    finalPiece = millerPiece[Game.pos[moveChoice[0][0]][moveChoice[0][1]][board.P_KING]]

    #Reverse co-ordinare to account for Millerboard
    #print moveChoice
    for cor in moveChoice:
        cor[1] = (cor[1] - 7) * -1

    #print moveChoice

    #Begin final formatting of move
    finalResult = [finalCol + str(moveChoice[0][1]) + str(moveChoice[0][0]) + finalPiece]

    #Add destinations to final move
    for dest in range(1, len(moveChoice)):
        finalResult.append(str(moveChoice[dest][1]) + str(moveChoice[dest][0]))

    return finalResult

    

    

print main(testBoard, "R")


    
