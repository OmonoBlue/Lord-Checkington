import os
import math

Data = open('Test Game.txt', 'r').read().split(" ")

conversionList = {
    1: [6, 0],
    2: [4, 0],
    3: [2, 0],
    4: [0, 0],
    5: [7, 1],
    6: [5, 1],
    7: [3, 1],
    8: [1, 1],
    9: [6, 2],
    10: [4, 2],
    11: [2, 2],
    12: [0, 2],
    13: [7, 3],
    14: [5, 3],
    15: [3, 3],
    16: [1, 3],
    17: [6, 4],
    18: [4, 4],
    19: [2, 4],
    20: [0, 4],
    21: [7, 5],
    22: [5, 5],
    23: [3, 5],
    24: [1, 5],
    25: [6, 6],
    26: [4, 6],
    27: [2, 6],
    28: [0, 6],
    29: [7, 7],
    30: [5, 7],
    31: [3, 7],
    32: [1, 7]
    }

corList = conversionList.items()

def numToCor(num):
    return conversionList(num)

def corToNum(cor1, cor2):

    for i in range(len(corList)):
        if corList[i][1] == [cor1, cor2]:
            return i

