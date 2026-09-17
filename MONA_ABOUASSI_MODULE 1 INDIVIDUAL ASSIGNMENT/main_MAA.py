from patient_Mona import *

# ---------------------------------------------------------------------------------------------------------------------------
#STEP 7: Make a bar graph that compares the mean (+/- standard deviation) of an attribute that you are interested in between female and male patients 
# ---------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 

# ---------------------------------------------------------------------------------------------------------------------------
#STEP 4:  Create patient objects using the .csv fileDownload .csv file you were provided of patient demographic data and Luminex protein (amyloid beta and Tau) data.
# --------------------------------------------------------------------------------------------------------------------------- 

    #to be sure that you're still creating your patient objects from the .csv data file. 
Patient.instantiate_from_csv("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/MONA_ABOUASSI_MODULE 1 INDIVIDUAL ASSIGNMENT/Metadata and Protein Data for Module 1.csv")

"""
patient1 = Patient(1933004, "Female", 80, "Bachelors", 0.97, 1.90, "No dementia")
patient2 = Patient(2033020, "Male", 81, "High School", 45.73, 3.87, "Dementia")
patient3 = Patient(2033001,"Male", 82, "Bachelors", 2.74, 2.74, "No dementia")
patient4 = Patient(2033002, "Female", 97, "High School", 0.15, 2.62, "No dementia")
patient5 = Patient(2033004, "Male", 86, "Trade School/Tech School", 80.27, 7.41, "Dementia")
patient6 = Patient(2033005, "Female", 99, "High School", 16.16, 1.33, "No dementia")
patient7 = Patient(2033008, "Female", 92, "Graduate(PhD/Masters)", 101.83, 2.57, "No dementia")
patient8 = Patient(2033011, "Female", 93, "Bachelors", 60.51, 9.54, "Dementia")
patient9 = Patient(2033012, "Female", 91, "Graduate(PhD/Masters)", 47.71, 4.55, "No dementia")
patient10 = Patient(2033013, "Male", 94, "Trade School/Tech School", 24.78, 3.11, "No dementia")
patient11 = Patient(2033014, "Female", 82, "Graduate(PhD/Masters)", 16.14, 3.40, "No dementia")
patient12 = Patient(2033015, "Male", 88, "Graduate(PhD/Masters)", 27.61, 1.83, "Dementia")
patient13 = Patient(2033016, "Female", 93, "Trade School/Tech School", 21.27, 2.82, "Dementia")
patient14 = Patient(2033017, "Male", 69, "Trade School/Tech School", 209.43, 5.88, "Dementia")
patient15 = Patient(2033018, "Female", 81, "Graduate(PhD/Masters)", 1412.57, 5.11, "Dementia")
"""


"""
dementia_patients = range(len(Patient.filter(Patient.all_patients, cognitive_status = "Dementia")))

print(f'Number of Dementia patients = {len(dementia_patients)}')

no_dementia_patients = range(
len(Patient.filter(Patient.all_patients, cognitive_status="No dementia"))
)

print(f"Number of No dementia patients = {len(no_dementia_patients)}")
"""

# ---------------------------------------------------------------------------------------------------------------------------
#STEP 5: Sort and print the patients in order based on a specific attribute (e.g., age at diagnosis, highest education level, Thal score, etc.)
# ---------------------------------------------------------------------------------------------------------------------------
Patient.print_sorted_by("age_at_death")
Patient.print_sorted_by("highest_education")
Patient.print_sorted_by("ABeta42") # Optional reverse sorting
Patient.print_sorted_by("pTAU")
Patient.print_sorted_by("cognitive_status")


# ---------------------------------------------------------------------------------------------------------------------------
#STEP 6: Make a class method to filter and print a sub-set of patients based on at least two specific attributes 
# ---------------------------------------------------------------------------------------------------------------------------
Patient.print_patients_in_80s_low_abeta(50.0) 



# ---------------------------------------------------------------------------------------------------------------------------
# STEP 7: Bar Graph comparing Female vs Male ABeta42 levels
# ---------------------------------------------------------------------------------------------------------------------------

    #makes two empty lists that will be populated by female and male patients, respectively
abeta_Female_patients = []
abeta_Male_patients = []

    #populates these two lists using the sex filter
for patient in Patient.filter(Patient.all_patients, sex="Female"):
    abeta_Female_patients.append(patient.ABeta42)
for patient in Patient.filter(Patient.all_patients, sex="Male"):
    abeta_Male_patients.append(patient.ABeta42)

    # Calculate means
x_Female_patient_bar = statistics.mean(abeta_Female_patients)
x_Male_patient_bar = statistics.mean(abeta_Male_patients)

    # Calculate standard deviations
abeta_Female_patient_stdev = statistics.stdev(abeta_Female_patients)
abeta_Male_patient_stdev = statistics.stdev(abeta_Male_patients)

    # Set up bar plot
Patient_sex_cols = ["Female", "Male"]
mean_sex = [x_Female_patient_bar, x_Male_patient_bar]
stdev_sex = [abeta_Female_patient_stdev, abeta_Male_patient_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]

# Assign to Figure 1
plt.figure(1)

plt.bar(
    Patient_sex_cols,
    mean_sex,
    yerr=yerr,
    capsize=10,
    color=["pink", "blue"],
)

plt.title("Average ABeta42 Levels by Sex")
plt.xlabel("Sex")
plt.ylabel("Average ABeta42 Level")

# REMOVE plt.show() FROM HERE!


# ---------------------------------------------------------------------------------------------------------------------------
# STEP 8: Scatter Plot comparing ABeta42 vs pTAU
# ---------------------------------------------------------------------------------------------------------------------------

    #makes two empty lists to hol the values
patient_abeta = []
patient_ptau = []

for patient in Patient.all_patients:
    if patient.pTAU != "n/a":
        patient_abeta.append(patient.ABeta42)
        patient_ptau.append(float(patient.pTAU))

X = patient_abeta  
y = patient_ptau   

# Assign to Figure 2
plt.figure(2)

    #visualize these data on our scatter plot, by typing the following:
plt.scatter(X, y, color='blue')
plt.xlabel('Amyloid-Beta 42 Level')
plt.ylabel('pTAU Level')
plt.title('Scatter Plot of Amyloid-Beta 42 vs pTAU')

# Call a single plt.show() at the very end to open both figure windows together
plt.show()
