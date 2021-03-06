
import math
import random



def sigmoid(x):
    e = 2.71828182845904523536028747135266249775724709369995
    y = 1/(1+(e**-x))

    return float(y)

def errorFunc(o, t):
    error = 1/2 * ((t-o)**2)
    return error

def errorSum(errorList):
    accum = 0
    for i in errorList:
        try:
            accum += i
        except(TypeError):
            pass

    return accum

def errorGrad(error, weight):
    errorGrad = []
    count = 0
    for layer in range(len(weight)):
        for node in range(len(weight[layer])):
            for i in range (len(weight[layer][node])):
                errorGrad.insert(count, sigmoid(error)/sigmoid(weight[layer][node][i]))
    return errorGrad


def initWeight(layer):
    weight = random.uniform(-1.0/math.sqrt(float(layer+1)), 1.0/math.sqrt(float(layer+1)))
    return weight

def weightDiff(errorList, weight):
    lc = 0.1
    count = 0
    for layer in range(len(weight)):
        for node in range(len(weight[layer])):
            for i in range (len(weight[layer][node])):
                weight[layer][node][i] =(-lc*(sigmoid(errorList[count]/sigmoid(weight[layer][node][i]))))
                count += 1
    
    
    return weight

