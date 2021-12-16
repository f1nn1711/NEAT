from .node import *
from .connection import *
import random

class Network:
    def __init__(self, nInput, nOutput, outputActivation='linear'):
        self.nInput = nInput
        self.nOutput = nOutput
        self.outputActivation = outputActivation

        self.inputNodes = []
        self.hiddenNodes = []
        self.outputNodes = []

        self.connections = []

        self.generateNodes()

    def generateNodes(self):
        for n in range(self.nInput):
            self.inputNodes.append(Node(True, False))
        
        for n in range(self.nOutput):
            self.outputNodes.append(Node(False, True, self.outputActivation))
    
    def addNode(self, isInput=False, inOutput=False, activation='linear'):
        self.hiddenNodes.append(Node(isInput, inOutput, activation))
    
    def addConnection(self, startNode=None, endNode=None):
        if (not startNode) or (not endNode):
            fromNodes = self.inputNodes+self.hiddenNodes
            startNode = random.choice(fromNodes)

            toNodes = self.outputNodes + self.hiddenNodes

            isValid = False
            while not isValid:
                endNode = random.choice(toNodes)

                if endNode != startNode:
                    isValid = True

            newConnection = Connection(startNode, endNode)
        else:
            newConnection = Connection(startNode, endNode)

        self.connections.append(newConnection)

    def run(self, inputs):
        # map the inputs to all the input nodes
        for node, inputValue in zip(self.inputNodes, inputs):
            node.process([inputValue])
        
        continueFProp = True
        # While not finished
        while continueFProp:
            # Loop through each node that isn't an input node
            for node in self.hiddenNodes+self.outputNodes:
                # Get the connections where to toNode is the
                relevantConnections = []
                for connection in self.connections:
                    if connection.endNode == node:
                        relevantConnections.append(connection)

                feedForwardResults = []
                # Try to do feedForward on each of the connections
                fullFeedForward = True
                for connection in relevantConnections:
                    if (result := connection.feedForward()):
                        feedForwardResults.append(result)
                    else:
                        fullFeedForward = False
                        break
                
                # if feedForward can be done on all the connection
                if fullFeedForward:
                    # pass the results of all of the feedForwards in to the input of the node
                    # run the node to set its output
                    node.process(feedForwardResults)

            # Loop through all of the output nodes and see of they have outputs
            gotAllResults = True
            networkOutput = []
            for node in self.outputNodes:
                if (result := node.output):
                    networkOutput.append(result)
                else:
                    gotAllResults = False
                    break
            
            # If all of them have outputs break out of while
            if gotAllResults:
                continueFProp = False

        # set the outputs of all of them to None
        # return all the output values
        return networkOutput
