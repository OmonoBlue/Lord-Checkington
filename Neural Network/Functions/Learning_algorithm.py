import os
import math
from maths import sigmoid, errorFunc, errorSum, errorGrad, weightDiff

def errorIndiv (nodes, act):
    error = []
    for i in range (len(nodes)):
        if i != act:
            error.append(errorFunc(nodes[i],0))
        else:
            error.append(errorFunc(nodes[i],1))

    totalError = errorSum(error)
    
