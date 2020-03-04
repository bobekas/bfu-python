class Plane:

    def __init__(self, planeName, seats, maxSpeed, fuelConsumation):
        self.name = planeName
        self.seats = seats
        self.maxSpeed = maxSpeed
        self.fuelConsumation = fuelConsumation
        self.length = 40
    def printSpecs(self):
        print (self.name, self.seats, self.maxSpeed, self.fuelConsumation)

    def printMaxSpeed(self):
        print ('Plane max speed: ' + str(self.maxSpeed))