import pandas as pd

df = pd.read_csv("C:/Users/ibi_d/OneDrive/UVA/BME 2315/Module 0/BME2315-Module-1/Metadata and Protein Data for Module 1.csv")

for column in df.columns:
    print(column)