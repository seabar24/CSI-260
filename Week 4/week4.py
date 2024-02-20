"""Module description goes here.

Author: Sean Barrick
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: February 9, 2020 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

from medical import Patient, Procedure
import time
import os

Patient.load_patients("patients.txt")  # Loads previous save if one exists

def modify_attribute(patient, attribute_name, new_value):
    """Modify the given attribute of a patient."""
    if hasattr(patient, attribute_name):
        setattr(patient, attribute_name, new_value)
        print(f"Changed {attribute_name} to {new_value}.")
    else:
        print(f"Attribute '{attribute_name}' does not exist!")
        time.sleep(2)
        Menu()

def modify_patient(patient):
    """Modify attributes or add a procedure for a patient."""
    attributes = {
        "1": "firstname",
        "2": "lastname",
        "3": "address",
        "4": "phone",
        "5": "contact_name",
        "6": "contact_phone",
        "7": "add_procedure",
        " ": Menu
    }
    attribute_choice = input(
        "What attribute would you like to change?\n1. First Name\n2. Last Name\n3. Address\n4. Phone Number\n5. Emergency Contact Name\n6. Emergency Contact Phone Number\n7. Add a Procedure\n\nEnter your choice here or hit 'Enter' to return to Main Menu: ")

    if attribute_choice in attributes:
        attribute_name = attributes[attribute_choice]
        if attribute_name == "add_procedure":
            Patient.add_procedure(patient)
        else:
            new_value = input(f"Enter the new value for attribute {attribute_name}: ")
            modify_attribute(patient, attribute_name, new_value)
    else:
        default_case()

    print("Changed Attribute! Returning to menu...")
    time.sleep(2)
    Menu()

def retrieve_info():
    """Retrieve and perform actions on patient information."""
    patient_id = int(input("Enter patient ID: "))
    patient = Patient.get_patient(patient_id)
    if patient is not None:
        print("\n", patient, "\n")
        switch_dict = {
            "1": lambda: modify_patient(patient),
            "2": Patient.delete_patient,
            "3": Menu
        }
        action = input("1. Modify an Attribute/Add a Procedure\n2. Delete a Patient\n3. Return to Main Menu\n\nEnter the number of the action you want to perform:")
        switch_dict.get(action, default_case)()
    else:
        print("Patient not found!")
        time.sleep(2)
        Menu()

def add_patient():
    """Add a new patient to the dictionary."""
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    address = input("Enter an address: ")
    phone_num = input("Enter a phone number: ")
    emerg_name = input("Enter an emergency contact name: ")
    emerg_num = input("Enter an emergency contact number: ")
    print("Adding patient...")
    time.sleep(2)
    Patient(first_name, last_name, address, phone_num, emerg_name, emerg_num)
    print("Done! Returning to menu...")
    time.sleep(2)
    Menu()

def quit_program():
    """Save and quit the program."""
    print("Saving...")
    time.sleep(2)
    Patient.save_patients("patients.txt")
    print("Quitting...")
    time.sleep(2)
    exit()

def default_case():
    """Default case if none of the options are chosen from menus."""
    print("Nuh uh")
    time.sleep(2)
    Menu()

def Menu():
    """Main Menu Function."""
    switch_dict = {
        "1": retrieve_info,
        "2": add_patient,
        "3": quit_program
    }

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    choice = input("1. Retrieve Patient Info\n2. Add a Patient\n3. Quit\n\nEnter your choice:")
    switch_dict.get(choice, default_case)()

Menu()
