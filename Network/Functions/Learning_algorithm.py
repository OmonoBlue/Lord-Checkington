import os
import math
from maths import sigmoid, errorFunc, errorSum, errorGrad, weightDiff, hiddenErrorFunc, derivative

def errorIndiv (nodes, act):
    lc = 0.1
    error = []
    for i in range (len(nodes)):
        if i != act:
            error.append(errorFunc(nodes[i],0))
        else:
            error.append(errorFunc(nodes[i],1))

    totalError = errorSum(error)
    return totalError

def hiddenError (nodes, weights, error):
    lc = 0.1
    nodesError = nodes

    for layer in range (len(nodesError)):
        for node in range (len(nodes[layer])):
            nodes[layer][node] = 0

    nodesError[3] = error

    for layer in range (len(nodes)-1,0,-1):
        for node in range(len(nodes[layer])):
            for i in range (len(nodes[layer-1])):

                nodesError[layer-1][i] += (weights[layer-1][i][node] * nodesError[layer][node]) * derivative(nodes[layer][node])


    for layer in range (len(nodes)-1):
        for node in range(len(nodes[layer])):
            for i in range (len(nodes[layer+1])):



                weights[layer][node][i] = weights[layer][node][i] + lc * nodesError[layer+1][i] * nodes[layer][node]

    return weights
