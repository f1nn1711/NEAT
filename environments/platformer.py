import pygame
import random

GRAVITY = 0.2

class Player:
    def __init__(self, screenWidth):
        self.x = 20
        self.y = 50
        self.width = 50
        self.height = 50
        self.screenWidth = screenWidth
        self.yVelocity = 0
        self.terminalYVelocity = 50

        self.xVelocity = 0
        self.xAcceleration = 1
        self.terminalXVelocity = 5

        self.colour = (0, 255, 0)

        self.dampening = 0.95

        self.crashed = False

        self.jumpForce = -5
    
    def doActions(self, actions={'jump':False,'left':False,'right':False}):
        if actions['jump']:
            if self.yVelocity > 0:
                self.yVelocity = self.jumpForce
        
        if actions['left']:
            self.xVelocity -= self.xAcceleration
    
        if actions['right']:
            self.xVelocity += self.xAcceleration
        
        self.step()
    
    def step(self):
        self.yVelocity += GRAVITY

        if self.yVelocity > self.terminalYVelocity:
            self.yVelocity = self.terminalYVelocity
        
        if abs(self.xVelocity) > self.terminalXVelocity:
            self.xVelocity = (abs(self.xVelocity)/self.xVelocity)*self.terminalXVelocity
        
        self.xVelocity *= self.dampening

        self.y += self.yVelocity
        self.x += self.xVelocity

        # self.x = max(0, self.x)
        # self.x = min(self.x+self.width, self.screenWidth)
    
    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), [self.x, self.y, self.width, self.height])
    
class Platform:
    def __init__(self, isLeft, screenWidth, screenHeight):
        self.isLeft = isLeft

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.thickness = 25
        self.y = -self.thickness
        self.platformSize = random.randint(150,225)
        
    
    def move(self, delta):
        self.y += delta
    
    def render(self, screen):
        if self.isLeft:
            pygame.draw.rect(screen, (0,0,255), [0, self.y, self.platformSize, self.thickness])
        else:
            pygame.draw.rect(screen, (0,0,255), [
                self.screenWidth-self.platformSize,
                self.y,
                self.platformSize,
                self.thickness
            ])

class Environment:
    def __init__(self, nPlayers=1, doRender=False, visulizer=None):
        self.width = 500
        self.height = 750
        self.visulizer = visulizer

        self.nPlayers = nPlayers

        self.leftSide = False
        
        self.yVel = 1
        self.platformFrequency = 175
        self.frameCount = 0

        self.platforms = []

        self.doRender = doRender

        self.players = [Player(self.width) for n in range(self.nPlayers)]

        if self.doRender:
            pygame.init()

            self.screen = pygame.display.set_mode((self.width, self.height))
            self.clock = pygame.time.Clock()
    
    def reset(self):
        pass
    
    def step(self):
        if self.frameCount % self.platformFrequency == 0:
            self.leftSide = not self.leftSide
            self.platforms.append(Platform(self.leftSide, self.width, self.height))
        
        for platform in self.platforms:
            platform.move(self.yVel)
        
        self.removePlatforms()
        self.frameCount += 1
    
    def removePlatforms(self):
        tempPlatforms = self.platforms

        for platform in tempPlatforms:
            if platform.y > self.height:
                self.platforms.remove(platform)

    def updateVisulizerNetwork(self, network):
        self.visulizer.network = network
    
    def render(self):
        self.screen.fill((0,0,0))

        
        if self.visulizer:
            self.visulizer.render()
        
        for platform in self.platforms:
            platform.render(self.screen)
        
        for player in self.players:
            player.render(self.screen)

        pygame.display.update()
        self.clock.tick(60)
        #print(f'FPS: {self.clock.get_fps()}')
        return 1

if __name__ == '__main__':
    env = Environment(1, True, None)

    mainloop = True

    while mainloop:
        
        #Itterates through all the events that have happend in the frame
        for event in pygame.event.get():
            #Quit the program if the user clicks the 'X'
            if event.type == pygame.QUIT:
                sys.exit()

        actions = {'jump':False,'left':False,'right':False}
        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            actions['left'] = True
        
        if keys[pygame.K_RIGHT]:
            actions['right'] = True
        
        if keys[pygame.K_UP]:
            actions['jump'] = True
        
        env.players[0].doActions(actions)

        env.step()
        env.render()
