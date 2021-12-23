from .network import n_network
import random
import copy

class Population:
    def __init__(self, config):
        self.size = config['populationSize']
        self.population = []
        self.generation = 1

        for n in range(self.size):
            newAgent = Agent(
                config['networkInputs'],
                config['networkOutputs'],
                config['ouputActivationFunction']
            )

            for n in range(config['initHiddenNodes']):
                newNode = newAgent.addNode(config['forceNewNodeConnections'])
            
            for n in range(config['initConnections']):
                newAgent.addConnection()

            self.population.append(newAgent)
    
    def generatePool(self):
        agentsDict = []

        for agent in self.population:
            pool.append{
                'fitness': agent.fitness,
                'agent': agent
            }
        
        agentsDict = sorted(agentsDict, key = lambda i: i['fitness'])

        pool = []

        for n, agent in enumerate(agentsDict):
            for c in range(n+1):
                pool.append(agent['agent'])

        return pool
    
    def generateEvolvedPopulation(self):
        pool = self.generatePool()

        newGeneration = []

        for n in range(self.size):
            newGeneration.append(copy.deepcopy(random.choice(pool)))

            if random.random() < config['nodeMutationRate']*(config['nodeMutationDecay']**self.generation):
                newGeneration[n].addNode(config['forceNewNodeConnections'])
            
            if random.random() < config['connectionMutationRate']*(config['connectionMutationDecay']**self.generation):
                newGeneration[n].addConnection()
            
            for connection in newGeneration[n].getConnections():
                pass

            for node in newGeneration[n].getNodes():
                pass

        self.population = newGeneration


        self.generation += 1

class Agent:
    def __init__(self, networkInputs, networkOutputs, outputActivation):
        self.neuralNetwork = n_network.Network(networkInputs, networkOutputs, outputActivation)
    
    def addNode(self, addConn):
        newNode = self.neuralNetwork.addNode()
        
        if addConn:
            self..addConnection(endNode=newNode)
            self.addConnection(startNode=newNode)
        
        return newNode

    def addConnection(self, startNode=None, endNode=None):
        return self.neuralNetwork.addConnection(startNode, endNode)
    
    def getNetworkResponse(self, inputs):
        return self.neuralNetwork.run(inputs)
    
    def setFitness(self, fitness):
        self.fitness = fitness
    
    def getConnections(self):
        pass
    
    def getNodes(self):
        pass
