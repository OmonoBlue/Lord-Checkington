import os


def networkRecorder(weight, nodes):
    networkValues = open(os.path.join('WeightSaves', 'latest_weight.txt'), 'w')



    networkValues.write(str(len(weight)) + '\n\n')

    for i in range (len(nodes)):
        networkValues.write(str(nodes[i])+'\n')

    networkValues.write('\n')

    for layer in range (len(weight)):
        for node in range (len(weight[layer])):
            for i in range (len(weight[layer][node])):
                networkValues.write(str(weight[layer][node][i])+'\n')
            networkValues.write('\n')
        
    networkValues.close()
