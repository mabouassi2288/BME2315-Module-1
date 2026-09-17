import pandas as pd

df = pd.read_csv("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1/BME2315-Module-1/Metadata and Protein Data for Module 1.csv")

for column in df.columns:
    print(column)

