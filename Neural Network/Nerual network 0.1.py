import math
import os
import importlib
importlib.import_module('Functions')
from Functions import Weight_Puller, maths, NetworkRecorder, dataSetOrganizer, conversion

def neuralNetwork(values):
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
                

        
    print nodesList[3]
    print len(nodesList[3])
                               

list1 = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

neuralNetwork(list1)
