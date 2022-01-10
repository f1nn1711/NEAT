from .network import n_network
import random
import copy
import os
import json

class Population:
    def __init__(self, config):
        self.size = config['populationSize']
        self.population = []
        self.generation = 1
        self.config = config

        if self.config['savePopulationProgress']:
            with open('progress/progress.json', 'w') as f:
                f.write(json.dumps([]))

        for n in range(self.size):
            if (saveFile := self.config['loadFromSave']):
                dirname = os.path.dirname(__file__)
                filename = os.path.join(dirname, saveFile)

                with open(filename, 'r') as f:
                    networkJson = json.loads(f.read())

                newAgent = Agent(jsonData=networkJson)

                self.population.append(newAgent)
                continue

            newAgent = Agent(
                self.config['networkInputs'],
                self.config['networkOutputs'],
                self.config['ouputActivationFunction']
            )

            for n in range(self.config['initHiddenNodes']):
                newNode = newAgent.addNode(self.config['forceNewNodeConnections'])
            
            for n in range(self.config['initConnections']):
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

        if self.config['saveProgress']:
            self.saveAgent(agentsDict[-1]['agent'])

        if self.config['savePopulationProgress']:
            fitnessValues = [element['fitness'] for element in agentsDict]
            populationStatistics = {
                "min": fitnessValues[0],
                "25percentile": fitnessValues[round(len(fitnessValues)*0.25)],
                "mean": sum(fitnessValues)/len(fitnessValues),
                "75percentile": fitnessValues[round(len(fitnessValues)*0.75)],
                "max": fitnessValues[-1]
            }

            self.savePerformance(populationStatistics)

        pool = []

        for n, agent in enumerate(agentsDict):
            for c in range(n+1):
                pool.append(agent['agent'])

        return pool
    
    def saveAgent(self, agent):
        agent.neuralNetwork.saveNetwork(prefix=f'gen-{self.generation}-')
    
    def generateEvolvedPopulation(self):
        pool = self.generatePool()

        newGeneration = []

        # print(len(pool))
        for n in range(self.size):
            newGeneration.append(copy.deepcopy(random.choice(pool)))

            if random.random() < self.config['nodeMutationRate']*((1-self.config['nodeMutationDecay'])**(self.generation-1)):
                newGeneration[n].addNode(self.config['forceNewNodeConnections'])
            
            if random.random() < self.config['connectionMutationRate']*((1-self.config['connectionMutationDecay'])**(self.generation-1)):
                newGeneration[n].addConnection()

            for connection in newGeneration[n].getConnections():
                if random.random() < self.config['weightMutationRate']*((1-self.config['weightMutationDecay'])**(self.generation-1)):
                    connection.mutate()

            for node in newGeneration[n].getNodes():
                if random.random() < self.config['biasMutationRate']*((1-self.config['biasMutationDecay'])**(self.generation-1)):
                    node.mutate()

        self.population = newGeneration

        self.generation += 1
    
    def savePerformance(self, data):
        with open('progress/progress.json', 'r') as f:
            existingData = json.loads(f.read())
        
        existingData.append(data)

        with open('progress/progress.json', 'w') as f:
            f.write(json.dumps(existingData))


class Agent:
    def __init__(self, networkInputs=1, networkOutputs=1, outputActivation='sigmoid', jsonData=None):
        if jsonData:
            self.neuralNetwork = n_network.Network(networkJson=jsonData)
            return

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
