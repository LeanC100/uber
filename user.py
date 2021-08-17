from account import Account

class User(Account):

    def __init__(self, name, document):
        super().__init__(name, document)

    def toPrint(self):
        print(f"User: {self.name} - Document: {self.document}")
