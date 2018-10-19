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

    for i in range (len(data)):
        data[i] = data[i].replace('.',' ')
        data[i] = data[i].replace('  ',' ')
        data[i] = data[i].replace('x', '-')
        data[i] = data[i].replace('\n',' ')
        data[i] = data[i].split(' ')
        

    for i in range (len(data)):
        moveCount = 0
        for move in range (len(data[i])+ 1000):
            try:

                if "-" not in data[i][move]:
                    del data[i][move]
                    moveCount += 1
                else:
                    dashCounter = 0
                    print data[i][move]
                    for char in range (len(data[i][move - moveCount])):
                        if data[i][move - moveCount][char] == "-":
                            dashCounter += 1
                        if dashCounter >= 2:
                            data[i][move] = data[i][move - moveCount][:char]
                    fullMove = data[i][move - moveCount].split('-')
                    data[i][move - moveCount] = [data[i][move - moveCount], fullMove]
                    data[i][move - moveCount][0] = data[i][move - moveCount][0].split('-')
##                if "\n" in data[i][move]:
##                    gayLineSkipper = 1
##                if len(data[i][move]) > 5:
##                    if gayLineSkipper == 1:
##                        data[i][move] = data[i][move][:5] + "\n"
##                    if gayLineSkipper == 0:
##                        data[i][move] = data[i][move][:5]
            except (IndexError):
                pass

    for i in range(len(data)):
        del data[i][len(data[i])-1]
    matchRecorder(data)




def matchRecorder(data):
    if os.path.lexists('Games') == False:
        os.makedirs('Games')

    for i in range (len(data)):
        moveW = 0
        fileStr = 'Game%s.txt' %(i)
        gameFile = open(os.path.join('Games', fileStr), 'w')
        for move in range (1, len(data[i])-1):
##            moveW += 1
##            if moveW == 2:
##                try:
##                    data[i][move] = data[i][move].split('-')
##                    data[i][move][0] = str((int(data[i][move][0]) -33) *(-1))
##                    data[i][move][1] = str((int(data[i][move][1]) -33) *(-1))
##                    dataSave =  ''.join(data[i][move][0] + '-' + data[i][move][1])
##                    data[i][move].pop()
##                    data[i][move] = dataSave
##                    moveW = 0
##                except:
##                    pass
            gameFile.write(str(data[i][move]) + ' ')
        gameFile.close()

    
        
def dataConverter():
    data = []
    count = 0
    while True:
        try:
            dataFile = open(os.path.join('Games', 'Game%s.txt' %(count)), 'r')
            dataFileExc = dataFile.read()
            data.insert(count, dataFileExc)
            count += 1
        except (IOError, IndexError):
            break

    for i in data:
        print i
        
        
        
    
dataSetOrgan()

        
            
##    for i in practiceData:
##        count += 1
##        print i
##        
##        if count == 100:
##            break
