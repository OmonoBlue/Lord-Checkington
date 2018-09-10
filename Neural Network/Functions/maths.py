import math

def sigmoid(x):
    e = 2.71828182845904523536028747135266249775724709369995
    y = 1/(1+(e**-x))

    return float(y)

def errorFunc(o, t):
    error = 1/2(o-t)^2
    return error

def errorSum(errorList):
    for i in errorList:
        accum += i
    return accum

def errorGrad(error, weight):
    errorGrad = []
    count = 0
    for layer in range(len(weight)):
        for node in range(len(weight[layer])):
            for i in range (len(weight[layer][node])):
                errorGrad.insert(count, sigmoid(error)/sigmoid(weight[layer][node][i]))
    return errorGrad

test = [[[1,2,3,4,5,6,7,8,9]]]
errorGrad = errorGrad(2, test)

print errorGrad
