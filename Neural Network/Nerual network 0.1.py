import math
import os
import importlib
importlib.import_module('Functions')
from Functions import Weight_Puller, maths, NetworkRecorder, dataSetOrganizer



neuralNetwork = []
nodes = []

(neuralNetwork, nodes) = Weight_Puller.weightPuller()


dataSetOrganizer.dataSetOrgan()
        
