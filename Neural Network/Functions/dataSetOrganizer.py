import os
import re

def dataSetOrgan():
    count = 0
    practiceData = open(os.path.join('Training data', 'OCA_2.0 - Copy.txt'), 'r')
    data = practiceData.read()
    data = data.replace('(', '')
    data = data.replace(')', '')
    data = data.replace('[','(')
    data = data.replace(']',')')


    data = re.split('[()]', data)
    count = 0
    for i in range (len(data)):
        count += 1
        if count == 20462:
            for ayy in range (3):
                del data[count]
        if count < 20462:
            for ayy in range (11):
                del data[count]

##    data = filter(str.strip, data)
##    for i in range (len(data)-1):
##        count = 0
##
##        data.insert(i, data[i].split(' '))
##        for move in range (len(data[i])/3):
##            if count == 0:
##                del data[i][move]
##            count += 1
##            if count == 3:
##                count = 0

    for i in data:
        print i
            
##    for i in practiceData:
##        count += 1
##        print i
##        
##        if count == 100:
##            break
dataSetOrgan()
