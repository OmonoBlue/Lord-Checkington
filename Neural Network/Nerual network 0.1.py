import math
import os
import importlib
importlib.import_module('Functions')
from Functions import Weight_Puller, maths, NetworkRecorder, dataSetOrganizer, converter 

def neuralNetworkLearning(values,gameEnd, moveNum):
    weights = []
    nodes = []
    

    (weights, nodes, games) = Weight_Puller.weightPuller()
    nodesList = [None] * len(nodes)
    

    nodesList[0] = values
    for i in range(1,len(nodes)):
        nodesList[i] = [None] * nodes[i]
        for a in range(nodes[i]):
            nodesList[i][a] = 0
    for layer in range (len(nodes)-1):
        for node in range (len(nodesList[layer])) :
            for i in range(len(weights[layer][node])):
                nodesList[layer+1][i] += (float(nodesList[layer][node]) * float(weights[layer][node][i]))

    for i in range (len(nodesList[len(nodes)-1])):
        nodesList[len(nodes)-1][i] = maths.sigmoid(nodesList[len(nodes)-1][i])

    actual = [0] * 128
    
    moves = dataSetOrgan()
    
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
        correctMoveNode = ((currentMove[0] - 1) * 4) + dirValue
        print correctMoveNode
        
        

        
    print nodesList[3]
    
                               

list1 = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

neuralNetworkLearning(list1,False,0)
