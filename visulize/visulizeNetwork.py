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

    def render(self):
        for n in range(len(self.network.inputNodes)):
            pygame.draw.circle(self.screen, (255, 255, 255), [self.x, self.y+((n+1)*self.inputSpacing)], 10)

        for n in range(len(self.network.outputNodes)):
            pygame.draw.circle(self.screen, (255, 255, 255), [self.x+self.width, self.y+((n+1)*self.outputSpacing)], 10)

        for n in range(len(self.network.hiddenNodes)):
            pygame.draw.circle(self.screen, (255, 255, 255), [self.x+(self.width//2), self.y+((n+1)*self.hiddenSpacing)], 10)

        for connection in self.network.getConnections:
            # get the from node
            # see what the index is for the from node out of the relevalt input/hidden/output list

            # get the to node
            # see what the index is for the to node out of the relevalt input/hidden/output list

            # calculate the start y bassed on:
            #   self.y+((n+1)*self.inputSpacing)
            # where inputSpacing is the relevant one

            # do the same for the end y

            # get the relevant x coord based on what type of node it is for both eht start and end node
