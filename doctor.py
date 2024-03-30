# from patient import Patient
#
# class Doctor:
#     def __init__(self, name, specialty):
#         self.name = name
#         self.specialty = specialty
#
#     def examine_patient(self, patient):
#
#         print(f"Doctor {self.name} is examining {patient.name} {patient.age} {patient.gender}.")
#         print(f"{patient.name}'s condition: {patient.condition}")
#
#
#
#     def prescribe_medication(self, patient, medication):
#         print(f"Doctor {self.name} is prescribing {medication} for {patient.name}.")
from patient import Patient

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def examine_patient(self, patient):
        print(f"Doctor {self.name} is examining {patient.name}.")
        print(f"{patient.name}'s condition: {patient.condition}")

    def prescribe_medication(self, patient, medication):
        print(f"Doctor {self.name} is prescribing {medication} for {patient.name}.")

    def prescribe_test(self, patient, test_name, pathology_lab):
        print(f"Doctor {self.name} is prescribing {test_name} for {patient.name}.")
        pathology_lab.conduct_test(test_name, patient)
