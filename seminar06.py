#ukol a) #ukol b)
class Patient:
    def __init__(self,first_name,last_name, age, diagnosis):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.diagnosis=diagnosis
    def show_information(self):
        print(f"{self.first_name} {self.last_name}, Age: {self.age}, Diagnosis: {self.diagnosis}")

patient1=Patient("Anna", "Smith", 30, "Flu")
patient2=Patient("John", "Doe", 41, "Cold")
patient3=Patient("Alice", "Johnson", 25, "Allergy")
patient4=Patient("Borya", "Jonsonuk", 70, "Diabetes")
patient5=Patient("Petr", "Petrov", 20, "Asthma")

patients=[patient1, patient2, patient3, patient4, patient5]

for patient in patients:
    patient.show_information()

#ukol c)
class Doctor:
    def __init__(self,first_name,second_name, specializace):
        self.first_name=first_name
        self.second_name=second_name
        self.specializace=specializace 
    def info(self):
        print(f"Dr.{self.first_name} {self.second_name} -- {self.specializace}")
doctor1=Doctor("Gregory", "House", "Diagnostics")
doctor2=Doctor("Meredith", "Grey", "Surgery")
doctor3=Doctor("John", "Watson", "General Practice")
doctor4=Doctor("Lisa", "Cuddy", "Endocrinology")

doctors=[doctor1, doctor2, doctor3, doctor4]

for doctor in doctors:
    doctor.info()


diadnosis_to_specialization={
    "Flu":"Diagnostics",
    "Cold":"Diagnostics",
    "Allergy":"General Practice",
    "Diabetes":"Endocrinology",
    "Asthma":"General Practice"
}

assignments=[]
for patient in patients:
    required_specialization = diadnosis_to_specialization.get(
        patient.diagnosis)
    for doctor in doctors:
        if doctor.specializace==required_specialization:
            assignments.append((patient, doctor))
            break
    for patient, doctor in assignments:
        print(f"{patient.first_name} {patient.last_name} is assigned to Dr.{doctor.first_name} {doctor.second_name}")
#ukol e)
class Appointment:
    def __init__(self, patient, doctor, time):
        self.patient = patient
        self.doctor = doctor
        self.time = time
    def show_info(self):
            print(f"Appointment: {self.patient.first_name} {self.patient.last_name} with Dr.{self.doctor.first_name} {self.doctor.second_name} at {self.time}")

appointment_times=["10:00", "11:00", "12:00", "13:00", "14:00"]
appointments=[]
for i, (patient, doctor) in enumerate(assignments):
    appointment=Appointment(patient, doctor, appointment_times[i])
    appointments.append(appointment)
for appointment in appointments:
    appointment.show_info()

#ukol f)

class Hospital:
    def __init__(self, patients):
        self.patients=patients
    def is_registreted (self, first_name, last_name):
        for patient in self.patients:
            if (
                patient.first_name==first_name
                and patient.last_name==last_name
            ):
                 return True
            return False

hospital=Hospital(patients)
print(hospital.is_registreted("Anna", "Smith"))
print(hospital.is_registreted("Borya", "Jonsonuk"))
print(hospital.is_registreted("Nonexistent", "Person"))
