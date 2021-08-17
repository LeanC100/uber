from payment import Payment 

class Cash(Payment):

    def __init__(self, cost):
        super().__init__(cost)

    def toPrint(self):
        print(f'Paid method: Cash - Cost: {self.cost} ')
