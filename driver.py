from account import Account

class Driver(Account):

    def __init__(self, name, document):
        super().__init__(name, document)

    def toPrint(self):
        print(f"Driver: {self.name} - Document: {self.document}")
