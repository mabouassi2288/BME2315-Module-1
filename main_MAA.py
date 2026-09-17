from patient_Mona import *

patient1 = Patient(1933004, 80, "Bachelors", 0.97, 1.90, "No dementia")
patient2 = Patient(2033020, 81, "High School", 45.73, 3.87, "Dementia")
patient3 = Patient(2033001, 82, "Bachelors", 2.74, 2.74, "No dementia")
patient4 = Patient(2033002, 97, "High School", 0.15, 2.62, "No dementia")
patient5 = Patient(2033004, 86, "Trade School/Tech School", 80.27, 7.41, "Dementia")
patient6 = Patient(2033005, 99, "High School", 16.16, 1.33, "No dementia")
patient7 = Patient(2033008, 92, "Graduate(PhD/Masters)", 101.83, 2.57, "No dementia")
patient8 = Patient(2033011, 93, "Bachelors", 60.51, 9.54, "Dementia")
patient9 = Patient(2033012, 91, "Graduate(PhD/Masters)", 47.71, 4.55, "No dementia")
patient10 = Patient(2033013, 94, "Trade School/Tech School", 24.78, 3.11, "No dementia")
patient11 = Patient(2033014, 82, "Graduate(PhD/Masters)", 16.14, 3.40, "No dementia")
patient12 = Patient(2033015, 88, "Graduate(PhD/Masters)", 27.61, 1.83, "Dementia")
patient13 = Patient(2033016, 93, "Trade School/Tech School", 21.27, 2.82, "Dementia")
patient14 = Patient(2033017, 69, "Trade School/Tech School", 209.43, 5.88, "Dementia")
patient15 = Patient(2033018, 81, "Graduate(PhD/Masters)", 1412.57, 5.11, "Dementia")


#print(patient15)

#print(patient15.get_age_at_death())

#print(Patient.sum_ages())

#Patient.print_sorted_by("age_at_death")

#Patient.instantiate_from_csv("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/Metadata and Protein Data for Module 1.csv")

#print(Patient.get_patient("1933004"))

dementia_patients = range(len(Patient.filter(Patient.all_patients, cognitive_status = "Dementia")))

print(f'Number of Dementia patients = {len(dementia_patients)}')

no_dementia_patients = range(
len(Patient.filter(Patient.all_patients, cognitive_status="No dementia"))
)

print(f"Number of No dementia patients = {len(no_dementia_patients)}")