import network.n_network as NN

neuralNetwork = NN.Network(1,1)
neuralNetwork.addNode()
neuralNetwork.addConnection(
    neuralNetwork.inputNodes[0],
    neuralNetwork.hiddenNodes[0]
)

neuralNetwork.addConnection(
    neuralNetwork.hiddenNodes[0],
    neuralNetwork.outputNodes[0]
)

output = neuralNetwork.run([2])
