"""
Define classes Car, Truck, and Motorcycle in this file.
They should extend the Vehicle base class.
"""
from vehicle import Vehicle

class Car(Vehicle):
    """Car class."""
    wheels = 4
    type = "car"

    def __init__(self, miles, make, model, year, fuelC=None, vin=None):
        """Initialize Car object."""
        fuelC = input("What is the fuel type of the car?")
        vin = input("What is the VIN number?")
        self.fuelC = fuelC
        self.vin = vin
        super().__init__(miles, make, model, year, fuelC, vin)

    def __str__(self):
        """String representation of Car object."""
        s = super().vehicle_type()
        s = s + "\n VIN: " + str(self.vin)
        s = s + "\n Year: " + str(self.miles)
        s = s + "\n Miles: " + str(self.make)
        s = s + "\n Fuel Type: " + str(self.fuelC)
        return s


class Truck(Vehicle):
    """Truck class."""
    wheels = 6
    type = "truck"

    def __init__(self, miles, make, model, year, fuelC=None, vin=None):
        """Initialize Truck object."""
        fuelC = input("What is the fuel type of the car?")
        vin = input("What is the VIN number?")
        self.fuelC = fuelC
        self.vin = vin
        super().__init__(miles, make, model, year, fuelC, vin)

    def __str__(self):
        """String representation of Truck object."""
        s = super().vehicle_type()
        s = s + "\n VIN: " + str(self.vin)
        s = s + "\n Year: " + str(self.miles)
        s = s + "\n Miles: " + str(self.make)
        s = s + "\n Fuel Type: " + str(self.fuelC)
        return s


class Motorcycle(Vehicle):
    """Motorcycle class."""
    wheels = 2
    type = "motorcycle"

    def __init__(self, miles, make, model, year, fuelC=None, vin=None):
        """Initialize Motorcycle object."""
        fuelC = input("What is the fuel type of the car?")
        vin = input("What is the VIN number?")
        self.fuelC = fuelC
        self.vin = vin
        super().__init__(miles, make, model, year, fuelC, vin)

    def __str__(self):
        """String representation of Motorcycle object."""
        s = super().vehicle_type()
        s = s + "\n VIN: " + str(self.vin)
        s = s + "\n Year: " + str(self.miles)
        s = s + "\n Miles: " + str(self.make)
        s = s + "\n Fuel Type: " + str(self.fuelC)
        return s
