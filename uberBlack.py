from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatMaterial = []

    def __init__(self, license, driver, typeCarAccepted, seatMaterial):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatMaterial = seatMaterial

    def toPrint(self):
        super().toPrint()
        print(f'Brand: {self.typeCarAccepted} - Model {self.seatMaterial}')
