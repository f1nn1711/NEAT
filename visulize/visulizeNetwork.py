import pygame

class Visulizer:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen

    def updateNetwork(self, network):
        self.network = network
        self.inputSpacing = self.height/(len(self.network.inputNodes)+1)
        self.hiddenSpacing = self.height/(len(self.network.hiddenNodes)+1)
        self.outputSpacing = self.height/(len(self.network.outputNodes)+1)
    
    def getNodeType(self, node):
        if node.isInput:
            return 'input'
        elif node.isOutput:
            return 'output'
        else:
            return 'hidden'
    
    def getNodeIndex(self, node, nodeType):
        if nodeType == 'input':
            return self.network.inputNodes.index(node)
        elif nodeType == 'hidden':
            return self.network.hiddenNodes.index(node)
        elif nodeType == 'output':
            return self.network.outputNodes.index(node)
    
    def getNodeCoords(self, nodeType, nodeIndex):
        coords = [0,0]

        if nodeType == 'input':
            coords[0] = self.x
            coords[1] = self.y+((nodeIndex+1)*self.inputSpacing)
        elif nodeType == 'hidden':
            coords[0] = self.x+(self.width//2)
            coords[1] = self.y+((nodeIndex+1)*self.outputSpacing)
        elif nodeType == 'output':
            coords[0] = self.x+self.width
            coords[1] = self.y+((nodeIndex+1)*self.outputSpacing)
        
        return coords

    def render(self):
        for n in range(len(self.network.inputNodes)):
            pygame.draw.circle(self.screen, (255, 255, 255), [self.x, self.y+((n+1)*self.inputSpacing)], 10)

        for n in range(len(self.network.outputNodes)):
            pygame.draw.circle(self.screen, (255, 255, 255), [self.x+self.width, self.y+((n+1)*self.outputSpacing)], 10)

        for n in range(len(self.network.hiddenNodes)):
            pygame.draw.circle(self.screen, (255, 255, 255), [self.x+(self.width//2), self.y+((n+1)*self.outputSpacing)], 10)

        for connection in self.network.getConnections():
            # get the from node
            # see what the index is for the from node out of the relevalt input/hidden/output list
            fromNodeType = self.getNodeType(connection.startNode)
            fromNodeIndex = self.getNodeIndex(connection.startNode, fromNodeType)
            # get the to node
            # see what the index is for the to node out of the relevalt input/hidden/output list
            toNodeType = self.getNodeType(connection.endNode)
            toNodeIndex = self.getNodeIndex(connection.endNode, toNodeType)
            # calculate the start y bassed on:
            #   self.y+((n+1)*self.inputSpacing)
            # where inputSpacing is the relevant one
            # do the same for the end y
            # get the relevant x coord based on what type of node it is for both eht start and end node
            startCoords = self.getNodeCoords(fromNodeType, fromNodeIndex)
            endCoords = self.getNodeCoords(toNodeType, toNodeIndex)

            if connection.weight < 0:
                connColour = (0,0,255)
            else:
                connColour = (255,0,0)

            pygame.draw.line(self.screen, connColour, startCoords, endCoords)

