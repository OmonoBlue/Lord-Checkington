import math
import os
import importlib
importlib.import_module('Functions')
from Functions import Weight_Puller, maths, NetworkRecorder, dataSetOrganizer, converter, Learning_algorithm

def neuralNetworkLearning(values,gameEnd,moveNum):


    for layer in range (len(nodes)-1):
        for node in range (len(nodesList[layer])) :
            for i in range(len(weights[layer][node])):
                nodesList[layer+1][i] += (float(nodesList[layer][node]) * float(weights[layer][node][i]))
    
    if gameEnd == False:
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
        return 




        
    if gameEnd == True:
        game += 1
        errorTot = maths.errorSum(error)
        errorGradList = maths.errorGrad(errorTot, weights)
        weights = maths.weightDiff(errorGradList, weights)
        
        NetworkRecorder.networkRecorder(weights,nodes,game)        
        

def neuralNetInit():
    

    (weights, nodes, game) = Weight_Puller.weightPuller()
    nodesList = [None] * len(nodes)
    print len(nodes)
    

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

neuralNetworkLearning(list1,False,0)

