# NEAT
## How does NEAT work?
An implementation of the NEAT(Neuro Evolution of Augmenting Topologies). NEAT combines neural networks and a genetic algorithm, in traditional neural networks the network weights and biases are adjusted by an optimization function (for example: stochastic gradient decent, adaptive moment estimation). In the NEAT algorithm the weights and biases are adjusted by random mutations. In traditional neural network the structure of the network is pre-defined in the hyper parameters and stay constants through the training process. In NEAT the structure of the nerual network can change throughout the training process through survival of the fittest. There is a chance that a mutation will occur where a new neuron or connection will be added to the network. In addition to this the weights and biases can under go mutations to allow them to change and improve over time.
## The advantages of NEAT
By allowing the structure of the neural network to change over time it also means that the most efficient network model can be found as well as the best weights and biases.
## The hyperparameters
Firstly a parameter is something that can be changed, when refering to a neural network an example of a parameter would be a weight or a bias. These are things that can be chnaged during the training process. A hyperparameter is something that can't be change during the training process. Here are the hyperparameters that can be set for this program:
1. "populationSize" => 100 => The number of agents per generation (Any integer >0)
2. "networkInputs" => 5 => The number of inputs to the neural network (Any integer >0)
3. "networkOutputs" => 1 => The number of output to the neural network (Any integer >0)
4. "initHiddenNodes" => 0 => The number of hidden nodes by default (Any integer >=0)
5. "initConnections" => 1 => The number of random connections by default (Any integer >=0)
6. "ouputActivationFunction" => "sigmoid" => The activation function that will be used by the output node.
7. "higherIsBetter" => true => Determines if the higher the fitness the more likely it is to survive (Boolean)
8. "forceNewNodeConnections" => false => Determines if a new node gets created, will it be connected to two other nodes. (Boolean)
9. "survivalRate" => 0.4 => The top n*100 survive to the next generation, e.g if the survial rate is 0.4 with a population size of 200, the top 80 would survive to the next round. (Float 0<=n<=1)
10. "nodeMutationRate" => 0 => This is the chance that a new node will be added to the model. (Float 0<=n<=1)
11. "nodeMutationDecay" => 0 => This is the rate at which the chance a new node is added to the model decays. (Float 0<=n<=1)
12. "connectionMutationRate" => 0 => s is the rate at which the chance a new connection is added to the model decays. (Float 0<=n<=1)
13. "connectionMutationDecay" => 0 => This is the rate at which the chance a connection node is added to the model decays. (Float 0<=n<=1)
14. "weightMutationRate" => 0 => This is the chance that a weight from the network is randomised. (Float 0<=n<=1)
15. "weightMutationDecay" => 0 => This is the rate at which the chance of a weight mutating decays. (Float 0<=n<=1)
16. "biasMutationRate" => 0 => This is the chance that a bias from the network is randomised. (Float 0<=n<=1)
17. "biasMutationDecay" => 0 => This is the rate at which the chance of a bias mutating decays. (Float 0<=n<=1)
