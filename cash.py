from payment import Payment 

class Cash(Payment):

    def __init__(self, cost):
        super().__init__(cost)

    def toPrint(self):
        super().toPrint()
        print(f'Paid method: Cash')
