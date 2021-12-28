from .network import n_network
import random
import copy

class Population:
    def __init__(self, config):
        self.size = config['populationSize']
        self.population = []
        self.generation = 1

        self.config = config

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
            agentsDict.append({
                'fitness': agent.fitness,
                'agent': agent
            })
        
        agentsDict = sorted(agentsDict, key = lambda i: i['fitness'])

        pool = []

        for n, agent in enumerate(agentsDict):
            for c in range(n+1):
                pool.append(agent['agent'])

        return pool
    
    def generateEvolvedPopulation(self):
        pool = self.generatePool()

        newGeneration = []

        print(len(pool))
        for n in range(self.size):
            newGeneration.append(copy.deepcopy(random.choice(pool)))

            if random.random() < self.config['nodeMutationRate']*((1-self.config['nodeMutationDecay'])**self.generation):
                newGeneration[n].addNode(self.config['forceNewNodeConnections'])
            
            if random.random() < self.config['connectionMutationRate']*((1-self.config['connectionMutationDecay'])**self.generation):
                newGeneration[n].addConnection()
            
            print(newGeneration)
            print(newGeneration[n].getConnections())
            for connection in newGeneration[n].getConnections():
                if random.random() < self.config['weightMutationRate']*((1-self.config['weightMutationDecay'])**self.generation):
                    connection.mutate()

            for node in newGeneration[n].getNodes():
                if random.random() < self.config['biasMutationRate']*((1-self.config['biasMutationDecay'])**self.generation):
                    node.mutate()

        self.population = newGeneration

        self.generation += 1

class Agent:
    def __init__(self, networkInputs, networkOutputs, outputActivation):
        self.neuralNetwork = n_network.Network(networkInputs, networkOutputs, outputActivation)
    
    def addNode(self, addConn):
        newNode = self.neuralNetwork.addNode()
        
        if addConn:
            self.addConnection(endNode=newNode)
            self.addConnection(startNode=newNode)
        
        return newNode

    def addConnection(self, startNode=None, endNode=None):
        return self.neuralNetwork.addConnection(startNode, endNode)
    
    def getNetworkResponse(self, inputs):
        return self.neuralNetwork.run(inputs)
    
    def setFitness(self, fitness):
        self.fitness = fitness
    
    def getConnections(self):
        return self.neuralNetwork.getConnections()
    
    def getNodes(self):
        return self.neuralNetwork.getNodes()
