from node import *
from connection import *

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
            # randomly add a connection
            pass
        else:
            newConnection = Connection(startNode, endNode)

    def run(self, inputs):
        pass
        