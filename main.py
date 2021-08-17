from driver import Driver
from user import User
from uberX import UberX
from uberXl import UberXl
from uberBlack import UberBlack
from uberBlackSuv import UberBlackSuv
from PayPal import PayPal
from creditCard import CreditCard
from cash import Cash 
from route import Route
from trip import Trip
def main():
  #user = User("Maria", "40.211.532")
  driver1 = Driver("Leandro", "43.543.234")
  #driver2 = Driver("Belen", "46.343.754")
  #driver3 = Driver("Agustin", "22.312.654")
  #driver4 = Driver("Mariana", "50.754.602")

  uber_x = UberX("ASD-132", driver1, "Chevrolet", "Spark")
  #uber_xl = UberXl("RGE-432", driver2, "Chevrolet", "Corvette")
  #uber_black = UberBlack("LCL-231", driver3, "Porsche", "Macan")
  #uber_blacksuv = UberBlackSuv("POS-866", driver4, "Porsche", "Targa")

  paypal = PayPal (323.29 , 'leandro@gmail.com')
  credit_card = CreditCard(323.29, 'Leonel Messi','3534 5354 6546 5643', '32/38', '547')
  #cash = Cash (323.29)
  
  route = Route('av. santa 211', 'lisa 9291')

  trip = Trip(uber_x, route, credit_card)
  trip.toPrint()


if __name__ == "__main__":
    main()

