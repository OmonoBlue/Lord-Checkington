
import os
import importlib
import board
import MainNetwork



weights, nodes, nodesList, actual, moves, gameNum = MainNetwork.neuralNetInit()
error = []
move = []
gameAmount = int(raw_input("How many games will you simulate?"))


for i in range (gameAmount):
    Game = board.NewBoard(8, 8)
    looping = True

    while looping == True:
        if Game.CheckGameEnd() == False:
            looping = False

        if Game.turn == 0:
            if Game.CheckGameEnd() == False:
                error, move = MainNetwork.neuralNetworkLearning(Game.GetStats(False), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)

            print move
            if Game.CheckGameEnd() == True:
                weights = MainNetwork.neuralNetworkLearning(Game.GetStats(False), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)

        if Game.turn == 1:
            if Game.CheckGameEnd() == False:
                error, move = MainNetwork.neuralNetworkLearning(Game.GetStats(True), Game.gameOver, Game.moveNum, nodes, nodesList, weights, actual, moves, gameNum,error)

                for i in range (len(move)):
                    move[i][0] = (move[i][0]-7) *-1
                    move[i][1] = (move[i][1]-7) *-1
                
            print move
            if Game.CheckGameEnd() == True:
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

        Game.Move((move[0][0], move[0][1]), (move[1][0], move[1][1]))



        #Game.Draw()
