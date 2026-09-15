import pandas as pd

df = pd.read_csv("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/Metadata and Protein Data for Module 1.csv")

for column in df.columns:
    print(column)

"""
# 1, 2, 3. Define Class, Constructor, and Representer
class Patient:
    def __init__(self, patient_id, sex, age, protein_level):
        self.patient_id = patient_id
        self.sex = str(sex).strip().capitalize()
        self.age = float(age) if pd.notnull(age) else df.nan
        self.protein_level = float(protein_level) if pd.notnull(protein_level) else df.nan

    def __repr__(self):
        """Representer defining what is printed for a Patient object."""
        return f"Patient(ID={self.patient_id}, Sex='{self.sex}', Age={self.age}, Protein={self.protein_level})"

    # 6. Class Method to Filter Data
    @classmethod
    def filter_by_sex(cls, patient_list, sex):
        """Filters a list of Patient objects by sex (e.g., 'Female' or 'Male')."""
        return [p for p in patient_list if p.sex.lower() == sex.lower()]

# 4. Instantiate Patient Objects from CSV
csv_path = "/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/Metadata and Protein Data for Module 1.csv"

# Load data
df = pd.read_csv(csv_path)

"""