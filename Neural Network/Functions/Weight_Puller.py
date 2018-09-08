import os
from NetworkRecorder import networkRecorder

def weightPuller():
    weight = []
    nodes = []

    # Pulling weight file
    if os.path.lexists('WeightSaves') == False:
        os.makedirs('WeightSaves')
    try:
        weightList = open(os.path.join('WeightSaves','latest_weight.txt', 'r'))
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
                    weight[layer][node].insert(i, 1)

        networkRecorder(weight,nodes)


