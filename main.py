from driver import Driver
from user import User
from uberX import UberX
from uberXl import UberXl
from uberBlack import UberBlack
from uberBlackSuv import UberBlackSuv

def main():
  #user = User("Maria", "40.211.532")
  #user.toPrint()
  driver1 = Driver("Leandro", "43.543.234")
  driver2 = Driver("Belen", "46.343.754")
  driver3 = Driver("Agustin", "22.312.654")
  driver4 = Driver("Mariana", "50.754.602")

  uber_x = UberX("ASD-132", driver1, "Chevrolet", "Spark")
  uber_xl = UberXl("RGE-432", driver2, "Chevrolet", "Corvette")
  uber_black = UberBlack("LCL-231", driver3, "Porsche", "Macan")
  uber_blacksuv = UberBlackSuv("POS-866", driver4, "Porsche", "Targa")




if __name__ == "__main__":
    main()

