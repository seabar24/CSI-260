from os import makedev
import time

class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        fuelC: The fuel type of the vehicle as a string.
        vin: The VIN (Vehicle Identification Number) of the vehicle as a string.
        sold_on: The date the vehicle was sold.
    """
    base_sale_price = 2000
    wheels = 0
    _vehicles = []

    def __init__(self, miles, make, model, year, fuelC=None, vin=None, sold_on=None):
        """Initialize a Vehicle object."""
        self.miles = int(miles)
        self.make = make
        self.model = model
        self.year = year
        self.fuelC = fuelC
        self.vin = vin
        self.sold_on = sold_on
        self._vehicles.append(self)

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is not None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (0.10 * self.miles)

    def vehicle_type(self):
        """Return a string representing the type of vehicle this is."""
        s = f"This is a {self.year} {self.make} {self.model}"
        return s

    @classmethod
    def vin_ID(cls, vin):
        """Return information about a vehicle with the given VIN."""
        for vehicle in cls._vehicles:
            if vehicle.vin == vin:
                return {
                    'vehicle_type': vehicle.vehicle_type(),
                    'fuelC': getattr(vehicle, 'fuelC', None),
                    'sale_price': vehicle.sale_price(),
                    'purchase_price': vehicle.purchase_price()
                }
        print(f"No vehicle with VIN {vin} exists.")
        time.sleep(2)
