#AI USAGE STATEMENT: 
#Used AI to create an ANOVA and p-value statistical analysis test with code.
#Used AI multiple times to see what was wrong with my code and how to fix it.
#Used AI to help with specific attributes on my graphs, such as how to move the text to the corner of the graph.
#Used AI to help with formatting and organizing the code for better readability and maintainability.

from patient_Mona import * #imports the patient file that has all necessary methods to gather and analyze patient data

# ---------------------------------------------------------------------------------------------------------------------------
#STEP 7: Import everything necessary to make a bar graph that compares the mean (+/- standard deviation) of an attribute that you are interested in between female and male patients 
# ---------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 
import pandas as pd
from sklearn.linear_model import LinearRegression #for the line of best fit

#Prints the title and beginning information
print("\n" + "=" * 60)
print("Hello and welcome to Mona and Cecilia's Module 1 Project!")
print("=" * 60)
print("All the data in this module has come from Metadata and Protein Data that Alzheimer's patients have graciously and selflessly provided for us.")
print(" ")
print("\n" + "=" * 60)
print("HEADERS")
print("=" * 60)
print("The following are the headers included in the dataset, printed individually for reference.")
print(" ")

# Opens CSV file and prints each column line by line
with open(
    "/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/Metadata and Protein Data for Module 1 copy.csv",
    newline=""
) as f:
    reader = csv.reader(f)
    headers = next(reader)  # Get the first row

    for h in headers:
        print(h)         

print("\n" + "=" * 60)
print("DATASET VARIABLES INCLUDED IN ANALYSIS")
print("=" * 60)
print("In our analysis, we will be focusing on the following variables from the dataset:")
print("- pTAU levels")
print("- ABeta42 levels (individually and by sex)")
print("- Age of Diagnosis")
print("- Age of Onset Symptoms")
print("- Last MMSE Score")
print("  ")
print("To demonstrate how the dataset can be sorted by different variables, the patients are shown below in ascending order of pTAU levels.")


# ---------------------------------------------------------------------------------------------------------------------------
#STEP 4:  Create patient objects using the .csv fileDownload .csv file you were provided of patient demographic data and Luminex protein (amyloid beta and Tau) data.
# --------------------------------------------------------------------------------------------------------------------------- 

    #to be sure that you're still creating your patient objects from the .csv data file. 
Patient.instantiate_from_csv("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/Metadata and Protein Data for Module 1 copy.csv")

# ---------------------------------------------------------------------------------------------------------------------------
#STEP 5: Sort and print the patients in order based on a specific attribute (e.g., age at diagnosis, highest education level, Thal score, etc.)
# ---------------------------------------------------------------------------------------------------------------------------
#Patient.print_sorted_by("age_at_death")
#Patient.print_sorted_by("ABeta42") # Optional reverse sorting
Patient.print_sorted_by("pTAU")
#Patient.print_sorted_by("cognitive_status")
#Patient.print_sorted_by("age_of_diagnosis")
#Patient.print_sorted_by("age_of_onset_symptoms")


# ---------------------------------------------------------------------------------------------------------------------------
#STEP 6: Make a class method to filter and print a sub-set of patients based on at least two specific attributes 
# ---------------------------------------------------------------------------------------------------------------------------

print(" ")
print("We can also filter the dataset using multiple attributes. This is demonstrated below by displaying patients who passed away in their 80s and had ABeta42 levels below 50.0.")

Patient.print_patients_in_80s_low_abeta(50.0) 



# ---------------------------------------------------------------------------------------------------------------------------
# STEP 7: Bar Graph comparing Average MMSE Scores by Age of Diagnosis
# ---------------------------------------------------------------------------------------------------------------------------

print("\n" + "=" * 60)
print("BAR GRAPH: AVERAGE MMSE SCORE BY AGE OF DIAGNOSIS")
print("=" * 60)
print(" ")
print("The bar graph compares average MMSE scores among patients diagnosed at different ages.")


    #makes two empty lists that will be populated by female and male patients, respectively
mmse_under_70 = []
mmse_70_79 = []
mmse_80_plus = []

    #populates these lists using the age of diagnosis filter
for patient in Patient.all_patients:

    if patient.age_of_diagnosis is not None and patient.last_MMSE_score is not None:

        if patient.age_of_diagnosis < 70:
            mmse_under_70.append(float(patient.last_MMSE_score))

        elif 70 <= patient.age_of_diagnosis < 80:
            mmse_70_79.append(float(patient.last_MMSE_score))

        else:
            mmse_80_plus.append(float(patient.last_MMSE_score))

    # Calculate means
mean_under_70 = statistics.mean(mmse_under_70)
mean_70_79 = statistics.mean(mmse_70_79)
mean_80_plus = statistics.mean(mmse_80_plus)

    # Calculate standard deviations
stdev_under_70 = statistics.stdev(mmse_under_70)
stdev_70_79 = statistics.stdev(mmse_70_79)
stdev_80_plus = statistics.stdev(mmse_80_plus)

    # Set up bar plot
diagnosis_groups = ["Under 70", "70-79", "80+"]

mean_mmse = [
    mean_under_70,
    mean_70_79,
    mean_80_plus
]

stdev_mmse = [
    stdev_under_70,
    stdev_70_79,
    stdev_80_plus
]

yerr = [np.zeros(len(mean_mmse)), stdev_mmse]

# BAR GRAPH
plt.figure(1)

plt.bar(
    diagnosis_groups,
    mean_mmse,
    yerr=yerr,
    capsize=10,
    color=["green", "blue", "purple"]
)

plt.title("Average MMSE Score by Age of Diagnosis")
plt.xlabel("Age of Diagnosis")
plt.ylabel("Average MMSE Score")


# ANOVA TEST CODE -----------------------------------------------

# Runs a one-way ANOVA test to compare the mean MMSE scores across the three age-of-diagnosis groups
f_stat, p_val = stats.f_oneway(
    mmse_under_70,   # MMSE scores for patients diagnosed before age 70
    mmse_70_79,      # MMSE scores for patients diagnosed between ages 70 and 79
    mmse_80_plus     # MMSE scores for patients diagnosed at age 80 or older
)

# Creates formatted text that summarizes the ANOVA results
anova_text = (
    f"ANOVA\n"               # Labels the statistical test as ANOVA
    f"F = {f_stat:.2f}\n"    # Displays the F-statistic rounded to 2 decimal places
    f"p = {p_val:.4f}"       # Displays the p-value rounded to 4 decimal places
)

plt.text(
    0.05, 0.95,
    anova_text,
    color= "red",
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment="top",
    horizontalalignment="left"
)

print("ANOVA statistical analysis: ")
print(f"F-statistic = {f_stat}")
print(f"p-value = {p_val}")


# ---------------------------------------------------------------------------------------------------------------------------
# STEP 8: Scatter Plot comparing pTAU vs last MMSE Score
# ---------------------------------------------------------------------------------------------------------------------------

print("\n" + "=" * 60)
print("SCATTER PLOT: PTAU VS LAST MMSE SCORE")
print("=" * 60)
print(" ")
print("A scatter plot is generated to show the correlation between pTAU and last MMSE scores in patients.")
    
    #makes two empty lists to hol the values
patient_ptau = []
patient_mmse = []

for patient in Patient.all_patients:
    if patient.pTAU != "n/a" and patient.last_MMSE_score is not None:
        patient_ptau.append(float(patient.pTAU))
        patient_mmse.append(float(patient.last_MMSE_score))

#convert lists to numpy array first, then do outlier test
patient_ptau = np.array(patient_ptau)
patient_mmse = np.array(patient_mmse)


#***********************
# OUTLIER TEST USING IQR
#***********************

# Find the first quartile (Q1) and third quartile (Q3) for pTAU values
Q1_ptau = np.percentile(patient_ptau, 25)
Q3_ptau = np.percentile(patient_ptau, 75)

# Calculate the interquartile range (IQR) for pTAU
IQR_ptau = Q3_ptau - Q1_ptau

# Calculate the lower and upper limits used to identify pTAU outliers
lower_ptau = Q1_ptau - 1.5 * IQR_ptau
upper_ptau = Q3_ptau + 1.5 * IQR_ptau


# Find the first quartile (Q1) and third quartile (Q3) for Last MMSE Scores
Q1_mmse = np.percentile(patient_mmse, 25)
Q3_mmse = np.percentile(patient_mmse, 75)

# Calculate the interquartile range (IQR) for Last MMSE Scores
IQR_mmse = Q3_mmse - Q1_mmse

# Calculate the lower and upper limits used to identify MMSE outliers
lower_mmse = Q1_mmse - 1.5 * IQR_mmse
upper_mmse = Q3_mmse + 1.5 * IQR_mmse


# Creates a Boolean array that marks data points as True if they are within
# the acceptable IQR range for BOTH pTAU and MMSE
non_outliers = (
    (patient_ptau >= lower_ptau) &    # pTAU value is above the lower bound
    (patient_ptau <= upper_ptau) &    # pTAU value is below the upper bound
    (patient_mmse >= lower_mmse) &    # MMSE score is above the lower bound
    (patient_mmse <= upper_mmse)      # MMSE score is below the upper bound
)


# Prints a heading before displaying any detected outliers
print("\nOutliers detected:")

# Pairs together the pTAU and MMSE values that were identified as outliers
for ptau, mmse in zip(
    patient_ptau[~non_outliers],      # Selects pTAU values marked as outliers
    patient_mmse[~non_outliers]       # Selects MMSE values marked as outliers
):
    # Prints the pTAU and MMSE values for each detected outlier
    print(f"pTAU = {ptau}, Last MMSE Score = {mmse}")


# Removes the outliers and keeps only the pTAU values within the accepted range
patient_ptau_filtered = patient_ptau[non_outliers]

# Removes the matching MMSE values so the x- and y-data stay paired correctly
patient_mmse_filtered = patient_mmse[non_outliers]

#now for the linear regression analysis using the filtered data
X = patient_mmse  #independent variable
y = patient_ptau   #dependent variable

#Linear Regression 
X = patient_ptau_filtered.reshape(-1, 1)
y = patient_mmse_filtered

model = LinearRegression()
model.fit(X, y)

#***********************
#p-value calculation
#***********************

# Calculates the Pearson correlation coefficient (r) and p-value
# between the x-values and y-values
r_value, p_value = stats.pearsonr(
    X.flatten(),  # Converts X from a 2D array into a 1D array for pearsonr()
    y             # y-values being compared with X
)

# Prints the Pearson correlation coefficient
# r shows the direction and strength of the linear relationship
print(f"Pearson correlation = {r_value}")

# Prints the p-value
# p < 0.05 generally indicates a statistically significant relationship
print(f"p-value = {p_value}")


#visualize these data on our scatter plot, by typing the following:
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color="red")

plt.xlabel("pTAU Level")
plt.ylabel("Last MMSE Score")
plt.title("pTAU vs Last MMSE Score")


# Annotate equation
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X,y)

equation = (
    f"y = {slope:.2f}x + {intercept:.2f}\n"
    f"R^2 = {r2:.2f}\n"
    f"p = {p_value:.4f}"
)
plt.text(
    0.75, 0.95,
    equation,
    transform=plt.gca().transAxes,
    color="red",
    fontsize=12,
    verticalalignment="top",
    horizontalalignment="left"
)


# Call a single plt.show() at the very end to open both figure windows together


# ---------------------------------------------------------------------------------------------------------------------------
# STEP 9: Scatter Plot comparing ABeta42 and Last MMSE Score
# ---------------------------------------------------------------------------------------------------------------------------

print("\n" + "=" * 60)
print("SCATTER PLOT: ABETA42 VS LAST MMSE SCORE")
print("=" * 60)
print(" ")
print("A scatter plot is generated to show the correlation between ABeta42 levels and Last MMSE Scores in patients.") 

    
    #makes two empty lists to hol the values
patient_abeta = []
patient_mmse = []

# Only include patients that have an MMSE score
for patient in Patient.all_patients:
    if patient.last_MMSE_score not in (None, "n/a", ""):
        patient_abeta.append(patient.ABeta42)
        patient_mmse.append(float(patient.last_MMSE_score))



# Linear Regression
X = np.array(patient_abeta).reshape(-1, 1)
y = np.array(patient_mmse)

model = LinearRegression()
model.fit(X, y)

#***********************
# OUTLIER TEST USING IQR
#***********************

# Convert the ABeta42 and MMSE lists into NumPy arrays
# so Boolean filtering can be used later
patient_abeta = np.array(patient_abeta)
patient_mmse = np.array(patient_mmse)


# Find the first quartile (Q1) and third quartile (Q3) for ABeta42
Q1_abeta = np.percentile(patient_abeta, 25)
Q3_abeta = np.percentile(patient_abeta, 75)

# Calculate the interquartile range (IQR) for ABeta42
IQR_abeta = Q3_abeta - Q1_abeta

# Calculate the lower and upper bounds used to identify ABeta42 outliers
lower_abeta = Q1_abeta - 1.5 * IQR_abeta
upper_abeta = Q3_abeta + 1.5 * IQR_abeta


# Find the first quartile (Q1) and third quartile (Q3) for Last MMSE Score
Q1_mmse = np.percentile(patient_mmse, 25)
Q3_mmse = np.percentile(patient_mmse, 75)

# Calculate the interquartile range (IQR) for MMSE scores
IQR_mmse = Q3_mmse - Q1_mmse

# Calculate the lower and upper bounds used to identify MMSE outliers
lower_mmse = Q1_mmse - 1.5 * IQR_mmse
upper_mmse = Q3_mmse + 1.5 * IQR_mmse


# Create a Boolean array marking points as True if BOTH
# ABeta42 and MMSE values fall within the acceptable IQR ranges
non_outliers = (
    (patient_abeta >= lower_abeta) &   # ABeta42 is above the lower bound
    (patient_abeta <= upper_abeta) &   # ABeta42 is below the upper bound
    (patient_mmse >= lower_mmse) &     # MMSE is above the lower bound
    (patient_mmse <= upper_mmse)       # MMSE is below the upper bound
)


# Print a heading before displaying any detected outliers
print("\nOutliers detected:")

# Pair together the ABeta42 and MMSE values identified as outliers
for abeta, mmse in zip(
    patient_abeta[~non_outliers],      # Select ABeta42 values marked as outliers
    patient_mmse[~non_outliers]        # Select matching MMSE values marked as outliers
):
    # Print each detected outlier pair
    print(f"ABeta42 = {abeta}, Last MMSE Score = {mmse}")


# Remove the outliers and keep only the valid ABeta42 values
patient_abeta_filtered = patient_abeta[non_outliers]

# Remove the matching MMSE values so the x- and y-data stay paired correctly
patient_mmse_filtered = patient_mmse[non_outliers]

#Make X and Y the filtered list to keep the outliers out
X = patient_abeta_filtered.reshape(-1, 1)
y = patient_mmse_filtered

#***********************
#p-value calculation
#***********************
r_value, p_value = stats.pearsonr(X.flatten(), y)

print(f"Pearson correlation = {r_value}")
print(f"p-value = {p_value}")

#SCATTER PLOT
plt.figure(3)


    #visualize these data on our scatter plot, by typing the following:
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color="red")

plt.xlabel('ABeta42 Level')
plt.ylabel('Last MMSE Score')
plt.title('ABeta42 vs Last MMSE Score')


# Annotate equation
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X,y)

equation = equation = (
    f"y = {slope:.2f}x + {intercept:.2f}\n"
    f"R^2 = {r2:.2f}\n"
    f"p = {p_value:.4f}"
)
plt.text(
    0.75, 0.95,
    equation,
    transform=plt.gca().transAxes,
    color="red",
    fontsize=12,
    verticalalignment="top",
    horizontalalignment="left"
)



# ---------------------------------------------------------------------------------------------------------------------------
# STEP 10: Scatter Plot comparing Age of Diagnosis vs Age of Onset Symptoms
# ---------------------------------------------------------------------------------------------------------------------------

print("\n" + "=" * 60)
print("SCATTER PLOT: AGE OF DIAGNOSIS VS AGE OF ONSET SYMPTOMS")
print("=" * 60)
print(" ")
print("A scatter plot is generated to show the correlation between Age of Diagnosis and Age of Onset Symptoms in patients.")
    
    #makes two empty lists to hol the values
patient_age_of_diagnosis = []
patient_age_of_onset_symptoms = []

for patient in Patient.all_patients: #if patient.age_of_diagnosis is not None and patient.age_of_onset_symptoms is not None:
    if patient.age_of_diagnosis is not None and patient.age_of_onset_symptoms is not None:
        patient_age_of_diagnosis.append(patient.age_of_diagnosis)
        patient_age_of_onset_symptoms.append(patient.age_of_onset_symptoms)


X = patient_age_of_diagnosis  #independent variable
y = patient_age_of_onset_symptoms   #dependent variable

#Linear Regression 
X = np.array(patient_age_of_diagnosis).reshape(-1,1)
y = np.array(patient_age_of_onset_symptoms) 

model = LinearRegression()
model.fit(X, y)

#***********************
# P-VALUE CALCULATION
#***********************

# Calculates the Pearson correlation coefficient (r) and p-value
# between the x-values and y-values
r_value, p_value = stats.pearsonr(
    X.flatten(),  # Converts X from a 2D array into a 1D array
    y             # y-values being compared with X
)

# Prints the Pearson correlation coefficient
# This shows the strength and direction of the linear relationship
print(f"Pearson correlation = {r_value}")

# Prints the p-value
# This helps determine whether the correlation is statistically significant
print(f"p-value = {p_value}")

#SCATTER PLOT
plt.figure(4)


    #visualize these data on our scatter plot, by typing the following:
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color="red")

plt.xlabel('Age of Diagnosis')
plt.ylabel('Age of Onset Symptoms')
plt.title('Age of Diagnosis vs Age of Onset Symptoms')


# Annotate equation
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X,y)

equation = equation = (
    f"y = {slope:.2f}x + {intercept:.2f}\n"
    f"R^2 = {r2:.2f}\n"
    f"p = {p_value:.4f}"
)
plt.text(
    0.10, 0.95,
    equation,
    transform=plt.gca().transAxes,
    color="red",
    fontsize=12,
    verticalalignment="top",
    horizontalalignment="left"
)



# Call a single plt.show() at the very end to open all figure windows together
plt.show()

#do an outlier test for a better grade
#do more than one scatter plot and bar graph