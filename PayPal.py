from payment import Payment 

class PayPal(Payment):
    email= str

    def __init__(self, cost, email):
        super().__init__(cost)
        self.email = email

    def toPrint(self):
        print(f'Paid method: Paypal - Cost: {self.cost} - Email: {self.email}' )
