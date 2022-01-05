import evolution.network.n_network as NN
import random

random.seed(1)

neuralNetwork = NN.Network(1,1, outputActivation='sigmoid')

neuralNetwork.addNode()
neuralNetwork.addNode()

neuralNetwork.addConnection(
    neuralNetwork.inputNodes[0],
    neuralNetwork.hiddenNodes[0]
)

neuralNetwork.addConnection(
    neuralNetwork.hiddenNodes[0],
    neuralNetwork.hiddenNodes[1]
)

neuralNetwork.addConnection(
    neuralNetwork.hiddenNodes[1],
    neuralNetwork.outputNodes[0]
)

output = neuralNetwork.run([2])
print(output) # This should return [0.6296103610471014]
neuralNetwork.saveNetwork()
