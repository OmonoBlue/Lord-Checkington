import random
import Player1Board as board
import copy

Game = board.NewBoard(8, 8)
startBoard = [['  X ', 'R01P', '  X ', 'R03P', '  X ', 'R05P', '  X ', 'R07P'],
              ['R10P', '  X ', 'R12P', '  X ', 'R14P', '  X ', 'R16P', '  X '],
              ['  X ', 'R21P', '  X ', 'R23P', '  X ', 'R25P', '  X ', 'R27P'],
              ['    ', '  X ', '    ', '  X ', '    ', '  X ', '    ', '  X '],
              ['  X ', '    ', '  X ', '    ', '  X ', '    ', '  X ', '    '],
              ['B50P', '  X ', 'B52P', '  X ', 'B54P', '  X ', 'B56P', '  X '],
              ['  X ', 'B61P', '  X ', 'B63P', '  X ', 'B65P', '  X ', 'B67P'],
              ['B70P', '  X ', 'B72P', '  X ', 'B74P', '  X ', 'B76P', '  X ']]

testBoard = [['  X ', 'R01P', '  X ', 'R03P', '  X ', 'R05P', '  X ', 'R07P'],
            ['R10P', '  X ', 'R12P', '  X ', 'R14P', '  X ', 'R16P', '  X '],
            ['  X ', 'B21P', '  X ', '    ', '  X ', 'R25P', '  X ', 'R27P'],
            ['    ', '  X ', '    ', '  X ', 'R34P', '  X ', 'B36P', '  X '],
            ['  X ', 'B41P', '  X ', 'B52P', '  X ', '    ', '  X ', '    '],
            ['B50P', '  X ', '    ', '  X ', 'B54P', '  X ', 'R46P', '  X '],
            ['  X ', 'B61P', '  X ', '    ', '  X ', 'B65P', '  X ', 'B67P'],
            ['B70P', '  X ', 'B72P', '  X ', '    ', '  X ', 'B76P', '  X ']]

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

    if len(starterMoves) == 0:
        return ["no","M00V"]



    #return starterMoves
    
    # Draw the MillerBoard
    #millerDraw(givenBoard)
        

    # If moves are captures, choose the largest capture chain possible
    if movesAreCaps:
        maxMove = []
        goodMoves = []
        for move in starterMoves:
            if len(move) > len(maxMove):
                maxMove = move
            elif len(move) == len(maxMove):
                if len(goodMoves) == 0:
                    goodMoves.append(maxMove)
                goodMoves.append(move)

        if len(goodMoves) == 0:
            moveChoice = maxMove

        elif len(goodMoves) == 1:
            moveChoice = goodMoves[0]

        else:
            # If there are multiple hops of the same length, choose the one with the least repercussions

            moveOverallPointValues = []
            
            for move in goodMoves:

                tmpDestList  = []

                for dest in range(1, len(move)):
                    tmpDestList.append(move[dest])
                
                tmpBoard = copy.deepcopy(Game)
                #print tmpDestList
                tmpBoard.Move(move[0], tmpDestList)
                #tmpBoard.Draw()

                enemyMoveList, enemyCanCap = tmpBoard.GetValidMoves((moveCol - 1) * -1)
                
                currentMovePointValue = 0

                # Loop through every possible enemy move, add the point value that the board returns from the enemy doing that move.
                
                for enemyMove in enemyMoveList:

                    enemyDestList = []

                    for dest in range(1, len(enemyMove)):
                        enemyDestList.append(enemyMove[dest])
                    
                    tmpEnemyBoard = copy.deepcopy(tmpBoard)
                    #print enemyDestList

                    if len(enemyDestList) == 1:
                        tmpEnemyBoard.Move(enemyMove[0], enemyDestList[0])
                    else:
                        tmpEnemyBoard.Move(enemyMove[0], enemyDestList)
                        
                    currentMovePointValue += tmpEnemyBoard.GetStats(millerCols[moveCol])

                    del tmpEnemyBoard

                if len(enemyMoveList) == 0:
                    print "Checkmate boiiii"
                    currentMovePointValue = 9999
                else:
                    currentMovePointValue /= len(enemyMoveList)
                
                moveOverallPointValues.append(currentMovePointValue)

                del tmpBoard
                

            bestMoves = []
            bestMovePointValue = max(moveOverallPointValues)
            bestMoveIndex = moveOverallPointValues.index(bestMovePointValue)

            bestMoves.append(goodMoves[bestMoveIndex])
            
            for move in range(len(goodMoves)):

                if move != bestMoveIndex and moveOverallPointValues[move] == bestMovePointValue:
                    bestMoves.append(goodMoves[move])

            moveChoice = bestMoves[random.randint(0, len(bestMoves) - 1)]

        
    else: # If the moves are not captures...

        
        # We are going to start by trying to avoid capture as much as possible
        
        capAvoidable = False
        capAvoidingMoveIndexes = []

        # Run through the board and check if there are any moves that can avoid a capture
        for move in range(len(starterMoves)):
            
            tmpBoard = copy.deepcopy(Game)
            tmpBoard.Move(starterMoves[move][0], starterMoves[move][1])
            
            enemyMoveList, enemyCanCap = tmpBoard.GetValidMoves((moveCol - 1) * -1)

            if enemyCanCap == False:
                capAvoidable = True
                capAvoidingMoveIndexes.append(move)

            del tmpBoard

        goodMoves = []

        # If a capture is avoidable, add the avoiding captures to our "goodMoves" list
        
        if capAvoidable:
            for capAvoidMove in capAvoidingMoveIndexes:
                goodMoves.append(starterMoves[capAvoidMove])

        else: # If the capture is not avoidable...

            # We have to choose the move that does the most damage control (Highest point value possible for our favor)
            
            moveOverallPointValues = []

            # Loop through each possible move again
            for move in range(len(starterMoves)):

                tmpBoard = copy.deepcopy(Game)
                tmpBoard.Move(starterMoves[move][0], starterMoves[move][1])

                # Get possible enemy moves from new position
                enemyMoveList, enemyCanCap = tmpBoard.GetValidMoves((moveCol - 1) * -1)

                currentMovePointValue = 0

                # Loop through every possible enemy move, add the point value that the board returns from the enemy doing that move.
                
                for enemyMove in enemyMoveList:

                    enemyDestList = []

                    for dest in range(1, len(enemyMoveList)):
                        enemyDestList.append(dest)
                    
                    tmpEnemyBoard = copy.deepcopy(tmpBoard)
                    tmpEnemyBoard.Move(enemyMove[0], enemyDestList)
                    currentMovePointValue += tmpEnemyBoard.GetStats(millerCols[moveCol])

                    del tmpEnemyBoard

                if len(enemyMoveList) == 0:
                    print "Checkmate boiiii"
                    currentMovePointValue = 9999
                else:
                    currentMovePointValue /= len(enemyMoveList)
                
                moveOverallPointValues.append(currentMovePointValue)

                del tmpBoard

            
            bestMovePointValue = max(moveOverallPointValues)
            bestMoveIndex = moveOverallPointValues.index(bestMovePointValue)

            goodMoves.append(starterMoves[bestMoveIndex])
            
            for move in range(len(starterMoves)):

                if move != bestMoveIndex and moveOverallPointValues[move] == bestMovePointValue:
                    goodMoves.append(starterMoves[move])

        if len(goodMoves) > 0:
            moveChoice = goodMoves[random.randint(0, len(goodMoves) - 1)]
        else:
            moveChoice = starterMoves[random.randint(0, len(starterMoves) - 1)]

    #Start assembling the final move
    finalCol = millerCols[Game.pos[moveChoice[0][0]][moveChoice[0][1]][board.P_COL]]
    finalPiece = millerPiece[Game.pos[moveChoice[0][0]][moveChoice[0][1]][board.P_KING]]

    #print moveChoice
    #print starterMoves
    #Reverse co-ordinare to account for Millerboard
    
    for cor in moveChoice:
        cor[1] = (cor[1] - 7) * -1

    #print moveChoice

    #Begin final formatting of move
    finalResult = [finalCol + str(moveChoice[0][1]) + str(moveChoice[0][0]) + finalPiece]

    #Add destinations to final move
    for dest in range(1, len(moveChoice)):
        finalResult.append(str(moveChoice[dest][1]) + str(moveChoice[dest][0]))

    #print "Game value is", Game.GetStats(givenCol), "for", givenCol
    return finalResult
