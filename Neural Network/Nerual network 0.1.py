import math
import os
import importlib
importlib.import_module('Functions')
from Functions import Weight_Puller, maths, NetworkRecorder, dataSetOrganizer, conversion

def neuralNetwork(values):
    weights = []
    nodes = []

    (weights, nodes) = Weight_Puller.weightPuller()

    print weights
    print nodes


neuralNetwork(1)
