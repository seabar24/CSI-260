import Patient
import Procedure
import time

Patient.load_patient() # Loads previous save if one exists

# Default case if none of the options are choen from menus
def default_case():
    print("Nuh uh")
    time.sleep(2)
    Menu()
# Modify's existing patients attributes  
def modify_patient(patient):
    attribute_choice = input("What attribute would you like to change?\n1. First Name\n2. Last Name\n3. Address\n4. Phone Number\n5. Emergency Contact Name\n6. Emergency Contact Phone Number\n\nEnter your choice here: ")

    if attribute_choice in ["1", "2", "3", "4", "5", "6"]:
        new_value = input(f"Enter the new value for attribute {attribute_choice}: ")
        if attribute_choice == "1":
            patient.first_name = new_value
        elif attribute_choice == "2":
            patient.last_name = new_value
        elif attribute_choice == "3":
            patient.address = new_value
        elif attribute_choice == "4":
            patient.phone_numb = new_value
        elif attribute_choice == "5":
            patient.emerg_name = new_value
        elif attribute_choice == "6":
            patient.emerg_numb = new_value
    else:
        default_case()

    print("Changed Attribute! Returning to menu...")
    time.sleep(2)
    Menu()
# Retrieves Patient info based on ID and gives a new menu
def retrieve_info():
    Patient.get_patient()
    switch_dict = {

        "1": modify_patient,
        "2": Patient.del_patient,
        "3": Patient.add_procedure
    }
    switch_dict.get(input("1. Modify an Attribute\n2.Delete a Patient\n3. Add a Procedure\n\nEnter the number of the action you want to perform:"), default_case)
    Menu()
# Adds a new patient to the dictionary
def add_patient():
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
# Saves and Quits the program
def quit():
    print("Saving...")
    time.sleep(2)
    Patient.save_patient()
    print("Quitting...")
    time.sleep(2)
    exit()
# Main Menu
def Menu():
    switch_dict = {
        
        "1": retrieve_info,
        "2": add_patient,
        "3": quit
    }
    switch_dict.get(input("What would you like to do?\n\n1: Lookup a Patient\n2: Add a Patient\n3: Quit\n\nChoice: "), default_case)()
Menu()
