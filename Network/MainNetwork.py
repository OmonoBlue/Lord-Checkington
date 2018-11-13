import math
import os
import importlib
importlib.import_module('Functions')
from Functions import Weight_Puller, maths, NetworkRecorder, dataSetOrganizer, converter, Learning_algorithm

def neuralNetworkLearning(values,gameEnd,moveNum,nodes,nodesList,weights,actual,moves,game,error):

    
    
    
    if gameEnd == False:
        nodesList[0] = values
        for layer in range (len(nodes)-1):
            for node in range (len(nodesList[layer])) :
                for i in range(len(weights[layer][node])):
                    nodesList[layer+1][i] += (float(nodesList[layer][node]) * float(weights[layer][node][i]))

        currentMove = moves[game][moveNum][0]
        currentMove = [currentMove[0], converter.spaceToDir(currentMove[0], currentMove[1])]
        dirValue = 0
        if currentMove[1][0] == 1 :
            if currentMove[1][1] == 1:
                dirValue = 0
            if currentMove[1][1] == -1:
                dirValue = 1

        if currentMove[1][0] == -1:
            if currentMove[1][1] == 1:
                dirValue = 2
            if currentMove[1][1] == -1:
                dirValue = 3
        correctMoveNode = ((int(currentMove[0]) - 1) * 4) + int(dirValue)

        error.append(Learning_algorithm.errorIndiv(nodesList[len(nodes)-1],correctMoveNode))
        for i in range (len(moves[game][moveNum][1])):
##            print moves[game][moveNum][1][i]
            try:
                moves[game][moveNum][1][i] = converter.numToCor(moves[game][moveNum][1][i])
            except (TypeError):
                pass
        return error, moves[game][moveNum][1]




        
    if gameEnd == True:
        game += 1
        weights = Learning_algorithm.hiddenError(nodesList,weights,error)
        
        NetworkRecorder.networkRecorder(weights,nodes,game)
        error = []
        return weights
        

def neuralNetInit():
    

    (weights, nodes, game) = Weight_Puller.weightPuller()
    nodesList = [None] * len(nodes)
    

    for i in range(1,len(nodes)):
        nodesList[i] = [None] * nodes[i]
        for a in range(nodes[i]):
            nodesList[i][a] = 0

    for i in range (len(nodesList[len(nodes)-1])):
        nodesList[len(nodes)-1][i] = maths.sigmoid(nodesList[len(nodes)-1][i])

    actual = [0] * 128
    
    moves = dataSetOrganizer.dataSetOrgan()

    return weights, nodes, nodesList, actual, moves, game
    
                               

list1 = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]



