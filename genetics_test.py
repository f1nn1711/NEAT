import evolution.population as genetics
import environments.flappy_bird as flappyBird
import json
import pygame
import random

with open('hyperparams.json', 'r') as f:
    config = json.loads(f.read())


pop = genetics.Population(config)

env = flappyBird.Environment(config['populationSize'], True)

mainloop = True

while mainloop:
    
    #Itterates through all the events that have happend in the frame
    for event in pygame.event.get():
        #Quit the program if the user clicks the 'X'
        if event.type == pygame.QUIT:
            sys.exit()

    #### LOGIC FOR DECIDING BIRD ACTION ####
    '''
    Below is an example of the birds jumping randomly.
    There is a 3% chance the bird will jump per frame
    
    for bird in env.birds:
        if random.random() > 0.97:
            bird.jump()
    
    '''
    relDistToPipe = (env.pipes[0].x-env.birds[0].x) / env.width
    topY = env.pipes[0].gapY
    bottomY = env.pipes[0].gapY+env.pipes[0].gapSize

    count = 0
    for bird, agent in zip(env.birds, pop.population):

        count += 1
        obs = bird.getObservation(relDistToPipe, topY, bottomY).values()
        '''
        if random.random() > 0.97:
            bird.jump()

        #print(agent.getNetworkResponse(obs)[0])
        '''

        
        if (result := agent.getNetworkResponse(obs)[0]) > 0.5:
            bird.jump()
            
        
        
    


    ########

    
    env.step()

    renderResult = env.render()

    if not renderResult:
        # Create new population
        sys.exit()

