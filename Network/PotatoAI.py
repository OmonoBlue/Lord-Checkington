import random
import board

Game = board.NewBoard(8, 8)

testList = [['  X ', 'R01P', '  X ', 'R03P', '  X ', 'R05P', '  X ', 'R07P'],
            ['R10P', '  X ', 'R12P', '  X ', 'R14P', '  X ', 'R16P', '  X '],
            ['  X ', 'R21P', '  X ', 'R23P', '  X ', 'R25P', '  X ', 'R27P'],
            ['    ', '  X ', '    ', '  X ', '    ', '  X ', '    ', '  X '],
            ['  X ', '    ', '  X ', '    ', '  X ', '    ', '  X ', '    '],
            ['B50P', '  X ', 'B52P', '  X ', 'B54P', '  X ', 'B56P', '  X '],
            ['  X ', 'B61P', '  X ', 'B63P', '  X ', 'B65P', '  X ', 'B67P'],
            ['B70P', '  X ', 'B72P', '  X ', 'B74P', '  X ', 'B76P', '  X ']]

millerCols = {0 : "B",
              1 : "R"}

millerPiece = {True : "K",
               False : "P"}

def main(givenBoard, givenCol):

    if givenCol == "B":
        moveCol = 0
    elif givenCol == "R":
        moveCol = 1
    else:
        raise Exception("Given move colour is not as expected")


    for x in range(len(givenBoard)) :
        print "|",
        for y in range(len(givenBoard[x])) :
                print givenBoard[x][y] + " |" ,
        print ""
        
    Game.Miller2Board(givenBoard)
    availableMoves, moveType = Game.GetValidMoves(moveCol)

    moveChoice = availableMoves[random.randint(0, len(availableMoves))]

    return [str(millerCols[str(givenCol)]) + str(moveChoice[0][0]) + str(moveChoice[0][1]) + str(millerPiece[str(Game.pos[moveChoice[0][0]][moveChoice[0][1]][Game.P_KING])]),
            str(moveChoice[1][0]) + str(moveChoice[1][1])]

    

    

main(testList, "B")


    
