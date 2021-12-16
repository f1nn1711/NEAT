import random
import activation as AF

class Node:
    def __init__(self, isInput, isOutput, activation='linear'):
        self.isInput = isInput
        self.isOutput = isOutput
        self.activation = AF.activationFunctions[activation]
    
        self.bias = 0# (random.random()*2)-1 # This scales the bias to be between -1 and 1

        self.output = None
    
    def process(self, inputValues):
        summedValues = sum(inputValues) + self.bias
        self.output = self.activation.transform(summedValues)
        return self.output
