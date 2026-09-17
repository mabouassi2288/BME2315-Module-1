import csv

with open("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/Metadata and Protein Data for Module 1.csv", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader) # Get the first row
        for h in headers:
            print(h)

class Patient: 

    all_patients = [] 

    def __init__(self, patient_ID: int, age_at_death: int, highest_education: str, ABeta42: float, pTAU: str = "n/a", cognitive_status: str = "n/a"): 
        self.patient_ID = patient_ID
        self.age_at_death = age_at_death
        self.highest_education = highest_education
        self.ABeta42 = ABeta42
        self.pTAU = pTAU
        self.cognitive_status = cognitive_status

        # Append each new dog to the list upon initialization
        Patient.all_patients.append(self)

    def __repr__(self):  
        return f"Patient ID {self.patient_ID}: ({self.age_at_death} | {self.highest_education} | ABeta42: {self.ABeta42} | pTAU: {self.pTAU} | {self.cognitive_status})" 

    def get_age_at_death(self): 
        return self.age_at_death

    @classmethod
    def sum_ages(cls):
        total = 0
        for patient in Patient.all_patients:
            total += patient.age_at_death
        return total

    @classmethod
    def get_patient(cls, patient_ID):
        for patient in Patient.all_patients:
            if patient_ID == patient.patient_ID: 
                return patient

    @classmethod
    def print_sorted_by(cls, attribute_name: str, reverse: bool = False):
        sorted_list = sorted(
            cls.all_patients,
            key=lambda patient: getattr(patient, attribute_name),
            reverse=reverse,
        )
        print(f"\n--- Patients sorted by '{attribute_name}' ---")
        for patient in sorted_list:
            print(patient)

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        # your CSV loading code...
        pass

    @classmethod
    def filter(cls, list, patient_ID:str ="any", age_at_death:int ="any", highest_education:str ="any", ABeta42:float ="any", pTAU:str ="any", cognitive_status:str ="any"):
            all_patients = list
            remove_list = []
            attr_list = (
                        patient_ID,
                        age_at_death,
                        highest_education,
                        ABeta42,
                        pTAU,
                        cognitive_status
                        )
            attr_name = (
                        "patient_ID",
                        "age_at_death",
                        "highest_education",
                        "ABeta42",
                        "pTAU",
                        "cognitive_status"
                        )
            for attr in range(len(attr_list)):
                if attr_list[attr] != "any":
                    for patient in all_patients:
                        if getattr(patient,attr_name[attr]) != attr_list[attr]:
                            remove_list.append(patient)
                    all_patients = [patient for patient in all_patients if patient not in remove_list]
                    remove_list.clear()

            return all_patients


