
import os
import importlib
import board
import MainNetwork



weights, nodes, nodesList, actual, moves, gameNum = MainNetwork.neuralNetInit()
error = []
move = []
gameAmount = int(raw_input("How many games will you simulate?\nGame amount: "))


for i in range (gameAmount):
    Game = board.NewBoard(8, 8)
    looping = True

    print "Simulating game number", gameNum
    print "Gamelength:", len(moves[gameNum]), "\n"
    
    while looping == True:
        if Game.CheckGameEnd() == True or Game.gameOver == True or len(moves[gameNum]) == Game.moveNum: 
            looping = False
##        print "the move is " + str(Game.moveNum)
        
##        print Game.GetStats(False)
##        print Game.GetStats(True)
        if Game.turn == 0:
            if Game.CheckGameEnd() == False:
                try:
                    error, move = MainNetwork.neuralNetworkLearning(Game.GetStats(False), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)
                except IndexError:
                    Game.gameOver = True
                    weights = MainNetwork.neuralNetworkLearning(Game.GetStats(False), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)

            if Game.CheckGameEnd() == True or Game.gameOver == True:
                weights = MainNetwork.neuralNetworkLearning(Game.GetStats(False), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)

        if Game.turn == 1:
            if Game.CheckGameEnd() == False:
                try:
                    error, move = MainNetwork.neuralNetworkLearning(Game.GetStats(True), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)
                except IndexError:
                    Game.gameOver = True
                    weights = MainNetwork.neuralNetworkLearning(Game.GetStats(True), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)
                    


                #move[i][0] = (move[i][0]-7) *-1
                #move[i][1] = (move[i][1]-7) *-1
                

            if Game.CheckGameEnd() == True or Game.gameOver == True:
                weights = MainNetwork.neuralNetworkLearning(Game.GetStats(True), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)

        

        if len(move) > 2:
            multiHop = True
        else:
            multiHop = False

        
        if multiHop:
            destList = []
            for dest in range(1, len(move)):
                destList.append([move[dest][0], move[dest][1]])
            Game.Move((move[0][0], move[0][1]), destList)
            
        else:
            Game.Move((move[0][0], move[0][1]), (move[1][0], move[1][1]))

##        Game.Draw()
    
    print "game", gameNum, "completed!\n"
    gameNum += 1

