from .network import n_network

class Population:
    def __init__(self, config):
        self.size = config['populationSize']
        self.population = []

        for n in range(self.size):
            newAgent = Agent(
                config['networkInputs'],
                config['networkOutputs'],
                config['ouputActivationFunction']
            )

            for n in range(config['initHiddenNodes']):
                newNode = newAgent.addNode()

                if config['forceNewNodeConnections']:
                    newAgent.addConnection(endNode=newNode)
                    newAgent.addConnection(startNode=newNode)
            
            for n in range(config['initConnections']):
                newAgent.addConnection()

            self.population.append(newAgent)
        

class Agent:
    def __init__(self, networkInputs, networkOutputs, outputActivation):
        self.neuralNetwork = n_network.Network(networkInputs, networkOutputs, outputActivation)
    
    def addNode(self):
        return self.neuralNetwork.addNode()

    def addConnection(self, startNode=None, endNode=None):
        return self.neuralNetwork.addConnection(startNode, endNode)
    
    def getNetworkResponse(self, inputs):
        return self.neuralNetwork.run(inputs)
