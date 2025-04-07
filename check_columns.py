import pandas as pd

df = pd.read_csv("data/mpesa_cleaned.csv")
print("✅ Column names in your CSV file:")
print(df.columns.tolist())
