class Payment:
    id = int
    cost = float

    def __init__ (self,cost):
        self.cost = cost    

    def toPrint(self):
        print(f'Cost: {self.cost}')    
