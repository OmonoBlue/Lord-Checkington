import os
import math

Data = open('Test Game.txt', 'r').read().split(" ")
for move in range(len(Data) - 1):
    if "-" not in Data[move]:
        del Data[move]

newMove = [None, None, None, None] * len(Data)

        
for move in range(len(Data) - 1):
    else:
        origin = Data[move].split('-')[0]
        destination = Data[move].split('-')[1]
        
        for row in range(8):
            mode = row % 2

            for space in range(8):

                if space % 2 != mode:

                    if origin != 0:

                        origin -= 1
                        
                    else:
                        newMove[move][0] = row
                        newMove[move][1] = space


        for row in range(8):
            mode = row % 2

            for space in range(8):

                if space % 2 != mode:

                    if destination != 0:

                        destination -= 1
                        


                    

            

            

            


