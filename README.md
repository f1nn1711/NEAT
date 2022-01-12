# NEAT
## Get started
First download/clone this repository, this can be done from the github web interface or be cloning the repository through the CLI. This has been developed on Python 3.8.0.
## Using the program
To see the NEAT algorithm immediatly run either "flappy_bird_example.py" or "platformer_example.py". If you wish to play the environments yourself, run either environments/flappy_bird.py or environments/platformer.py.
If you wish to edit how the simulation is running, please refer to the hyperparameters section below.
Once you are happy with the progress that the population has made you and close the program, navigate to the progress directory and run progressView.py. It is important that this file is ran from withing the progress directory. This is will display a graph of the fitness of the population over the generations.

## Flappy Bird
This is a very basic clone of the orignal game, each frame the only actions the player can take is to either jump or not to jump.
The inputs for this envronment are:
1. Vertical velocity
2. Forward distance to the next pipe
3. Vertical distance to the top of the next pipe
4. Vertical distance to the bottom of the next pipe
5. Relative Y position
## Platformer
This is a simple game where the player needs to jump and move left or right to start on the platforms. The platforms have a random width, the player can travel up through a platform but can't fall back through a platfrom. If the player moves of either the left or right hand screen they will teleport to the oposite side of the screen however if they go off the top or bottom of the screen then they will die. The player can only jump once they have touched a platform, they dont have to be touching a platform when they jump, this means if they are on a platform and slide off it they will still be able to jump.
In this environment the inputs are:
1. A simplified view of the screen where a 0 is a cell where the player would fall and a 1 is a place where the player can stand. An example can be seen below:
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
2. It is also give the relative x and y position of the player.

## How does NEAT work?
An implementation of the NEAT(Neuro Evolution of Augmenting Topologies). NEAT combines neural networks and a genetic algorithm, in traditional neural networks the network weights and biases are adjusted by an optimization function (for example: stochastic gradient decent, adaptive moment estimation). In the NEAT algorithm the weights and biases are adjusted by random mutations. In traditional neural network the structure of the network is pre-defined in the hyper parameters and stay constants through the training process. In NEAT the structure of the nerual network can change throughout the training process through survival of the fittest. There is a chance that a mutation will occur where a new neuron or connection will be added to the network. In addition to this the weights and biases can under go mutations to allow them to change and improve over time.
## The advantages of NEAT
By allowing the structure of the neural network to change over time it also means that the most efficient network model can be found as well as the best weights and biases. This allows the most optimal network structure to be found.
## The disadvantages of NEAT
Since the mutations are random, it is possible that the population may be unlucky and not have any mutations with positive affect. Since this implementation of the NEAT algorithm has an adaptive learning rate, if the population starts mutating in the wrong direction it is possible that this error is unable to be resolved in later generations.
## The hyperparameters
Firstly a parameter is something that can be changed, when refering to a neural network an example of a parameter would be a weight or a bias. These are things that can be chnaged during the training process. A hyperparameter is something that can't be change during the training process. Here are the hyperparameters that can be set for this program:
1. "populationSize" => The number of agents per generation (Any integer >0)
2. "networkInputs" => The number of inputs to the neural network (Any integer >0)
3. "networkOutputs" => The number of output to the neural network (Any integer >0)
4. "initHiddenNodes" => The number of hidden nodes that the network will start with (Any integer >=0)
5. "initConnections" => The number of random connections the network will start with (Any integer >=0)
6. "ouputActivationFunction" => The activation function that will be used by the output node. Look at evolution/network/activation.py to see the available activation fucntions.
7. "higherIsBetter" => Determines if the higher the fitness the more likely it is to survive (Boolean)
8. "forceNewNodeConnections" => Determines if a new node gets created, will it be connected to two other nodes. (Boolean)
9. "nodeMutationRate" => This is the chance that a new node will be added to the model. (Float 0<=n<=1)
10. "nodeMutationDecay" => This is the rate at which the chance a new node is added to the model decays. (Float 0<=n<=1)
11. "connectionMutationRate" => s is the rate at which the chance a new connection is added to the model decays. (Float 0<=n<=1)
12. "connectionMutationDecay" => This is the rate at which the chance a connection node is added to the model decays. (Float 0<=n<=1)
13. "weightMutationRate" => This is the chance that a weight from the network is randomised. (Float 0<=n<=1)
14. "weightMutationDecay" => This is the rate at which the chance of a weight mutating decays. (Float 0<=n<=1)
15. "biasMutationRate" => This is the chance that a bias from the network is randomised. (Float 0<=n<=1)
16. "biasMutationDecay" => This is the rate at which the chance of a bias mutating decays. (Float 0<=n<=1)
17. "savePopulationProgress" => This controls if statistics about each generation are recorded to be viewed later. View "Example-Fitness-Trend.png" to see an example graph.
18. "loadFromSave" => This can either be a relative file path("../saves/gen-3-1641769940.json") from "population.py" or false. If this is flase the model will train from scratch, otherwise it will start from a previous save.
19. "saveProgress" => this controls id the best agent from each generation is saved, this allows for the program to be exited and then training to continue where it previously finished.
## Plans/Changes for the future
1. Better way to control the hyperparameter.
2. Make the code more readbale.
3. Add more complex environments.
4. Add a set number of frame per generation.
5. Flappy bird - Increase the speed of the game as the game progresses.
6. Platformer - Increase the speed as the game progresses as this will force the agents to be more efficient.
7. Platformer - Add the option to count going off the left or right side of the screen as dying. This will prevent 'cheaty' methods of completing the game from occuring.
8. Improve the efficiency of the feedforward function of the neural network.
9. Speciation
