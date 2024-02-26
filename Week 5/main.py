from vehicle_types import Car, Truck, Motorcycle
from vehicle import Vehicle
import time
import os


def default_case():
    """Default case function."""
    print("Nuh uh")
    time.sleep(2)
    Menu()


def Quit():
    """Quit function."""
    print("Goodbye")
    time.sleep(2)
    exit()


def display_vehicle():
    """Display vehicle function."""
    vin = input("What is the VIN number?")
    info = Vehicle.vin_ID(vin)
    if info:
        print(f"\n{info['vehicle_type']}")
        print(f"Fuel Type: {info['fuelC']}")
        print(f"Sale Price: ${info['sale_price']}")
        print(f"Purchase Price: ${info['purchase_price']}")
        time.sleep(5)
    Menu()


def type_car():
    """Type car function."""
    miles = input("How many miles has the car been driven?")
    make = input("What is the make of the car?")
    model = input("What is the model of the car?")
    year = input("What year was the car built?")
    car = Car(miles, make, model, year)
    print(f"\n{car}")
    time.sleep(2)
    Menu()


def type_truck():
    """Type truck function."""
    miles = input("How many miles has the truck been driven?")
    make = input("What is the make of the truck?")
    model = input("What is the model of the truck?")
    year = input("What year was the truck built?")
    truck = Truck(miles, make, model, year)
    print(f"\n{truck}")
    time.sleep(2)
    Menu()


def type_motorcycle():
    """Type motorcycle function."""
    miles = input("How many miles has the motorcycle been driven?")
    make = input("What is the make of the motorcycle?")
    model = input("What is the model of the motorcycle?")
    year = input("What year was the motorcycle built?")
    motor = Motorcycle(miles, make, model, year)
    print(f"\n{motor}")
    time.sleep(2)
    Menu()


def add_vehicle():
    """Add vehicle function."""
    vehicle_type = input("What type of vehicle would you like to add"
                         "\n\nCar\nTruck\nMotorcycle\n\nInput: ")
    if vehicle_type.lower() == "car":
        type_car()
    elif vehicle_type.lower() == "truck":
        type_truck()
    elif vehicle_type.lower() == "motorcycle":
        type_motorcycle()
    else:
        print("Nuh uh")
        time.sleep(2)
        add_vehicle()


def Menu():
    """Main Menu Function."""
    switch_dict = {
        "1": display_vehicle,
        "2": add_vehicle,
        "3": Quit
    }

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    choice = input("1. Display a Vehicle\n2. Add a Vehicle\n3. "
                   "Quit\n\nEnter your choice:")
    switch_dict.get(choice, default_case)()


Menu()
