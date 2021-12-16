import math

class ActivationFunction:
    def __init__(self):
        pass
    
    def transform(self, value):
        return value

class Binary(ActivationFunction):
    def __init__(self):
        super().__init__()

    def transform(self, value):
        if value < 0:
            return 0
        else:
            return 1

class Sigmoid(ActivationFunction):
    def __init__(self):
        super().__init__()

    def transform(self, value):
        return 1/(1+(math.e**(-value)))

class Tanh(ActivationFunction):
    def __init__(self):
        super().__init__()

    def transform(self, value):
        numerator = (math.e**value) - (math.e**(-value))
        denominator = (math.e**value) + (math.e**(-value))
        return numerator/denominator

class ReLU(ActivationFunction):
    def __init__(self):
        super().__init__()

    def transform(self, value):
        return max(0,value)

class LeakyReLU(ActivationFunction):
    def __init__(self):
        super().__init__()

    def transform(self, value):
        return max(0.1*value,value)

activationFunctions = {
    'linear' : ActivationFunction,
    'binary' : Binary,
    'sigmoid' : Sigmoid,
    'tanh' : Tanh,
    'relu' : ReLU,
    'leaky_relu' : LeakyReLU
}