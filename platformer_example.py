import evolution.population as genetics
import environments.platformer as platformer
import visulize.visulizeNetwork as vis
import json
import pygame
import random
import list_functions as lf

with open('hyperparams-platformer.json', 'r') as f:
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
            for player, agent in zip(env.players, pop.population):
                agent.setFitness(player.getCrashed())
            
            pop.generatePool()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        continue
    
    count = 0
    environmentObs = env.getEnvironment()
    environmentObs = lf.flattenList(environmentObs)
    for player, agent in zip(env.players, pop.population):

        count += 1

        obs = environmentObs.copy()
        obs.append(player.getRelX())
        obs.append(player.getRelY())

        networkResult = agent.getNetworkResponse(obs)

        player.doActions({'jump': networkResult[0] > 0.5, 'left': networkResult[1] > 0.5, 'right': networkResult[2] > 0.5})

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
