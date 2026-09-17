import csv

# Opens CSV file and prints each column line by line
with open(
    "/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1 INDIVIDUAL ASSIGNMENT/MODULE-1-INDIVIDUAL-ASSIGNMENT/Metadata and Protein Data for Module 1.csv",
    newline=""
) as f:
    reader = csv.reader(f)
    headers = next(reader)  # Get the first row

    for h in headers:
        print(h)


# ---------------------------------------------------------------------------------------------------------------------------
# STEP 1: Define a Class of "patient objects".
# ---------------------------------------------------------------------------------------------------------------------------

class Patient:

    all_patients = []

    # -----------------------------------------------------------------------------------------------------------------------
    # STEP 2: Make a "constructor" (__init__) that lists the different attributes
    # that you want your patient objects to have.
    # -----------------------------------------------------------------------------------------------------------------------

    def __init__(self,sex: str,age_at_death: int,highest_education: str,ABeta42: float,pTAU: str = "n/a",cognitive_status: str = "n/a"):
        self.sex = sex
        self.age_at_death = int(age_at_death)
        self.highest_education = highest_education
        self.ABeta42 = float(ABeta42)
        self.pTAU = pTAU
        self.cognitive_status = cognitive_status

        # Append each new patient to the list upon initialization
        Patient.all_patients.append(self)


    # -----------------------------------------------------------------------------------------------------------------------
    # STEP 3: Make a "representer" (__repr__) that defines what is shown
    # when you print a patient object.
    # -----------------------------------------------------------------------------------------------------------------------

    def __repr__(self):

        return (
            f"(sex: {self.sex} | "
            f"{self.age_at_death} | "
            f"{self.highest_education} | "
            f"ABeta42: {self.ABeta42} | "
            f"pTAU: {self.pTAU} | "
            f"{self.cognitive_status})"
        )


    # Getter instance method that returns a specific patient's age at death
    def get_age_at_death(self):

        return self.age_at_death


    # -----------------------------------------------------------------------------------------------------------------------
    # Class method that iterates through all_patients to calculate
    # the cumulative sum of patient ages at death
    # -----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def sum_ages(cls):

        total = 0

        for patient in cls.all_patients:
            total += patient.age_at_death

        return total


    # -----------------------------------------------------------------------------------------------------------------------
    # Class method searches through all the patient IDs and returns
    # the matching patient instance
    # -----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def get_patient(cls, patient_ID):

        for patient in cls.all_patients:

            if patient_ID == patient.patient_ID:
                return patient


    # -----------------------------------------------------------------------------------------------------------------------
    # Retrieves the attribute value for sorting and creates a sorted
    # copy of patient list based on attribute, then prints each patient line-by-line
    # -----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def print_sorted_by(cls, attribute_name: str, reverse: bool = False):

        sorted_list = sorted(
            cls.all_patients,
            key=lambda patient: getattr(patient, attribute_name),
            reverse=reverse
        )

        print(f"\n--- Patients sorted by '{attribute_name}' ---")

        for patient in sorted_list:
            print(patient)


    # -----------------------------------------------------------------------------------------------------------------------
    # STEP 4: Implement CSV
    # -----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def instantiate_from_csv(cls, filename: str):

        with open(filename, newline="") as f:

            reader = csv.DictReader(f)

            for row in reader:

                cls(
                    sex=row["Sex"],
                    age_at_death=int(row["Age at Death"]),
                    highest_education=row["Highest level of education"],
                    ABeta42=float(row["ABeta42 pg/ug"]),
                    pTAU=row["pTAU pg/ug"],
                    cognitive_status=row["Cognitive Status"]
                )


    # -----------------------------------------------------------------------------------------------------------------------
    # STEP 5: Filter patients based on specific attributes
    #used AI to inform me on how to filter patients correctly, as I had been doing
    # -----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def filter(
        cls,
        list,
        patient_ID="any",
        sex="any",
        age_at_death="any",
        highest_education="any",
        ABeta42="any",
        pTAU="any",
        cognitive_status="any"
    ):

        all_patients = list
        remove_list = []

        attr_list = (
            patient_ID,
            sex,
            age_at_death,
            highest_education,
            ABeta42,
            pTAU,
            cognitive_status
        )

        attr_name = (
            "patient_ID",
            "sex",
            "age_at_death",
            "highest_education",
            "ABeta42",
            "pTAU",
            "cognitive_status"
        )

        for attr in range(len(attr_list)):

            if attr_list[attr] != "any":

                for patient in all_patients:

                    if getattr(patient, attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)

                all_patients = [
                    patient
                    for patient in all_patients
                    if patient not in remove_list
                ]

                remove_list.clear()

        return all_patients


    # -----------------------------------------------------------------------------------------------------------------------
    # STEP 6: Make a class method to filter and print a sub-set of patients
    # based on at least two specific attributes
    #
    # Here:
    # 1. Patient died in their 80s
    # 2. Patient has ABeta42 below max_abeta
    # -----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def print_patients_in_80s_low_abeta(cls, max_abeta: float = 50.0):

        filtered_patients = [
            patient
            for patient in cls.all_patients
            if 80 <= patient.age_at_death < 90
            and patient.ABeta42 < max_abeta
        ]

        print(
            f"\n--- Patients who died in their 80s "
            f"with ABeta42 < {max_abeta} ---"
        )

        for patient in filtered_patients:
            print(patient)

        return filtered_patients


