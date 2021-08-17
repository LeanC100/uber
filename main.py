from driver import Driver
from user import User

def main():
  driver = Driver("Leandro", "43.543.234")
  car = User("Maria", "40.211.532")

  driver.toPrint()
  car.toPrint()



if __name__ == "__main__":
    main()

