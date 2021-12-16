from .network import n_network

class Population:
    def __init__(self, size, networkInputs, networkOutputs, outputActivation='sigmoid'):
        self.size = size
        self.population = []

        for n in range(self.size):
            self.population.append(Agent(networkInputs, networkOutputs, outputActivation))
        
        print(self.population[0].neuralNetwork.networkInfo())
        

class Agent:
    def __init__(self, networkInputs, networkOutputs, outputActivation):
        self.neuralNetwork = n_network.Network(networkInputs, networkOutputs, outputActivation)
