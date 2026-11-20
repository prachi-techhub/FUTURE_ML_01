import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------
# 1. Set project paths
# --------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_DIR / "data" / "Sample - Superstore.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------
# 2. Load the dataset
# --------------------------------

df = pd.read_csv(DATA_PATH, encoding="latin1")

print("Original dataset shape:", df.shape)

# --------------------------------
# 3. Remove duplicate records
# --------------------------------

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)

# --------------------------------
# 4. Convert Order Date to datetime
# --------------------------------

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

# --------------------------------
# 5. Clean the Sales column
# --------------------------------

df["Sales"] = pd.to_numeric(
    df["Sales"],
    errors="coerce"
)

# --------------------------------
# 6. Handle missing values
# --------------------------------

print("\nMissing values before cleaning:")
print(df[["Order Date", "Sales"]].isnull().sum())

# Remove rows without a valid date or sales value
df = df.dropna(subset=["Order Date", "Sales"])

# Sales cannot be negative in this forecasting project.
# Remove invalid negative sales values.
df = df[df["Sales"] >= 0]

print("\nMissing values after cleaning:")
print(df[["Order Date", "Sales"]].isnull().sum())

print("\nCleaned dataset shape:", df.shape)

# --------------------------------
# 7. Create monthly sales totals
# --------------------------------

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Month"] = monthly_sales["Month"].dt.to_timestamp()

monthly_sales = monthly_sales.sort_values("Month")

print("\nMONTHLY SALES:")
print(monthly_sales.to_string(index=False))

# --------------------------------
# 8. Save monthly sales data
# --------------------------------

monthly_sales.to_csv(
    OUTPUT_DIR / "monthly_sales.csv",
    index=False
)

# --------------------------------
# 9. Plot monthly sales
# --------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["Month"],
    monthly_sales["Sales"],
    marker="o",
    linewidth=2
)

plt.title("Historical Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_sales.png",
    dpi=300
)

plt.show()

print("\nMonthly sales analysis completed successfully!")
print("Monthly data saved in the outputs folder.")
print("Sales graph saved in the outputs folder.")