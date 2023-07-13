from car import Car
from account import Account



if __name__ == "__main__":

    print("Hola mundo")
    # car = Car()
    # car.license = "AMSDFLAF"
    # car.driver = "Andres Ferandez"
    # print(vars(car))

    # car2 = Car()
    # car2.license = "QETE342"
    # car2.driver = "Carlos Enrique"
    # print(vars(car2))
    car = Car("AWDFA12",Account("Andrea Villatoro", "ANDREA123"))
    print(vars(car))
    print(vars(car.driver))
    

