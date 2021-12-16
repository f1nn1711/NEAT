class Connection:
    def __init__(self, startNode, endNode):
        self.startNode = startNode
        self.endNode = endNode

        self.weight = 2#(random.random()*2)-1
    
    def feedForward(self):
        inputValue = self.startNode.output

        if not inputValue:
            return None
        
        return inputValue * self.weight

