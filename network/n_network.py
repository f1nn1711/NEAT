from node import *
from connection import *
import random

class Network:
    def __init__(self, nInput, nOutput):
        self.nInput = nInput
        self.nOutput = nOutput

        self.inputNodes = []
        self.hiddenNodes = []
        self.outputNodes = []

        self.connections = []

    def generateNodes(self):
        for n in range(self.nInput):
            self.inputNodes.append(Node(True, False))
        
        for n in range(self.nOutput):
            self.outputNodes.append(Node(False, True))
    
    def addNode(self):
        self.hiddenNodes.append(Node(False, False))
    
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
        # While not finished
            # Loop through each node that isn't an input node
                # Get the connections where to toNode is the
                # Try to do feedForward on each of the connections
                # if feedForward can be done on all the connection
                    # pass the results of all of the feedForwards in to the input of the node
                    # run the node to set its output

            # Loop through all of the output nodes and see of they have outputs
            # If all of them have outputs break out of while

        # set the outputs of all of them to None
        # return all the output values
        pass
