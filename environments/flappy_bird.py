import pygame
import random

GRAVITY = 0.2

class Bird:
    def __init__(self, screenHeight):
        self.x = 20
        self.y = 50
        self.width = 50
        self.height = 50
        self.screenHeight = screenHeight
        self.velocity = 0
        self.terminalVelocity = 50

        self.colour = (0, 255, 0)

        self.crashed = False

        self.jumpForce = -5
    
    def step(self):
        self.velocity += GRAVITY

        if self.velocity > self.terminalVelocity:
            self.velocity = self.terminalVelocity
        
        self.y += self.velocity

        #self.y = max(0, self.y)
        #self.y = min(self.y, self.screenHeight-self.height)

    def jump(self):
        self.velocity = self.jumpForce
    
    def getObservation(self, relDistToPipe, topY, bottomY):
        return {
            "relY": self.y/self.screenHeight,
            "vel": self.velocity/(abs(self.jumpForce)+self.terminalVelocity),
            "distToTopPipe": (topY-self.y)/self.screenHeight,
            "distToBottomPipe": (bottomY-self.y)/self.screenHeight,
            "distToPipe": relDistToPipe,
        }

    def checkCollision(self, pipe, crashedAt):

        if self.y < 0 or self.y > (self.screenHeight-self.height):
            self.setCrashed(crashedAt)
            self.colour = (137, 52, 235)
            return

        # rectA's are the bird
        # rectB's are the top pipe
        # rectC's are the bottom pipe
        rectAX1 = self.x
        rectAY1 = self.y
        rectAX2 = self.x+self.width
        rectAY2 = self.y+self.height

        rectBX1 = pipe.x
        rectBY1 = 0
        rectBX2 = pipe.x+pipe.pipeWidth
        rectBY2 = pipe.gapY

        rectCX1 = pipe.x
        rectCY1 = pipe.gapY+pipe.gapSize
        rectCX2 = pipe.x+pipe.pipeWidth
        rectCY2 = pipe.screenHeigth

        if (rectAX1 < rectBX2 and rectAX2 > rectBX1 and rectAY1 < rectBY2 and rectAY2 > rectBY1) or (rectAX1 < rectCX2 and rectAX2 > rectCX1 and rectAY1 < rectCY2 and rectAY2 > rectCY1):
            self.setCrashed(crashedAt)
            self.colour = (137, 52, 235)

    def render(self, screen):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])
    
    def getCrashed(self):
        return self.crashed
    
    def setCrashed(self, crashedValue):
        self.crashed = crashedValue

class Pipe:
    def __init__(self, screenWidth, screenHeigth, speed, gapSize=100):
        self.screenWidth = screenWidth
        self.screenHeigth = screenHeigth
        self.x = screenWidth
        self.pipeWidth = 50
        self.gapSize = 175
        self.gapY = random.randint(0, self.screenHeigth-self.gapSize)
        self.speed = speed
    
    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), [self.x, 0, self.pipeWidth, self.gapY])
        pygame.draw.rect(screen, (255,0,0), [self.x, self.gapY+self.gapSize, self.pipeWidth, self.screenHeigth])
    
    def step(self):
        self.x -= self.speed

class Environment:
    def __init__(self, nBirds=1, doRender=False):
        self.width = 500
        self.height = 750

        self.pipeFreqency = 200
        self.pipes = []

        self.doRender = doRender

        self.stepCount = 1

        self.nBirds = nBirds

        if self.doRender:
            pygame.init()

            self.screen = pygame.display.set_mode((self.width, self.height))
            self.clock = pygame.time.Clock()

        
        self.birds = [Bird(self.height) for n in range(self.nBirds)]
        self.pipes.append(Pipe(self.width, self.height, 2))
    
    def reset(self):
        self.pipes = []
        self.stepCount = 1
        self.birds = [Bird(self.height) for n in range(self.nBirds)]
        self.pipes.append(Pipe(self.width, self.height, 2))
    
    def step(self):
        if self.stepCount % self.pipeFreqency == 0:
            self.pipes.append(Pipe(self.width, self.height, 2))

        self.stepCount += 1
    
    def render(self):
        self.screen.fill((66,205,255))

        for pipe in self.pipes:
            pipe.step()
            pipe.render(self.screen)

        pipesCopy = self.pipes.copy()
        for pipe in pipesCopy:
            if pipe.x+pipe.pipeWidth < 0:
                self.pipes.remove(pipe)

        relDistToPipe = (self.pipes[0].x-self.birds[0].x) / self.width
        topY = self.pipes[0].gapY
        bottomY = self.pipes[0].gapY+self.pipes[0].gapSize
        
        crashedCount = 0
        for bird in self.birds:
            if bird.crashed:
                crashedCount += 1
                continue
            
            bird.step()

            for pipe in self.pipes:
                bird.checkCollision(pipe, self.stepCount)

            bird.render(self.screen)
        
        if crashedCount == len(self.birds):
            return 0

        pygame.display.update()
        self.clock.tick(60)
        print(f'FPS: {self.clock.get_fps()}')
        return 1

if __name__ == '__main__':
    env = Environment(1, True)

    mainloop = True

    while mainloop:
        
        #Itterates through all the events that have happend in the frame
        for event in pygame.event.get():
            #Quit the program if the user clicks the 'X'
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #If the LMB is clicked
                if event.button == 1:
                    env.birds[0].jump()

        env.step()
        env.render()
