import pickle

class Patient:
    _next_patient_id = 1
    _all_patients = {}

    def __init__(self, fname, lname, address, phone, contact_name, contact_phone):
        self.firstname = fname
        self.lastname = lname
        self.address = address
        self.phone = phone
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.ID = Patient._next_patient_id
        Patient._next_patient_id += 1
        self.procedures = []
        Patient._all_patients[self.ID] = self

    def __str__(self):
        patient_info = f"Patient ID: {self.ID}\nName: {self.firstname} {self.lastname}\nAddress: {self.address}\nPhone: {self.phone}\nEmergency Contact: {self.contact_name} ({self.contact_phone})"
        procedures_info = "\nProcedures:"
        for proc in self.procedures:
            procedures_info += f"\n{proc.__str__()}"
        return f"{patient_info}{procedures_info}"
    
    @classmethod
    def add_procedure(cls):
        name = input("Enter name of the procedure:") 
        date = input("Enter the date of the procedure:")
        practitioner = input("Enter the name of the practioner:"), 
        cost = float(input(f"Enter the cost of {name}:"))
        procedure = Procedure(name, date, practitioner, cost)
        cls._all_patients[cls._next_patient_id].procedures.append(procedure)

    @classmethod
    def get_patient(cls, patient_id):
        if patient_id in cls._all_patients:
            return cls._all_patients.get(patient_id)
        else:
            return None

    @classmethod
    def delete_patient(cls, patient_id):
        if patient_id in cls._all_patients:
            del cls._all_patients[patient_id]

    @classmethod
    def save_patients(cls, filename):
        with open(filename, 'wb') as file:
            pickle.dump(cls._all_patients, file)

    @classmethod
    def load_patients(cls, filename):
        try:
            with open(filename, 'rb') as file:
                cls._all_patients = pickle.load(file)
                cls._next_patient_id = max(cls._all_patients.keys(), default=0) + 1
        except FileNotFoundError:
            cls._all_patients = {}
            cls._next_patient_id = 1

class Procedure:
    _next_procedure_id = 1

    def __init__(self, name, date, practitioner, cost):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.cost = cost
        self.ID = Procedure._next_procedure_id
        Procedure._next_procedure_id += 1

    def __str__(self):
        return f"Procedure ID: {self.ID}\nName: {self.name}\nDate: {self.date}\nPractitioner: {self.practitioner}\nCost: {self.cost}"
