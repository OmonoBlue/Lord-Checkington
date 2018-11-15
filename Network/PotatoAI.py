import random
import board

Game = board.NewBoard(8, 8)

testBoard = [['  X ', 'R01P', '  X ', 'R03P', '  X ', 'R05P', '  X ', 'R07P'],
            ['R10P', '  X ', 'R12P', '  X ', 'R14P', '  X ', 'R16P', '  X '],
            ['  X ', 'R21P', '  X ', '    ', '  X ', 'R25P', '  X ', 'R27P'],
            ['    ', '  X ', '    ', '  X ', 'R23P', '  X ', '    ', '  X '],
            ['  X ', '    ', '  X ', 'B52P', '  X ', '    ', '  X ', '    '],
            ['B50P', '  X ', '    ', '  X ', 'B54P', '  X ', 'B56P', '  X '],
            ['  X ', 'B61P', '  X ', 'B63P', '  X ', 'B65P', '  X ', 'B67P'],
            ['B70P', '  X ', 'B72P', '  X ', 'B74P', '  X ', 'B76P', '  X ']]

millerCols = {0 : "B",
              1 : "R"}

millerPiece = {True : "K",
               False : "P"}

def main(givenBoard, givenCol):

    Game.Miller2Board(givenBoard)
    
    # Un-stupify variables
    if givenCol == "B":
        moveCol = 0
    elif givenCol == "R":
        moveCol = 1
    else:
        raise Exception("Given move colour is not as expected")

    # Get some baseline available moves
    starterMoves, moveType = Game.GetValidMoves(moveCol)

    # Draw the MillerBoard
    for x in range(len(givenBoard)) :
        print "|",
        for y in range(len(givenBoard[x])) :
                print givenBoard[x][y] + " |" ,
        print ""
        
    

    moveChoice = starterMoves[random.randint(0, len(starterMoves) - 1)]

    #Reverse co-ordinare to account for Millerboard

    print moveChoice
    for cor in range(len(moveChoice)):
        moveChoice[cor][1] = (moveChoice[cor][1] - 7) * -1
        print moveChoice[cor]

    for move in starterMoves:
        for cor in move:
            cor[1] = (cor[1] - 7) * -1

            
    return moveChoice

    

    

print main(testBoard, "R")


    
