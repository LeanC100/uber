from payment import Payment 

class PayPal(Payment):
    email= str

    def __init__(self, cost, email):
        super().__init__(cost)
        self.email = email

    def toPrint(self):
        super().toPrint()
        print(f'Paid method: Paypal - Email: {self.email}' )
