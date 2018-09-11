import os
from NetworkRecorder import networkRecorder
from maths import initWeight

def weightPuller():
    weight = []
    nodes = []
    weightList = []

    # Pulling weight file
    if os.path.lexists('WeightSaves') == False:
        os.makedirs('WeightSaves')
    try:
        weight = open(os.path.join('WeightSaves','latest_weight.txt'), 'r')
        layerNo = int(weight.readline())
        weight.readline()


        for i in range (layerNo + 1):
            nodes.insert(i, int(weight.readline()))
            
        weight.readline()

        for layer in range (0, layerNo):
            weightList.insert(layer, [])

            for node in range (0, int(nodes[layer])):
                weightList[layer].insert(node, [])

                
                for i in range (0, int(nodes[layer+1])):
                    weightList[layer][node].insert(i, float(weight.readline()))

                weight.readline()

                    
        
                         
    except(IOError):
        
        # Weight File isn't here so making a new one
        
        print ('Failed to import weight folder, please check the directory.')
        print ('Creating new set of weights all equal to 1')
        try:
            layerNo = int(raw_input("Please enter the amount of layers.\n"))
        except: 
            print ('Invalid input, shutting down program.')
            exit()

        for layer in range(0, layerNo):
            nodes.insert(layer, raw_input('Please enter the amount of nodes in layer #' + str(layer+1) + "\n"))

        for layer in range (0, layerNo -1):
            weight.insert(layer, [])

            for node in range (0, int(nodes[layer])):
                weight[layer].insert(node, [])

                
                for i in range (0, int(nodes[layer+1])):
                    weight[layer][node].insert(i, initWeight(layer))

        networkRecorder(weight,nodes)
        return (weight, nodes)
    return (weightList, nodes)
    

