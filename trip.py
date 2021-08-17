from car import Car
from route import Route
from payment import Payment

class Trip:
    id = int
    car = Car
    route = Route
    payment = Payment

    def __init__(self, car, route,payment):
        self.car = car
        self.route = route
        self.payment = payment

    def toPrint(self):
        self.car.driver.toPrint()
        self.route.toPrint()
        self.payment.toPrint()

