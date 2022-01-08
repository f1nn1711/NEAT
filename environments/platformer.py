import pygame
import random

GRAVITY = 0.2

class Player:
    def __init__(self, screenWidth, screenHeight):
        self.x = 20
        self.y = 50
        self.width = 50
        self.height = 50
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.yVelocity = 0
        self.terminalYVelocity = 50
        self.xVelocity = 0
        self.xAcceleration = 1
        self.terminalXVelocity = 5
        self.colour = (0, 255, 0)
        self.canJump = False
        self.dampening = 0.95
        self.crashed = False
        self.jumpForce = -8
    
    def doActions(self, actions={'jump': False, 'left': False, 'right': False}):
        if actions['jump']:
            if self.yVelocity > 0 and self.canJump:
                self.yVelocity = self.jumpForce
                self.canJump = False
        
        if actions['left']:
            self.xVelocity -= self.xAcceleration
    
        if actions['right']:
            self.xVelocity += self.xAcceleration
    
    def getCrashed(self):
        return self.crashed

    def checkBoundries(self, frame):
        if self.y+self.height > self.screenHeight:
            self.colour = (0, 0, 255)
            self.crashed = frame
        elif self.y < 0:
            self.colour = (0, 0, 255)
            self.crashed = frame

        if self.x < -self.width:
            self.x = self.screenWidth-self.width
        elif self.x > self.screenWidth:
            self.x = 0

    
    def step(self, platforms, frame):
        self.yVelocity += GRAVITY

        if self.yVelocity > self.terminalYVelocity:
            self.yVelocity = self.terminalYVelocity
        
        if abs(self.xVelocity) > self.terminalXVelocity:
            self.xVelocity = (abs(self.xVelocity)/self.xVelocity)*self.terminalXVelocity
        
        self.xVelocity *= self.dampening


        # loop through each platform,
        forcedY = False
        for platform in platforms:
            # if the player startX<playerx<endx-player width
            if platform['startX']-self.width < self.x < platform['endX']:
                # then check if the player is curently above the platform
                if self.y+self.height < platform['y']:
                    # if updating the y would put it below
                    if self.y+self.height + self.yVelocity > platform['y']:
                        # then set the y to the y of the platform
                        # set the yvelocity to 0
                        self.y = platform['y']-self.height
                        self.yVelocity = platform['vel']
                        forcedY = True
                        self.canJump = True

        if not forcedY:
            self.y += self.yVelocity

        self.x += self.xVelocity

        self.checkBoundries(frame)
    
    def render(self, screen):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])


class Platform:
    def __init__(self, isLeft, screenWidth, screenHeight):
        self.isLeft = isLeft

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.thickness = 25
        self.y = -self.thickness
        self.platformSize = random.randint(150,225)

    def getX(self):
        if self.isLeft:
            return 0
        else:
            return self.screenWidth-self.platformSize
    
    def getTopVerticies(self):
        verticies = {
            "TL": [
                self.getX(),
                self.y
            ],
            "TR": [
                self.getX()+self.platformSize,
                self.y
            ]
        }

        return verticies

    def move(self, delta):
        self.y += delta
    
    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), [self.getX(), self.y, self.platformSize, self.thickness])


class Environment:
    def __init__(self, nPlayers=1, doRender=False, visulizer=None):
        self.width = 500
        self.height = 750
        self.visulizer = visulizer

        self.cellSize = 50

        self.nPlayers = nPlayers

        self.leftSide = False
        
        self.spacingAdjustment = 0
        self.yVel = 1*(1+self.spacingAdjustment)
        self.platformFrequency = 170*(1-self.spacingAdjustment)
        self.doRender = doRender

        if self.doRender:
            pygame.init()

            self.screen = pygame.display.set_mode((self.width, self.height))
            self.clock = pygame.time.Clock()

        self.setup()
    
    def setup(self):
        self.frameCount = 0
        self.platforms = []
        self.players = [Player(self.width, self.height) for n in range(self.nPlayers)]

        for n in range(300):
            self.step()

    def reset(self):
        self.setup()
    
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

        formattedPlatforms = []
        for platform in self.platforms:
            platform.render(self.screen)

            formattedPlatform = {
                'startX': platform.getX(),
                'endX': platform.getX()+platform.platformSize,
                'y': platform.y,
                'vel': self.yVel
            }

            formattedPlatforms.append(formattedPlatform)
        
        crashedCount = 0
        for player in self.players:
            player.step(formattedPlatforms)
            if player.crashed != False:
                crashedCount += 1
                continue
            
            player.render(self.screen)


        pygame.display.update()
        self.clock.tick(60)
        #print(f'FPS: {self.clock.get_fps()}')
        if crashedCount == len(self.players):
            return 0
        
        return 1
    
    def verticiesInCell(self, verticies, point1, point2):
        for vertex in verticies:
            if point1[0] <= verticies[vertex][0] <= point2[0] and point1[1] <= verticies[vertex][1] <= point2[1]:
                return True

        return False
    
    def linesInCell(self, verticies, point1, point2):
        if point1[0] > verticies["TL"][0] and verticies["TR"][0] > point2[0] and point1[1] < verticies["TL"][1] < point2[1]:
            return True

        return False
    
    def getCellObservation(self, verticies, point1, point2):
        if self.verticiesInCell(
            verticies,
            point1,
            point2
        ) or self.linesInCell(
            verticies,
            point1,
            point2
        ):
            return 1
        
        return 0

    def getEnvironment(self):
        observations = []
        for row in range(self.height//self.cellSize):
            rowObs = []
            cellY = row * self.cellSize
            for col in range(self.width//self.cellSize):
                cellX = col * self.cellSize
                cellObservation = 0
                # loop through each platform
                for platform in self.platforms:
                    platformVerticies = platform.getTopVerticies()
                    # check if the corners are in the cell
                    if self.getCellObservation(
                        platformVerticies,
                        [cellX, cellY],
                        [cellX+self.cellSize, cellY+self.cellSize]
                    ):
                        cellObservation = 1
                        break
                
                rowObs.append(cellObservation)

            observations.append(rowObs)
        
        print('-'*20)
        print(observations)
        return observations


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

        env.getEnvironment()
