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

    data = filter(str.strip, data)
    practiceData.close()
    
    count = 0


    dataRecorder(data)





def dataRecorder(data):
    if os.path.lexists('Games') == False:
        os.makedirs('Games')

    for i in range (len(data)):
        fileStr = 'Game%s.txt' %(i)
        gameFile = open(os.path.join('Games', fileStr), 'w')
        gameFile.write(data[i])
        gameFile.close()

    
        

    
        
            
##    for i in practiceData:
##        count += 1
##        print i
##        
##        if count == 100:
##            break
dataSetOrgan()
