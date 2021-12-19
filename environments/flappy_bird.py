import pygame
import random

GRAVITY = 0.2

class Bird:
    def __init__(self):
        self.x = 20
        self.y = 50
        self.width = 50
        self.height = 50

        self.velocity = 0
        self.terminalVelocity = 50

        self.jumpForce = -5
    
    def step(self):
        self.velocity += GRAVITY

        if self.velocity > self.terminalVelocity:
            self.velocity = self.terminalVelocity
        
        self.y += self.velocity

    def jump(self):
        self.velocity = self.jumpForce

    def checkCollision(pipe):

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

            print('collision')

    def render(self, screen):
        pygame.draw.rect(screen, (0,255,0), [self.x, self.y, self.width, self.height])

class Pipe:
    def __init__(self, screenWidth, screenHeigth, speed, gapSize=100):
        self.screenWidth = screenWidth
        self.screenHeigth = screenHeigth
        self.x = screenWidth
        self.pipeWidth = 50
        self.gapSize = 100
        self.gapY = random.randint(0, self.screenHeigth-self.gapSize)
        self.speed = speed
    
    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), [self.x, 0, self.pipeWidth, self.gapY])
        pygame.draw.rect(screen, (255,0,0), [self.x, self.gapY+self.gapSize, self.pipeWidth, self.screenHeigth])
    
    def step(self):
        self.x -= self.speed

class Environment:
    def __init__(self, doRender=False):
        self.width = 500
        self.height = 750

        self.pipeFreqency = 400
        self.pipes = []

        self.doRender = doRender

        self.stepCount = 0

        if self.doRender:
            pygame.init()

            self.screen = pygame.display.set_mode((self.width, self.height))
            self.clock = pygame.time.Clock()

        
        self.birds = [Bird()]
    
    def step(self):
        if self.stepCount % self.pipeFreqency == 0:
            self.pipes.append(Pipe(self.width, self.height, 2))

        self.stepCount += 1
    
    def render(self):
        self.screen.fill((66,205,255))

        for pipe in self.pipes:
            pipe.step()
            pipe.render(self.screen)
        
        for bird in self.birds:
            bird.step()
            bird.render(self.screen)

        pygame.display.update()
        self.clock.tick(60)

env = Environment(True)

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
