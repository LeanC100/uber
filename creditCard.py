from payment import Payment

class CreditCard(Payment):

    name_complete = str
    number = int 
    expiration = str
    cvv = int 

    def __init__(self, cost, name_complete, number, expiration,cvv):
        super().__init__(cost)
        self.name_complete = name_complete
        self.number =  number
        self.expiration = expiration
        self.cvv = cvv

    def toPrint(self):
        print(f'Paid method: Paypal - Cost: {self.cost} - Name Complete: {self.name_complete} - Number: {self.number} - Expiration: {self.expiration}, CVV: {self.cvv}')
