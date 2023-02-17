class Elevator:
    def __init__(self, make, floor):
        self.make = make
        self.floor = floor


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        


elevator = Elevator("The Elevator Company", 1)

print(elevator.make) # "The Elevator company"
print(elevator.floor) # 1

car1 = Car("Mazda demio", 2005, "Red")
print(car1.model + " " + car1.color + " " , car1.year)

car2 = Car("BMW", 2010, "Silver Blue")
print(car2.model + " " + car2.color + " " , car2.year)
