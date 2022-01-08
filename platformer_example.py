import evolution.population as genetics
import environments.platformer as platformer
import visulize.visulizeNetwork as vis
import json
import pygame
import random

with open('hyperparams.json', 'r') as f:
    config = json.loads(f.read())


pop = genetics.Population(config)

visulizer = vis.Visulizer(50,50,100,150,None)


env = platformer.Environment(config['populationSize'], True, visulizer)

visulizer.screen = env.screen

visulizer.updateNetwork(pop.population[0].neuralNetwork)

mainloop = True
prevKeys = []
paused = False

while mainloop:
    #Itterates through all the events that have happend in the frame
    for event in pygame.event.get():
        #Quit the program if the user clicks the 'X'
        if event.type == pygame.QUIT:
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        continue
    
    count = 0
    for player, agent in zip(env.players, pop.population):

        count += 1
        '''
        inputs are going to be:
        0: rel x pos
        1: rel y pos
        2: flattened array of the values from the env observation
        ...
        n
        '''
        obs = bird.getObservation(relDistToPipe, topY, bottomY).values()
        
        if (result := agent.getNetworkResponse(obs)[0]) > 0.5:
            bird.jump()
            player.doActions({'jump': random.random() > 0.5, 'left': random.random() > 0.7, 'right': random.random() > 0.7})

    env.step()

    renderResult = env.render()
    
    for player, agent in zip(env.players, pop.population):
        if not player.crashed:
            visulizer.updateNetwork(agent.neuralNetwork)
            break
    
    visulizer.render()
    
    if not renderResult:
        for player, agent in zip(env.players, pop.population):
            agent.setFitness(player.getCrashed())
        
        pop.generateEvolvedPopulation()

        env.reset()
