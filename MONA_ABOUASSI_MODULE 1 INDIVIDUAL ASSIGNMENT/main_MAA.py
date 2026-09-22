from patient_Mona import *

# ---------------------------------------------------------------------------------------------------------------------------
#STEP 7: Make a bar graph that compares the mean (+/- standard deviation) of an attribute that you are interested in between female and male patients 
# ---------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 
import pandas as pd
from sklearn.linear_model import LinearRegression #for the line of best fit

# ---------------------------------------------------------------------------------------------------------------------------
#STEP 4:  Create patient objects using the .csv fileDownload .csv file you were provided of patient demographic data and Luminex protein (amyloid beta and Tau) data.
# --------------------------------------------------------------------------------------------------------------------------- 

    #to be sure that you're still creating your patient objects from the .csv data file. 
Patient.instantiate_from_csv("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/MONA_ABOUASSI_MODULE 1 INDIVIDUAL ASSIGNMENT/Metadata and Protein Data for Module 1.csv")


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
#Patient.print_sorted_by("highest_education")
#Patient.print_sorted_by("ABeta42") # Optional reverse sorting
#Patient.print_sorted_by("pTAU")
#Patient.print_sorted_by("cognitive_status")


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


# T-TEST -----------------------------------------------
print(" ")
t_stat, p_val = stats.ttest_ind(abeta_Female_patients, abeta_Male_patients)
print(f't_stat = {t_stat}, p_val = {p_val}')


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

X = patient_abeta  #independent variable
y = patient_ptau   #dependent variable

#Linear Regression 
X = np.array(patient_abeta).reshape(-1,1)
y = np.array(patient_ptau)

model = LinearRegression()
model.fit(X, y)


# Annotate equation
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X,y)

equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"
plt.text(X.max(), y.max(), equation, color="red", fontsize=12, verticalalignment="top")


# Assign to Figure 2
plt.figure(2)


    #visualize these data on our scatter plot, by typing the following:
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color="red")
plt.xlabel('Amyloid-Beta 42 Level')
plt.ylabel('pTAU Level')
plt.title('Scatter Plot of Amyloid-Beta 42 vs pTAU')
plt.scatter(X,y, color = "blue")
plt.plot(X,model.predict(X), color = "red")


# Call a single plt.show() at the very end to open both figure windows together
plt.show()




#do an outlier test for a better grade
#do more than one scatter plot and bar graph