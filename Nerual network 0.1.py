import math
import os
import importlib
importlib.import_module('Functions')
from Functions import Weight_Puller, maths, NetworkRecorder, dataSetOrganizer, conversion

def neuralNetwork(values, color):
    weights = []
    nodes = []

    (weights, nodes) = Weight_Puller.weightPuller()
    values2 = []

    if color == "R" :
        for i in range (len(values)):
            values[i] = values[i] * -1
            values2.insert(31-i,(values[i]))
    else:
        values2 = values
        
    print values2
            

values = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
neuralNetwork(values,"R")
