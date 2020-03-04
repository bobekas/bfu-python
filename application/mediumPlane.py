from plane import Plane

class MediumPlane(Plane):
    def __init__(self, planeName, seats, maxSpeed, fuelConsumation, make):
        super().__init__(planeName, seats, maxSpeed, fuelConsumation)
        self.make = make
        self.type = 'Medium Plane'

    # Overwriting function
    def printSpecs(self):
        print (self.name, self.seats, self.maxSpeed, self.fuelConsumation, self.type, self.make)