import pickle


class Patient:
    _next_id = 0
    _all_patients = {}

    # Initializes a new patient with the given name, age, and gender
    def __init__(self, first_name, last_name, address, phone_num, emerg_name,
                 emerg_num):
        self._id = Patient._next_id
        Patient._next_id += 1

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_numb = phone_num
        self.emerg_name = emerg_name
        self.emerg_numb = emerg_num
        self.procedures = []  # Initially, no procedures scheduled

        Patient._all_patients[self._id] = self

    # Returns the Patients Information
    def __str__(self):
        return f"Patient ID: {self._id}\nName: {self.first_name} {self.last_name}\nAddress: {self.address}\nPhone Number: {self.phone_numb}\nEmergency Contact: {self.emerg_name} - {self.emerg_numb}\nProcedures: {', '.join(str(proc) for proc in self.procedures)}"

    # Adds procedure to the patient's list of procedures
    def add_procedure(self, procedure, date, practitioner, cost):
        procedure = Procedure(procedure, date, practitioner, cost)
        self.procedures.append(procedure)

    # Gets patient based on ID
    def get_patient():
        id = input("Enter the patient ID: ")
        if id in Patient._all_patients:
            print(Patient._all_patients[id])
        else:
            return None

    # Deletes a patient
    def delete_patient():
        id = input("Enter the patient ID you wish to delete: ")
        if id in Patient.all_patients:
            del Patient.all_patients[id]
        else:
            return None

    # Saves patients to a file
    def save_patient():
        pickle.dump(Patient._all_patients, open("patients.p", "wb"))

    # Loads patients from a file
    def load_patient():
        pickle.load(open("patients.p", "rb"))


class Procedure:
    _next_id = 0
    _all_patients = {}

    #Initiliazes Procedures with the given name, date, practitioner, and cost
    def __init__(self, procedure, date, practitioner, cost):
        self._id = Patient._next_id
        Patient._next_id += 1

        self.procedure = procedure
        self.date = date
        self.practitioner = practitioner
        self.cost = cost
        self.procedures = []  # Initially, no procedures scheduled

        Patient._all_patients[self._id] = self

    # Returns the Procedure Information
    def __self__(self):
        return f"Patient ID: {self._id}\nProcedure: {self.procedure}\nDate: {self.date}\nPractitioner: {self.practitioner}\nCost: {self.cost}"
