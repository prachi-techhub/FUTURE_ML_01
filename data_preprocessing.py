import pandas as pd
from pathlib import Path

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Path to the dataset
DATA_PATH = PROJECT_DIR / "data" / "Sample - Superstore.csv"

# Load the dataset
df = pd.read_csv(DATA_PATH, encoding="latin1")

# Display the first five rows
print("\nFIRST FIVE ROWS:")
print(df.head())

# Display the number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Display all column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Check data types and missing values
print("\nDATASET INFORMATION:")
df.info()

print("\nMISSING VALUES:")
print(df.isnull().sum())

# Check the date and sales columns
print("\nORDER DATE EXAMPLES:")
print(df["Order Date"].head())

print("\nSALES SUMMARY:")
print(df["Sales"].describe())