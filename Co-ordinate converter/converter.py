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

    
for move in range(len(Data) - 1):
    if "-" not in Data[move]:
        del Data[move]
print Data

newMove = []
for move in range(len(Data) - 1):
    origin = int(Data[move].split('-')[0])
    dest = int(Data[move].split('-')[1])

    print conversionList[origin]
    newMove.append([conversionList[origin][0], conversionList[origin][1], conversionList[origin][0] - conversionList[dest][0], conversionList[origin][1] - conversionList[dest][1]])
    

newFile = open('Reorginized Game.txt', 'w')

newFile.write(str(newMove))


newFile.close()
